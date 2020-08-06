
# Identity Clonning

[![GitHub license](https://img.shields.io/github/license/titanlambda/identity-cloning)](https://github.com/titanlambda/identity-cloning/blob/master/LICENSE) [![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Ftitanlambda%2Fidentity-cloning)](https://twitter.com/intent/tweet?text=Check%20out%20the%20Identity%20Cloning%20project%20to%20see%20how%20to%20clone%20yourself%20using%20next-generation%20AI%20to%20trigger%20a%20social%20engineering%20attack.%20%23security%20%23socialengineering%20%23phishing&url=https%3A%2F%2Fgithub.com%2Ftitanlambda%2Fidentity-cloning)

I am releasing this project as part of my talk in Black Hat USA 2020 conference. More details here - https://www.blackhat.com/us-20/briefings/schedule/index.html#how-i-created-my-clone-using-ai---next-gen-social-engineering-19802

Here is an interview with Dark Reading talking about this project:

[![](https://i.vimeocdn.com/video/929512576.webp)](https://vimeo.com/441393679 "Dark Reading News Room - Attack of the clone")


This project is inspired by the first episode of the season 2 of Black Mirror called "Be Right Back". Here we tried to create a pipeline using various AI projects to create a bot who talks like me and can be used to impersonate me online and do social engineering. The objective of this prototype is to simulate a Google hangout video call where someone can talk to the bot over a video call which will look like me and say in my voice with similar kind of response what I prefer to give based on my personality.

### Output: 
- Here are few sample output of text chat with the bot which is trained with my conversational data:
![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/text_demo.png)

- Here is a video demonstration where someone is talking to the bot and the bot is trying to do a social engineering by asking for money.

- [![](http://img.youtube.com/vi/-bhIL2qnXxc/0.jpg)](http://www.youtube.com/watch?v=-bhIL2qnXxc "Social engineering attempt with a bot making hangout call and asking for money")

### Pre-requisite: 
- We will be using virtualenv to create virtual environments. You can you other options like Conda if are familiar to that. 
- Python 3.7 used for this project
- Here we will explain how to run all the componenets locally except the fake video generation server. For that we will require a server with GPU. 


### Flow summary: 
![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/flow.png)
The entire project has mainly 3 componenets:
- Brain - NLP engine which will respond to a question with a similar utterance of mine.
- Voice - Voice cloning which will clone my voice and say the response generated in the previous step (Work In Progress, as of now we are using google text to speech engine.)
- Face - Video generation where we used [LipGAN](https://github.com/Rudrabha/LipGAN) library to generate video at runtime and play in response of the question asked as if the user is talking to a person.

### Architecture: 
![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/architecture.png)


### 1. Install virtualenv
---

```
pip install virtualenv
```

### 2. Clone the repo
---

```
git clone https://github.com/titanlambda/identity-clonning.git
cd identity-clonning/
```

It has following componenets:
1. 1_data_processor - to process social network data - FB, hangouts, whatsapp and create data set to train the NLP engine
2. 2_rasa_chitchat - Rasa chatbot code to handle chitchat
3. 3_ParlAI - Generative model to handle random questions
4. 4_chatterbot - To handle historical questions trained with the social networking data
5. 5_pipeline - Audio/Video streamer and google hangout integration to make it live in action


### 3. Process Social Network data
---

**Pre-requisite - export your social networking chat data from whatsapp, hangouts and FB.**
- [Export Whatsapp data](https://www.zapptales.com/en/how-to-export-whatsapp-chat-android-iphone-ios/)
- [Export FB data](https://www.zapptales.com/en/download-facebook-messenger-chat-history-how-to/)
- [Export Hangout data](https://blog.jay2k1.com/2014/11/10/how-to-export-and-backup-your-google-hangouts-chat-history/) - use JSON format as exported format

#### Create and activate virtual env
```
cd 1_data_processor
virtualenv venv_data_processor
source venv_data_processor/bin/activate
pip install -r requirements.txt
```
##### Copy the data files in data folders as per the names - 1_whatsapp_data, 2_hangout_data, 3_facebook_data then run the following command
```
python 1_whatsappParser.py
python 2_hangoutJsonParser.py
python 3_facebookParser.py
python 4_mergeAllData.py
```

##### You should get the final output data file "ALL_chatterbot_FINAL.csv" inside output folder. We will be using this file in step 4_chatterbot

![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/Categories%20of%20conversation.png)

### 4. Set up RASA chitchat server
---

![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/cat1_RASA.png)


0. Open a new terminal

``` 
cd 2_rasa_chitchat
virtualenv venv_rasa_chitchat
source venv_rasa_chitchat
pip install -r requirements.txt
rasa train
```

test - chat with the bot:
```
rasa shell
```

Run in production:
```
rasa run --enable-api
```

### 5. Set up RASA Action server
---

![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/cat3_RASA_actions.png)

**Pre-requisite - You need to get API keys as mentioned in the actions/actions.py file and put it there. Also you need to set up ParlAI and Chatterbot app server and mention the URLs of those servers in the actions.py file.**

Open a new terminal

```
cd 2_rasa_chitchat
source venv_rasa_chitchat
cd actions
pip install -r requirements.txt
rasa run action
```


### 6. Set up ParlAI server
---

![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/cat4_ParlAI.png)

```
git clone https://github.com/titanlambda/ParlAI.git
cd ParlAI
virtualenv venv_ParlAI
source venv_ParlAI/bin/activate
python setup.py develop
pip install tornado
pip install 'git+https://github.com/rsennrich/subword-nmt.git#egg=subword-nmt'
```

### 7. Run ParlAI server
---

##### It has 2 server componenets - socket server on port 10001 and then http server on 8080


#### Terminal 1: Open the socket server

```
cd ParlAI
python parlai/chat_service/services/websocket/run.py --config-path parlai/chat_service/tasks/chatbot/config.yml --port 10001
```
#### Terminal 2: Open the http server

```
cd ParlAI
python parlai/chat_service/services/browser_chat/client.py --port 10001 --host localhost --serving-port 8080
```

#### Test from the client

##### OPTION 1: Through Terminal
```
cd ParlAI
python client_tb -m "Hi"
```
##### OPTION 2: Through browser
Open browser and go to http://localhost:8080 and start typing the message

**IMP: Always type "begin" as the first message to start the server.**


### 8. Setup and run Chatterbot server
---

![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/cat2_chatterbot.png)

Open a new terminal

- Create a new virtual env
```
virtualenv venv_chatterbot
```

- Activate the venv
```
source venv_chatterbot
```

```
cd 4_chatterbot
pip install -r requirements.txt
```

- Train the model: copy "ALL_chatterbot_FINAL.csv" from data processor to the data folder here then run 

```
python train.py
```

- Launch the app server on port 5000

```
python app.py
```

---
### 9. Run the video streamer
---

![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/Video_Streamer_architecture.png)


- In the pipeline folder, record one video of you sitting and doing nothing as if you are listening to the audio over the zoom call. Example given in the source folder called "silent.m4v". Make sure the video is of 480p resolution

- ![](https://github.com/titanlambda/identity-cloning/blob/master/sample_output/silent.gif)

- Go to google tesxt to speech service and register there to get an API key. It should be in a file called "key.json". Download the file and save it in this folder.

Open a new terminal

``` 
cd 5_pipeline
virtualenv venv_pipeline
source venv_pipeline
pip install -r requirements.txt
python streamerV4.py
```




---
### 10. Run the audio speech to text engine
---
Open a new terminal

``` 
cd 5_pipeline
source venv_pipeline
pip install -r requirements.txt
python audio_recognition.py
```


---
### 11. Set up the server (with GPU) which will generate the lip-sync video.
---
WORK IN PROGRESS. I WILL BE RELEASING THIS PART SOON...

## Contribution

Please feel free to provide your:
- feedback
- suggestions
- Any other comment
- If you want to contribute or help me to improve it with some better componenets

## TO DO

- Will improve the documentation
- Improve API calling mechanism
- Simpler deployment

## Future Roadmap

Following features will be added in the future:
- personality analysis
- emotion and sentiment analysys
- Adding knowledge base to improve the genuinity of the bot

## Contact

- You can reach me at tamaghna.basu@gmail.com



