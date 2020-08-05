# -*- coding: utf-8 -*-

# %%

##############################################################################################################
# Global Constants
# Register on https://newsapi.org and get an API KEY and put it here
NEWS_API_KEY = ''


# Register on http://api.weatherstack.com and get an API KEY and put it here
weatherstack_api_key = ''

parlAI_base_url = "http://localhost:8080"
chatterbot_base_url = "http://localhost:5000"



##############################################################################################################

# %%

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
import json

from rasa_sdk import Action
import logging

from rasa_sdk.forms import FormAction, REQUESTED_SLOT, Action
from rasa_sdk import ActionExecutionRejection
from rasa_sdk.events import SlotSet, FollowupAction

logger = logging.getLogger(__name__)

def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

def reset_ParlAI_conversations():
    import requests
    url = "{}/reset".format(parlAI_base_url)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers)

    import json
    response_json = json.loads(response.text)
    response_text = response_json['text']

    print(response_text)
    logger.debug("reset_ParlAI_conversations: message - {}".format(response_text))
    return response_text


def send_message_to_external_AI(user_message):
    words = user_message.split()
    if len(words) >= 3:
        message, response_confidence = send_message_to_Chatterbot(user_message)
        print("User message: {}, Response from chatterbot: {}, Confidence: {}".format(user_message, message, response_confidence))
        if response_confidence < 0.9:
            message = sendToParlAI(user_message)
    else:
        message = sendToParlAI(user_message)
    return message


def sendToParlAI(user_message, silentMode=False):
    url = "{}/interact".format(parlAI_base_url)
    headers = {'Content-Type': 'application/json'}
    response_text = ""
    if silentMode:
        asyncReq(url, headers=headers, data=user_message)
    else:
        import requests
        response = requests.request("POST", url, headers=headers, data=user_message)
        import json
        response_json = json.loads(response.text)
        response_text = response_json['text']
        print(response_text)
        logger.debug("send_message_to_ParlAI: message - {}".format(response_text))

    return response_text

def asyncReq(url, headers, data):
    from requests_futures.sessions import FuturesSession
    session = FuturesSession()
    session.post(url, headers=headers, data=data)


def send_message_to_Chatterbot(user_message):
    import requests

    url = "http://localhost:5000/service"

    payload = "{\"data\" : \"" + user_message + "\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    import json
    response_json = json.loads(response.text)
    response_text = response_json['text']
    response_confidence = response_json['confidence']

    log_message = "#############################\n" \
                  "send_message_to_Chatterbot:\n " \
                  "response - {},\n " \
                  "confidence - {}".format(response_text, response_confidence)
    # print(log_message)
    logger.debug(log_message)
    return response_text, response_confidence


class JokeTellerAction(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_tell_joke"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        sender = tracker.sender_id
        print("################### sender: {}".format(sender))
        request = json.loads(
            requests.get('https://official-joke-api.appspot.com/jokes/random').text)  # make an apie call
        setup = request['setup']
        punchline = request['punchline']
        message = setup + ' ' + punchline
        message = "Hear this. {}".format(message)
        logger.debug("action_tell_joke: message - {}".format(message))
        print("action_tell_joke: message - {}".format(message))
        dispatcher.utter_message(message)  # send the message back to the user
        return []


class WeatherTellerAction(Action):

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_tell_weather"

    @staticmethod
    def getWeatherInfo(location):
        params = {
            'access_key': weatherstack_api_key,
            'query': location
        }

        api_result = requests.get('http://api.weatherstack.com/current', params)

        api_response = api_result.json()
        print(api_response)
        description = api_response['current']['weather_descriptions'][0]
        response = u'Current temperature in %s is %d degree celsius. Seems %s' % (
            api_response['location']['name'], api_response['current']['temperature'], description)
        image = api_response['current']['weather_icons']
        print(response)
        print(api_response['current']['weather_icons'])
        print(api_response['current']['weather_descriptions'])
        return response, image

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        # get all the entities extracted by rasa
        entities = tracker.latest_message['entities']

        # cycle through them and extract the relavant one for us
        location = None
        for e in entities:
            if e['entity'] == "user_location":
                location = e['value']
        if location:
            message, image = self.getWeatherInfo(location)
        else:
            message, image = self.getWeatherInfo('fetch:ip')
        print("action_tell_weather: message - {}".format(message))
        # message = [{"text": message},{"image":image}]
        dispatcher.utter_message(message)  # send the message back to the user
        # dispatcher.utter_message(template = "utter_aget.tell_weather", message=message, image=image)  # send the message back to the user
        return []


class FallBackAction(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_fallback_lmgtfy"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        print(tracker.latest_message)
        user_input = tracker.latest_message['text']
        user_input = self.urlify(user_input)
        message = send_message_to_external_AI(user_input)
        logger.debug("action_fallback_lmgtfy_parlAI: message - {}".format(message))
        dispatcher.utter_message(message)  # send the message back to the user
        return []

    def urlify(self, s):
        import re
        # Remove all non-word characters (everything except numbers and letters)
        s = re.sub(r"[^\w\s]", '', s)
        # Replace all runs of whitespace with a single dash
        s = re.sub(r"\s+", '+', s)
        return s


class InitializeParlAIAction(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_initialize_ParlAI"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        sendToParlAI('begin')
        sendToParlAI('begin')
        sendToParlAI('begin')
        logger.debug("action_initialize_ParlAI initilize")
        return []


class ParlAISendMessageAction(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_send_to_ParlAI"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        print(tracker.latest_message)
        user_input = tracker.latest_message['text']
        logger.debug("action_send_to_ExternalAI: message - {}".format(user_input))
        message = send_message_to_external_AI(user_input)
        logger.debug("action_send_to_ParlAI: message - {}".format(message))
        dispatcher.utter_message(message)  # send the message back to the user
        return []


class ParlAISendSilentMessageAction(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_send_silently_to_ParlAI"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        print(tracker.latest_message)
        user_input = tracker.latest_message['text']
        message = sendToParlAI(user_input, silentMode=True)
        logger.debug("action_send_to_ParlAI: message - {}".format(message))
        return []


def who_is(query):
    summary = ""
    if not isBlank(query):
    # if query is not None and len(query.strip()) > 0:
        import wikipedia
        try:
            summary =  wikipedia.summary(query, chars=100)
        except Exception:
            for new_query in wikipedia.search(query):
                try:
                    summary = wikipedia.summary(new_query, chars=100)
                except Exception:
                    pass

    if len(summary) > 1500:
        summary = summary[: 500]
    return summary


class DefinitionTellerAction(Action):

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_tell_definition"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        # get all the entities extracted by rasa
        entities = tracker.latest_message['entities']

        # cycle through them and extract the relavant one for us
        word = None
        for e in entities:
            if e['entity'] == "word":
                word = e['value']
        message = who_is(word)
        if isBlank(message) :
            send_message_to_external_AI(word)
        print("action_tell_definition: message - {}".format(message))
        dispatcher.utter_message(message)  # send the message back to the user
        return []


class TriviaTellerAction(Action):

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_tell_trivia"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        # get all the entities extracted by rasa
        entities = tracker.latest_message['entities']

        # cycle through them and extract the relavant one for us
        attribute = None
        entity = None
        for e in entities:
            if e['entity'] == "attribute":
                attribute = e['value']
            elif e['entity'] == "entity":
                entity = e['value']

        if isBlank(attribute) or isBlank(entity):
            user_input = tracker.latest_message['text']
            message = send_message_to_external_AI(user_input)
        else:
            query = "{} of {}".format(attribute, entity)
            message = who_is(query)

        print("action_tell_trivia: message - {}".format(message))
        dispatcher.utter_message(message)  # send the message back to the user
        return []


class DateTimeTellerAction(Action):

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_tell_date_time"

    @staticmethod
    def getTime():
        from datetime import datetime
        import pytz

        timezone = 'Asia/Calcutta'
        tz_India = pytz.timezone(timezone)
        datetime_India = datetime.now(tz_India)
        time_string = datetime_India.strftime("%H:%M")
        date_string = datetime_India.strftime("%B %d")
        print("Time zone - {}, date - {}, time - {}".format(timezone, date_string, time_string))
        return date_string, time_string

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        # get all the entities extracted by rasa
        entities = tracker.latest_message['entities']

        # cycle through them and extract the relavant one for us
        user_location = None
        for e in entities:
            if e['entity'] == "user_location":
                user_location = e['value']
        currentDate, currentTime = self.getTime()
        if user_location is not None:
            message = "Not sure about the time in {}, but here the time is {}.".format(user_location, currentTime)
        else:
            message = "Here the time is {}.".format(currentTime)
        message += " And the date is {}.".format(currentDate)
        message += "Looks like you still think that I am a bot."
        print("action_tell_time: message - {}".format(message))
        dispatcher.utter_message(message)  # send the message back to the user
        return []


# A form action to fetch news from the internet
class getNews(FormAction):
    def name(self):
        return "get_news"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["topic_news"]

    def slot_mappings(self):
        return {"topic_news": [self.from_text(intent=[None, "getNews", "inform"]),
                               self.from_entity(entity="topic_news", intent=["getNews"])]}

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        """Define what the form has to do
            after all required slots are filled"""

        topic_news = tracker.get_slot("topic_news")

        pageSize = '2'  # Set the number to how many news articles you want to fetch

        url = "https://newsapi.org/v2/everything?q=" + topic_news + "&apiKey=" + NEWS_API_KEY + "&pageSize=" + pageSize

        r = requests.get(url=url)
        data = r.json()  # extracting data in json format
        data = data['articles']

        dispatcher.utter_message("Here is some news I found!")

        for i in range(len(data)):
            output = data[i]['title'] + "\n" #  + data[i]['url'] + "\n"
            dispatcher.utter_message(output)

        dispatcher.utter_template("utter_confirm_if_service_is_correct", tracker)

        # utter submit template
        return []
