import json

from dataHandler import *

def parseData(jsonData):
    simpleJson = []
    for i in range(0, len(jsonData['conversations'])):
        conversation = {}
        conversation['chatName'] = ""
        conversation['participants'] = getParticipants(i)
        conversation['messages'] = []

        for j in range(0, len(jsonData['conversations'][i]['events'])):
            message = {}
            message['sender'] = {}
            message['sender']['name'] = getName(
                jsonData['conversations'][i]['events'][j]['sender_id']['gaia_id'], conversation['participants'])
            message['sender']['id'] = jsonData['conversations'][i]['events'][j]['sender_id']['gaia_id']
            message['unixtime'] = (int(jsonData['conversations'][i]
                                       ['events'][j]['timestamp']))/1000000

            if 'chat_message' in jsonData['conversations'][i]['events'][j]:
                # if it's a message(normal hangouts, image...)
                if 'segment' in jsonData['conversations'][i]['events'][j]['chat_message']['message_content']:
                    # if it's a normal hangouts message
                    content = ""
                    for k in range(0, len(jsonData['conversations'][i]['events'][j]['chat_message']['message_content']['segment'])):
                        if jsonData['conversations'][i]['events'][j]['chat_message']['message_content']['segment'][k]['type'] == "TEXT":
                            content = content + \
                                jsonData['conversations'][i]['events'][j]['chat_message']['message_content']['segment'][k]['text']
                        elif jsonData['conversations'][i]['events'][j]['chat_message']['message_content']['segment'][k]['type'] == "LINK":
                            content = content + \
                                jsonData['conversations'][i]['events'][j]['chat_message']['message_content']['segment'][k]['text']
                    message['content'] = content

            conversation['messages'].append(message)

        simpleJson.append(conversation)
        simpleJson[i]['chatName'] = chatName(i, simpleJson)
    return simpleJson

def getParticipants(index):
    participants = []
    for i in range(0, len(jsonData['conversations'][index]['conversation']['conversation']['participant_data'])):
        person = {}
        person['id'] = jsonData['conversations'][index]['conversation']['conversation']['participant_data'][i]['id']['gaia_id']
        if 'fallback_name' in jsonData['conversations'][index]['conversation']['conversation']['participant_data'][i]:
            person['name'] = jsonData['conversations'][index]['conversation']['conversation']['participant_data'][i]['fallback_name']
        else:
            person['name'] = jsonData['conversations'][index]['conversation']['conversation']['participant_data'][i]['id']['gaia_id']
        participants.append(person)
    return participants

def getName(id, participants):
    for i in range(0, len(participants)):
        if id == participants[i]['id']:
            return participants[i]['name']
    return id

def chatName(i, simpleJson):
    if (('name' in jsonData['conversations'][i]['conversation']['conversation'])and(jsonData['conversations'][i]['conversation']['conversation']['name'] != "")):
        return jsonData['conversations'][i]['conversation']['conversation']['name']
    participants = []
    index = 0
    for k in range(0, len(simpleJson[i]['participants'])):
        participants.append(simpleJson[i]['participants'][k]['name'])
        if simpleJson[i]['participants'][k]['id'] == jsonData['conversations'][i]['conversation']['conversation']['self_conversation_state']['self_read_state']['participant_id']['gaia_id']:
            index = k
            break
    name = participants[index]
    return name

def getGoogleHangoutsData(personName, jsonData):
    responseDictionary = []
    """
        The key is the other person's message, and the value is my response
        Going through each file, and recording everyone's messages to me, and my
        responses
    """
    allChatterBotMessages = []

    for data in jsonData:
        if len(data['participants']) != 2:
            continue

        myMessage, otherPersonsMessage, currentSpeaker = "", "", ""
        chatterbotMessageList = []
        allLines = data['messages']

        for index, line in enumerate(allLines):
            if 'sender' not in line.keys() or 'content' not in line.keys():
                continue

            # Find messages that I sent
            if line['sender']['name'] == personName:
                if not myMessage:
                    # Want to find the first message that I send (if I send
                    # multiple in a row)
                    startMessageIndex = index - 1
                myMessage += " " + line['content'] + "."

            elif myMessage:
                # Now go and see what message the other person sent by looking at
                # previous messages
                for counter in range(startMessageIndex, 0, -1):
                    currentLine = allLines[counter]
                    # In case the message above isn't in the right format
                    if 'sender' not in currentLine.keys() or 'content' not in currentLine.keys():
                        break
                    if not currentSpeaker:
                        # The first speaker not named me
                        currentSpeaker = currentLine['sender']
                    elif currentSpeaker != currentLine['sender']:
                        # A different person started speaking, so now I know that
                        # the first person's message is done
                        otherPersonsMessage = cleanMessage(otherPersonsMessage)
                        myMessage = cleanMessage(myMessage)
                        writeConversationToResponseDictionary(myMessage, otherPersonsMessage, responseDictionary)
                        chatterbotMessageList.append(otherPersonsMessage)
                        chatterbotMessageList.append(myMessage)
                        break
                    otherPersonsMessage = currentLine['content'] + ". " + otherPersonsMessage
                myMessage, otherPersonsMessage, currentSpeaker = "", "", ""
        if len(chatterbotMessageList) > 0 :
            otherPersonName = data['participants'][0]['name']
            if otherPersonName == personName:
                otherPersonName = data['participants'][1]['name']
            # allChatterBotMessages.append(chatterbotMessageList)
            allChatterBotMessages.append({"Name": otherPersonName, "Conversation": chatterbotMessageList})
    return responseDictionary, allChatterBotMessages


if __name__ == '__main__':
    me = "Tamaghna Basu"

    # location of Hangouts Json file obtained from Google Takeout
    data_hangouts_json = './2_hangout_data/Hangouts.json'

    with open(data_hangouts_json, 'r') as f:
        jsonData = json.load(f)

    jsonData = parseData(jsonData)

    combinedDictionary, allChatterBotMessages = getGoogleHangoutsData(me, jsonData)
    print('Total len of dictionary', len(combinedDictionary))
    writeToFiles(combinedDictionary, SocialNetwork.Hangout)
