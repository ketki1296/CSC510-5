import sched, time, datetime, os
from dbConnector import dbConnector
from notifier import Notifier
from git_connector import fetch_num_of_tasks
from form_reader import FormReader
#from mocker import start_mocking_git, start_mocking_forms, stop_mocking
import configparser

config=configparser.ConfigParser()
config.read('config.ini')

class queryDB:

    def __init__(self):
        self.professor = config.get('myvars','PROFESSOR')
        self.s = sched.scheduler(time.time, time.sleep)
        self.interval = 86400
        self.db_connector = dbConnector()
        self.notifier = Notifier()
        self.form_reader = FormReader()
        self.s.enter(1, 1, self.check_due_submission, (self.s,))
        self.s.run()

    def check_due_submission(self, sc):
        self.s.enter(self.interval, 1, self.check_due_submission, (sc,))
        current_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        results = self.db_connector.get_ungraded_submissions(current_date)

        left_to_grade = ",".join(results.keys())
        if len(results) > 0:
            self.notifier.notify("Should we start grading for " + left_to_grade, self.professor)
