import asyncio
import json
import _thread
# from pprint import pprint
import configparser

from mattermostdriver import Driver
from event_handler import EventHandler
from question_handler import QuestionHandler
from queryDB import queryDB
from init import get_driver

config=configparser.ConfigParser()
config.read('config.ini')
event_handler = EventHandler()
question_handler = QuestionHandler()


class Listener:


    def __init__(self,bot_name):
        self.bot_name = bot_name
        self.DIRECT_CHANNEL = "D"
        self.EVENT_POSTED = "posted"
        self.QUESTIONS_CHANNEL = "questions"

    @asyncio.coroutine
    def my_event_handler(self, message):
        message = json.loads(message)
        # pprint(message)
        if 'event' in message.keys() and message['event'] == self.EVENT_POSTED:
            # print(message)
            post = json.loads(message["data"]["post"])
            user_id = client.users.get_user_by_username(self.bot_name)["id"]

            if message['data']["channel_name"] == self.QUESTIONS_CHANNEL:
                # send it to the Question handler
                print(post['message'])
                user_email = client.users.get_user(post["user_id"])["email"]
                question_handler.is_good_question(user_email, post['message'].lower())

            elif message['data']['channel_type'] == self.DIRECT_CHANNEL and post["user_id"] != user_id:
                # send it to event handler
                print(post['message'])
                user_email = client.users.get_user(post["user_id"])["email"]
                event_handler.interpret(user_email, post['message'])

def start_queryDB():
    queryDB()

if __name__ == '__main__':
    try:
        _thread.start_new_thread(start_queryDB, ())
    except:
        print("FATAL ERROR: Could not start queryDB")
    print("Created new thread for queryDB. Starting listener.")
    bot_name = config.get('myvars','BOTNAME')
    listener = Listener(bot_name)
    host = config.get('myvars','HOST')
    team = config.get('myvars','TEAMNAME')
    client = get_driver()
    client.login()
    client.init_websocket(listener.my_event_handler)
