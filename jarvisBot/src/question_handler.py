from datetime import datetime

from dbConnector import dbConnector
from notifier import Notifier


class QuestionHandler:
    def __init__(self):
        self.db_connector = dbConnector()
        self.notifier = Notifier()

    def is_good_question(self, Unity_id, question):
        deadline = datetime.now()
        deadline = deadline.strftime("%Y-%m-%dT%H:%M:%SZ")
        tags = self.db_connector.get_tags_valid_submissions(deadline)
        if '?' in question:
            question = question.replace('?',' ').replace(','," ").replace("'"," ").strip().split(' ')
            # question = question.split(' ')
            while("" in question) : 
                question.remove("") 
            for i in question:
                if i in tags:
                    self.db_connector.update_reward_table(Unity_id, 'GoodQuestion')
                    self.notifier.notify("You received a Good Question Reward for posting a relevant question",
                                         Unity_id)
                    break
