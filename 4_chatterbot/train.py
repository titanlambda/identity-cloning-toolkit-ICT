# -*- coding: utf-8 -*-
import enum

import numpy as np
import pandas as pd
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


class SocialNetworkType(enum.Enum):
    NONE = 0  # NONE
    H = 1  # Hangout
    W = 2  # Whatsapp
    F = 3  # Facebook
    ALL = 4


def getDatasetName(socialNetworkType):
    switcher = {
        SocialNetworkType.H: "Hangout",
        SocialNetworkType.W: "Whatsapp",
        SocialNetworkType.F: "Facebook",
        SocialNetworkType.ALL: "ALL"
    }

    csvFileName = ""
    dbFileName = "database_DEFAULT"

    if socialNetworkType == SocialNetworkType.NONE:
        csvFileName = ""
        dbFileName = "database_DEFAULT"
    else:
        networkType = switcher.get(socialNetworkType)
        if networkType is not None:
            csvFileName = "conversation_{}".format(networkType)
            dbFileName = "database_{}".format(networkType)
    return csvFileName, dbFileName


def isNotBlank(myString):
    return bool(myString and myString.strip())


def create_chatbot(socialNetworkType, isTrainedAlready=True):
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

    if not isTrainedAlready:
        print("Starting English corpus training...")
        train_on_english_corpus(chatbot)
        if isNotBlank(csvFileName):
            train_on_social_chat(chatbot, csvFileName)

    # Get a response to an input statement
    response = chatbot.get_response("Hello")
    print(response)
    print(response.confidence)
    response = chatbot.get_response("How are you today?")
    print(response)
    print(response.confidence)
    return chatbot


def train_on_english_corpus(chatbot):
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english")

    print("Done English corpus training...")


def train_on_social_chat(chatbot, dataset):
    csvFileName = 'dataset/csv/{}.csv'.format(dataset)

    print("Starting List training...")
    csv_columns = ['Message', 'MyResponse']
    df_all = pd.read_csv(csvFileName)
    df_all.replace(np.NaN, ' ', inplace=True)

    trainer = ListTrainer(chatbot)
    rowCount = df_all.shape[0]
    for index, row in df_all.iterrows():
        print("Training {} of {}".format(index, rowCount))
        message = row[csv_columns[0]]
        myResponse = row[csv_columns[1]]
        trainer.train([message, myResponse])

    print("Done List training...")


if __name__ == "__main__":
    isTrainedAlready = False
    chatbot = create_chatbot(SocialNetworkType.ALL, isTrainedAlready=isTrainedAlready)
