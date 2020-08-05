import csv
import re
from functools import reduce
from pathlib import Path

from bs4 import BeautifulSoup
from tqdm import tqdm

from dataHandler import csv_columns, SocialNetwork, output_dir


def messageFileKey(file):
    match = re.search(r'message_(\d+).html', str(file))
    return int(match.group(1))


def parseMessage(block):
    children = block.div.find_all(recursive=False)
    message = children[1].find(text=True, recursive=False)
    if message != None:
        message = ' '.join(message.split())
    return message


def parseMessageBlock(block):
    author = block.select('div._3-96._2pio._2lek._2lel')[0].getText()
    message = parseMessage(block.select('div._3-96._2let')[0])
    return (author, message)


def parseFile(file):
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        blocks = soup.select(
            'html body._5vb_._2yq._4yic div.clearfix._ikh div._4bl9 div._li div._3a_u div._4t5n div.pam._3-95._2pi0._2lej.uiBoxWhite.noborder')
        messages = []
        for block in blocks[::-1]:
            messages.append(parseMessageBlock(block))
        return messages


def filterMessages(messages):
    return filter(lambda message: message[1] != None, messages)


def mergeMessages(messages):
    def reducer(acc, message):
        if len(acc) == 0:
            return [message]

        (lastAuthor, lastMessage) = acc[-1]
        (currentAuthor, currentMessage) = message
        if lastAuthor != currentAuthor:
            return acc + [message]
        else:
            newMessage = ' '.join([lastMessage, currentMessage])
            return acc[:-1] + [(currentAuthor, newMessage)]

    return reduce(reducer, messages, [])


# TODO - Refactor this method to use the standard CSV write method from dataHandler
def saveMessages(messages, personName):
    csv_file_name = "{}/{}_FINAL.csv".format(output_dir, SocialNetwork.Facebook.name)
    with open(csv_file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(csv_columns)
        for msg1, msg2 in zip(messages[::2], messages[1::2]):
            author1, message1 = msg1
            author2, message2 = msg2

            if author1 == personName:
                writer.writerow([message2, message1])
            else:
                writer.writerow([message1, message2])


def getFBConversationData(messagePath):
    print("Find messenger files...")
    messageFiles = Path(messagePath).rglob('message*.html')
    messageFiles = sorted(messageFiles, key=messageFileKey, reverse=True)
    print("Parse files... {} ".format(messageFiles))
    messages = []
    totalFileCount = 0
    errorFileCount = 0
    for messageFile in tqdm(messageFiles):
        totalFileCount += 1
        chatData = ""
        try:
            chatData = parseFile(messageFile)
        except:
            print("######################@@@@\n Error Parsing {}".format(messageFile))
            errorFileCount += 1
        if chatData != "":
            messages = messages + chatData

    print("Filter and merge files...")
    messages = filterMessages(messages)
    messages = mergeMessages(messages)
    return messages, totalFileCount, errorFileCount


if __name__ == '__main__':
    me = "Tamaghna Basu"
    messagePath = "./3_facebook_data/inbox"
    messages, totalFileCount, errorFileCount = getFBConversationData(messagePath)
    saveMessages(messages, me)
    print("Conversations saved! \n Total files {}, Error in files {}".format(totalFileCount, errorFileCount))
