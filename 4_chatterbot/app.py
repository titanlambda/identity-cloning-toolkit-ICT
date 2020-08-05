#app.py

from flask import Flask, jsonify, request #import main Flask class and request object
import json
from talk import *

#create the Flask app
app = Flask(__name__)
chatbot = loadChatbot(SocialNetworkType.HWFMS)

@app.route('/service', methods=['POST'])
def service():
    json_request_body = json.loads(request.data)

    if json_request_body is None:
        return jsonify({"message":"text not found"})
    else:
	    text_message = json_request_body['data']
	    print(text_message)
	    bot_response = get_response_from_chatbot(chatbot, text_message)
	    print(bot_response)
	    response = {"text":bot_response.text, "confidence":bot_response.confidence}

	    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000