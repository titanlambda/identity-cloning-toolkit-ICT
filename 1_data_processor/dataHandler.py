import csv
import enum
import re

output_dir = "output"
csv_columns = ['Message', 'MyResponse']
class SocialNetwork(enum.Enum):
    Hangout = 1
    WhatsApp = 2
    Facebook = 3
    ALL = 4


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def cleanMessage(message):
    message = remove_emoji(message)
    # Remove new lines within message
    cleanedMessage = message.replace('\n', ' ')
    # Deal with some weird tokens
    cleanedMessage = cleanedMessage.replace("\xc2\xa0", "")
    # Remove punctuation
    # cleanedMessage = re.sub('([.,!?])', ' ', cleanedMessage)
    # Remove multiple spaces in message
    cleanedMessage = re.sub(' +', ' ', cleanedMessage)

    # Remove text based emjis - :-), :), ;), :D, :P, ;P, ;D, :(, :((, :))
    cleanedMessage = cleanedMessage.replace(":-)", "")
    cleanedMessage = cleanedMessage.replace(":)", "")
    cleanedMessage = cleanedMessage.replace(";)", "")
    cleanedMessage = cleanedMessage.replace(":D", "")
    cleanedMessage = cleanedMessage.replace(":P", "")
    cleanedMessage = cleanedMessage.replace(":-P", "")
    cleanedMessage = cleanedMessage.replace(";P", "")
    cleanedMessage = cleanedMessage.replace(";D", "")
    cleanedMessage = cleanedMessage.replace(":(", "")
    cleanedMessage = cleanedMessage.replace(":((", "")
    cleanedMessage = cleanedMessage.replace(":))", "")

    return cleanedMessage.strip()


def is_not_blank(s):
    return bool(s and s.strip())


def writeConversationToResponseDictionary(myMessage, otherPersonsMessage, responseDictionary):
    if is_not_blank(otherPersonsMessage) \
            and is_not_blank(myMessage):
        responseDictionary.append({"Message": otherPersonsMessage.strip(), "MyResponse": myMessage.strip()})


def writeToFiles(dict_data, socialNetworkType):
    output_dir = "output"
    messageFileName = '{}/message_{}.txt'.format(output_dir, socialNetworkType.name)
    myResponseFileName = '{}/myResponse_{}.txt'.format(output_dir, socialNetworkType.name)
    csv_file_name = "{}/{}_FINAL.csv".format(output_dir, socialNetworkType.name)

    print(messageFileName)
    print(myResponseFileName)
    print(csv_file_name)

    otherPersonsMessageFile = open(messageFileName, 'w')
    myMessageFile = open(myResponseFileName, 'w')

    try:
        with open(csv_file_name, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for message in dict_data:
                writer.writerow(message)
                otherPersonsMessageFile.write(message['Message'].strip() + "\n")
                myMessageFile.write(message['MyResponse'].strip() + "\n")
    except IOError:
        print("I/O error")
    otherPersonsMessageFile.close()
    myMessageFile.close()


if __name__ == '__main__':
    writeToFiles("", SocialNetwork.Hangout)
    writeToFiles("", SocialNetwork.LinkedIn)
    writeToFiles("", SocialNetwork.WhatsApp)
