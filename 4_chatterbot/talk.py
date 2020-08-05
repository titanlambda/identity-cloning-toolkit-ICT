# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.filters import get_recent_repeated_responses
from train import SocialNetworkType, getDatasetName

def loadChatbot(socialNetworkType):
	csvFileName, dbFileName = getDatasetName(socialNetworkType)

	chatbot = ChatBot(
			'Tamaghna Basu',
			filters=[
		        {
		            'import_path': 'chatterbot.filters.get_recent_repeated_responses',
		            'threshold': 1,
		            'quantity': 5
		        }
		    ],
		    storage_adapter='chatterbot.storage.SQLStorageAdapter',
			logic_adapters=[
		        {
		            'import_path': 'chatterbot.logic.BestMatch',
		            'default_response': 'I am sorry, but I do not understand. Please rephrase your question.',
		            'maximum_similarity_threshold': 0.90
		        }
			],
			database_uri='sqlite:///dataset/sqlite/{}.sqlite3'.format(dbFileName)

		)



	# Get a response to an input statement
	response = chatbot.get_response("Hello")
	print(response)
	print(response.confidence)
	return chatbot

def get_response_from_chatbot(chatbot, text_message):
	bot_response = chatbot.get_response(text_message)

	print(bot_response.confidence)
	return bot_response

	# if bot_response.confidence > 0.9:
	# 	return bot_response
	# else:
	# 	return "Sorry, not able to follow, can you please repharse it?"


if __name__ == "__main__":

	chatbot = loadChatbot(SocialNetworkType.ALL)

	while True:
	    try:
	    	print(get_response_from_chatbot(chatbot, input()))

	    except(KeyboardInterrupt, EOFError, SystemExit):
	        break
