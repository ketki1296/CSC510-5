from dbConnector import dbConnector
from notifier import Notifier
from form_reader import FormReader
# from mocker import start_mocking_git, start_mocking_forms, stop_mocking
from git_connector import fetch_last_commit, fetch_num_of_tasks
import datetime, os
import configparser

config=configparser.ConfigParser()
config.read('config.ini')

class EventHandler:

    def __init__(self):
        self.professor = config.get('myvars','PROFESSOR')
        self.db_connector = dbConnector()
        self.notifier = Notifier()
        self.form_reader = FormReader()
        self.error_message = """Error! Command not found. Available Commands:\n
                             create-submission <name> <Deadline YYYY/MM/DD-HH:MM> <# issues> <Submission Link>\n
                             add-keywords <name> <comma-separated tags Ex: tag1,tag2>\n
                             start-grading <name>\n
                             show-rewards\n"""

    def interpret(self, user_email, commandInput="/create-submission def  2019-10-25 5 http://test.com "):
        parameters = commandInput.strip().split()
        self.handle_events(user_email, parameters[0], parameters[1:])

    def handle_events(self, email, keyword, parameters):
        if email == self.professor:
            if keyword == "create-submission":
                if len(parameters) != 4:
                    self.notifier.notify("""Error invalid parameters. Usage: create-submission <name> 
                                         <Deadline YYYY/MM/DD-HH:MM> <# issues> <Submission Link>""", email)
                else:
                    self.create_submission(parameters, email)
            elif keyword == "add-keywords":
                if len(parameters) != 2:
                    self.notifier.notify("""Error invalid parameters. Usage: add-keywords <name> 
                                        <comma-separated tags "Ex: tag1,tag2>""", email)
                else:
                    self.add_keyword(parameters, email)
            elif keyword == "start-grading":
                if len(parameters) != 1:
                    self.notifier.notify("Error invalid parameters. Usage: start-grading <name>", email)
                else:
                    self.start_grading(parameters, email)
            elif keyword == "show-rewards":
                self.show_rewards(email)
            else:
                self.notifier.notify(self.error_message, email)
        elif keyword == "show-rewards":
            self.show_rewards(email)
        else:
            self.notifier.notify("Error! Command not found. Available Commands:\n show-rewards", email)

    def show_rewards(self, email):
        if email == self.professor:
            students = self.db_connector.get_students()
            allstudents_reward = "Rewards for all Students: \n"
            for i in students:
                reward = self.db_connector.get_rewards(i)
                allstudents_reward += "Unity_ID=" + i + " \t OnTime= :+1: x" + str(
                    reward[0]) + " \t GoodJob= :clap: x" + str(
                    reward[1]) + "\t GoodQuestion= :metal: x" + str(reward[2]) + "\n"
            self.notifier.notify(allstudents_reward, email)
        else:
            reward = self.db_connector.get_rewards(email)
            if len(reward) > 0:
                self.notifier.notify(
                    "OnTime= :+1: x" + str(reward[0]) + "\t GoodJob= :clap: x" + str(
                        reward[1]) + "\t GoodQuestion= :metal: x" + str(reward[2]),
                    email)
            else:
                self.notifier.notify("You do not have any rewards", email)

    def create_submission(self, parameters, email):
        submissionName = parameters[0]
        """
        Make a DB call to get all submission Names and see if the submissionName already exists
        If name already exits, return back an error
        """
        if self.db_connector.get_submission(submissionName):
            self.notifier.notify("Name already exists. Please provide a new Name.", email)
            return

        try:
            datetime.datetime.strptime(parameters[1], "%Y/%m/%d-%H:%M")
        except ValueError:
            self.notifier.notify("Incorrect date format, should be YYYY/MM/DD-HH:MM.", email)
            return

        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        if parameters[1] < current_date:
            self.notifier.notify("Previous date given for submission", email)
            return

        if not parameters[2].isdigit():
            self.notifier.notify("Number of Issues not provided or invalid", email)
            return

        self.db_connector.add_submission(submissionName, parameters[1], parameters[2], parameters[3])
        self.notifier.notify("Submission Created.", email)

    def add_keyword(self, parameters, email):

        submissionName = parameters[0]

        if not self.db_connector.get_submission(submissionName):
            self.notifier.notify("Submission Name is not present.", email)
            return

        keywords = parameters[1]
        self.db_connector.add_keywords(submissionName, keywords.lower())
        self.notifier.notify("Keywords added.", email)

    def start_grading(self, parameters, email):
        submission_details = self.db_connector.get_submission_details(parameters[0])
        deadline = datetime.datetime.strptime(submission_details['Deadline'], "%Y-%m-%dT%H:%M:%SZ")
        if len(submission_details.keys()) == 0:
            self.notifier.notify("Submission name not found", email)
            return
        if datetime.datetime.now() < deadline:
            self.notifier.notify("Can't grade before deadline. Deadline for " + str(
                parameters[0]) + " is " + str(submission_details['Deadline']) + ".", email)
            return

        graded = submission_details["Is_Graded"]
        if not graded:
            self.calculate_rewards(parameters[0])
            self.notifier.notify("Grading Done.", email)
        else:
            self.notifier.notify("Submission already graded.", email)

    def calculate_rewards(self, submissionName):
        """
        Check validity if the name exists and if it has been previously graded and grading is not
        starting before the deadline. If in this case, return error to the Bot.
        Here get all the data of that submission, which is required for further steps
        :return:
        """
        submissionDict = self.db_connector.get_submission_details(submissionName)
        formLink = submissionDict['Sub_Link']
        userRepoDict = self.form_reader.fetch_sheet(formLink)

        onTimeRewardList = []
        goodJobRewardList = []
        for entry in userRepoDict.keys():
            commitDate = fetch_last_commit(userRepoDict[entry])
            if commitDate is None:
                continue
            deadline = datetime.datetime.strptime(submissionDict['Deadline'], "%Y-%m-%dT%H:%M:%SZ")
            if commitDate <= deadline:
                onTimeRewardList.extend(list(entry))

            num_of_issues = fetch_num_of_tasks(userRepoDict[entry], deadline)
            if num_of_issues >= submissionDict['Num_Issues']:
                goodJobRewardList.extend(list(entry))

        for user in onTimeRewardList:
            self.db_connector.update_reward_table(user, 'OnTime')
            self.notifier.notify("You received an On-Time Reward for " + submissionName, user)

        for user in goodJobRewardList:
            self.db_connector.update_reward_table(user, 'GoodJob')
            self.notifier.notify("You received a Good-Job Reward for creating tasks for " + submissionName, user)

        isGraded = True
        self.db_connector.update_submission_grading(submissionName, isGraded)
