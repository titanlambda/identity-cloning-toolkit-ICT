import os

from dataHandler import *

def getWhatsAppDataTXT(personName):
    # Putting all the file names in a list
    allFiles = []
    # Edit these file and directory names if you have them saved somewhere else

    for filename in os.listdir(dataDir):
        if filename.endswith(".txt"):
            allFiles.append('{}/{}'.format(dataDir, filename))

    responseDictionary = []
    """responseDictionary
        The key is the other person's message, and the value is my response
        Going through each file, and recording everyone's messages to me, and my
        responses
    """
    for currentFile in allFiles:
        myMessage, otherPersonsMessage, currentSpeaker = "", "", ""
        with open(currentFile, 'r') as openedFile:
            allLines = openedFile.readlines()
        for index, line in enumerate(allLines):
            # The sender's name is separated by a ']' or '-' and a ': ' (The whitespace is important)
            leftDelimPattern = re.compile(r'[\]\-]')
            # A pattern to match either `]` or `-`
            leftDelim = leftDelimPattern.search(line)
            leftDelim = leftDelim.start() if leftDelim else -1
            rightColon = line.find(': ')

            # Find messages that I sent
            if line[leftDelim + 1:rightColon].strip() == personName:
                if not myMessage:
                    # Want to find the first message that I send (if I send
                    # multiple in a row)
                    startMessageIndex = index - 1
                myMessage += " " + line[rightColon + 1:].strip() + "."

            elif myMessage:
                # Now go and see what message the other person sent by looking at
                # previous messages
                for counter in range(startMessageIndex, 0, -1):
                    currentLine = allLines[counter]
                    # Extracting the values of left and right delimiters
                    leftDelim = leftDelimPattern.search(currentLine)
                    leftDelim = leftDelim.start() if leftDelim else -1
                    rightColon = line.find(': ')
                    if (leftDelim < 0 or rightColon < 0):
                        # In case the message above isn't in the right format
                        myMessage, otherPersonsMessage, currentSpeaker = "", "", ""
                        break
                    if not currentSpeaker:
                        # The first speaker not named me
                        currentSpeaker = currentLine[leftDelim + 1:rightColon].strip()
                    elif (currentSpeaker != currentLine[leftDelim + 1:rightColon].strip()):
                        # A different person started speaking, so now I know that
                        # the first person's message is done
                        otherPersonsMessage = cleanMessage(otherPersonsMessage)
                        myMessage = cleanMessage(myMessage)
                        writeConversationToResponseDictionary(myMessage, otherPersonsMessage, responseDictionary)
                        break
                    otherPersonsMessage = currentLine[rightColon + 1:].strip() + " " + otherPersonsMessage
                myMessage, otherPersonsMessage, currentSpeaker = "", "", ""
    return responseDictionary


if __name__ == '__main__':
    personName = "Tamaghna Basu"
    dataDir = '1_whatsapp_data'

    combinedDictionary = getWhatsAppDataTXT("Tamaghna Basu neoEYED")
    print(combinedDictionary)

    print('Total len of dictionary', len(combinedDictionary))
    writeToFiles(combinedDictionary, SocialNetwork.WhatsApp)


