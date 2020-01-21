# JarvisBot

## Deployment Scripts

We used Ansible as a configuration management tool for our bot deployment. The scripts can be found under the ansible_scripts folder.
We can define the remote host on which we need to deploy the bot in the inventory file.<br>

The main steps in our playbook include installing mysql and mattermost, configuring mattermost service to run on the server, creating a team, register the bot with professor's account, create a questions channel in which students can ask questions, and deploy the backend code for our BOT.<br>

We have also provided vars.yml file which contains  all the variables that need to be defined to run the playbook.<br>

The parameters are as follows:

**Variables used  in vars.yml**: <br>
mattermost_user_api_url:  http://<mattermost_server_ip>:8065/api/v4/users/login <br>
mattermost_bots_api_url: http://<mattermost_server_ip>:8065/api/v4/bots <br>
mattermost_getteam_api_url: http://<mattermost_server_ip>:8065/api/v4/teams <br>
mattermost_channel_api_url: http://<mattermost_server_ip>:8065/api/v4/channels <br>
SiteURL: http://<mattermost_server_ip> <br>
url: http://<mattermost_server_ip>:8065 <br>
team_name: name of Team to be created <br> 
db_user: mattermost database user name <br>
professor: email address of professor <br>
professor_pwd: password for professor's account <br>
botname: name of the bot to be created <br>
firstname: first name of the admin user <br>
username: username of admin <br>
githubuser: githubuser name <br>
githubpassword: github user password <br>


Main.yml is the file which we use to run our ansible-playbooks. The order of deployment of our Ansible script is

#### 1) sqlinstall.yml:


We first install mysql on the remote host along with the different packages that are required to run mysql. We also create a db user and provide him with the required permissions for the database

#### 2) mminstall.yml


This playbook downloads the latest version of mattermost and installs it on the remote host

#### 3) jsonchange.yml


This playbook basically allows to modify the configuration files that are required for starting mattermost and registers mattermost to run as a service.


#### 4) configmm.yml


It registers a team named 'csc5105' and adds the professor as a admin of the team.


#### 5) create_bot.yml


This plabook has the tasks to create and register a bot on mattermost server that we just installed. For this we get the token of the professor and use it to register our bot


#### 6) create_channel.yml


This playbook is used to install the questions channel that is required for our bot. The bot listens to the questions that are asked in the questions channel


#### 7) loaddb.yml


This playbook adds a database named RewardBot in mysql database to be used by the bot. We use the schema file jarvis.sql present in the directory.


#### 8) appdeploy.yml


We clone the repository containing our bot code and install all the packages that are required to run the bot.



To run the playbook, run the command ansible-playbook -i inventory main.yml



## Acceptance Tests
To run acceptance tests, you will need two user accounts: professor and student.
We have created a github repository and google doc to be used for testing.
### Testing Details
- Mattermost Server: http://34.66.232.72:8065/
- Team Name: CSC-510-F19
- Login Credentials:
  - Professor Account:
    - Username: professor
    - Password: Jarvisbot@2019
  - Student Account:
    - Username: student
    - Password: Jarvisbot@2019
- Google doc link: https://docs.google.com/spreadsheets/d/1YzP8PrQ_wncYIRF5d45BlmCIe_-1oIKQpdNDjFiZNhI/edit#gid=0
- Github Repository: https://github.ncsu.edu/mkushal/demo-test

The google document is already populated with an entry from student account to the github repository. You can view that in the google document.

NOTE: please note that if you are running this demo multiple times, use different names for submissions. We will use the names finaldemo1, finaldemo2 and finaldemo3 for the first time.
### Testing scenarios:
- Scenario: Student should be able to check their rewards
  - Login as student and open the direct message channel for jarvisbot.
  - Command: **show-rewards**
  - Expected response: counts for three types of rewards: OnTime, GoodJob and GoodQuestion. It should not show rewards for other students.

- Scenario: Professor should be able to check all students' rewards
  - Login as professor and open the direct message channel for jarvisbot.
  - Command: **show-rewards**
  - Expected response: For each student, counts for three types of rewards: OnTime, GoodJob and GoodQuestion. It should show rewards for all students.

- Scenario: Student should be rewarded for asking a relevant question (Use-case 1).
  - Prerequisite:
    - Required Parameters: Name, date, minimum number of github issues, submission google doc and keywords (comma separated).
    - Date is in format: YYYY/MM/DD-HH:MM (Any other format will not be accepted).
  - Login as professor and open direct message channel for jarvisbot.
  - We will set the deadline for the submission as a future time. Replace the <date> in the below command with the current time + 15 mins in 24 hout format (YYYY/MM/DD-HH:MM). For example, if the current date and time is December 10, 2019 04:28PM, add 15 minutes to this. Result will be 2019/12/10-16:43 for this example.
  - Create a submission using the command: **create-submission finaldemo2 <date> 2 https://docs.google.com/spreadsheets/d/1YzP8PrQ_wncYIRF5d45BlmCIe_-1oIKQpdNDjFiZNhI/edit#gid=0**
  - Expected response: **Submission Created.**
  - After getting the above response, add the keywords for this submission using the command: **add-keywords finaldemo2 ansible,jenkins**
  - Expected response: **Keywords added.**
  - Logout and login as student. Note that you will have to do this before the deadline (i.e., within 15 mins of submission creation).
  - As a student, open the #questions channel and post the below question or any question containing ansible and jenkins words.
  - Question: Does ansible support nested playbooks?
  - Expected response: You should receive a direct message from jarvisbot saying **You received a Good Question Reward for posting a relevant question**
  - Check the current rewards for this student using the command: **show-rewards**
  - Expected response: You should see an increase in the number of GoodQuestion rewards for this student.
  
- Scenario: Student should be rewarded for making on-time submission and creating minimum number of github issues (Use-case 2 and 3).
  - Prerequisite:
    - Required Parameters: Name, date, minimum number of github issues, submission google doc and keywords (comma separated).
    - Date is in format: YYYY/MM/DD-HH:MM (Any other format will not be accepted).
    - Google doc already has an entry for student with the github repository. THe last commit in this directory is quite old and your submission deadline will be greater than the last commit time.
    - The github repository already has 2 issues created. We will create a submission with 2 as minimum number of issues so that the student receives a reward.
  - Login as professor and open direct message channel for jarvisbot.
  - We will set the deadline for the submission as 1 minute in future. Replace the <date> in the below command with the current time + 1 min in 24 hout format (YYYY/MM/DD-HH:MM). For example, if the current date and time is December 10, 2019 04:28PM, add 1 minute to this. Result will be 2019/12/10-16:29 for this example.
  - Create a submission using the command: **create-submission finaldemo3 <date> 2 https://docs.google.com/spreadsheets/d/1YzP8PrQ_wncYIRF5d45BlmCIe_-1oIKQpdNDjFiZNhI/edit#gid=0**
  - Expected response: **Submission Created.**
  - Wait for 1 minute till the deadline expires. Running the next command before the deadline will not be accepted by the bot (you can try!).
  - Now, in the same window, start assigning rewards to students for this submission by using the command below.
  - Command: **start-grading finaldemo3**
  - Expected response: **Grading Done.**
  - Logout and login as student.
  - As a student, open the direct message channel. You should see two new messages from jarvisbot saying:
    - **You received an On-Time Reward for finaldemo3**
    - **You received a Good-Job Reward for creating tasks for finaldemo3**
  - Both these awards are received because the student's submission has on-time commits and minimum number of github issues.
  - Check the current rewards for this student using the command: **show-rewards**
  - Expected response: You should see an increase in the number of OnTime and GoodJob rewards for this student.
  
## Final Code
**Directory Structure**:
- **jarvisBot**: Contains all the development code for jarvisbot.
- **test/selenium**: Contains all selenium test.
- **ansible_scripts**: Contains all the deployment scripts.

We have created a couple of files which are triggered after the bot is started from the python script **listener.py**
- **jarvisBot/src/listener.py**: Listens to incoming messages from the mattermost server by creating a websocket. Triggers event_handler.py for any direct messages and question_handler for messages on #questions channel.
- **jarvisBot/src/event_handler.py**: Handles all commands and sends responses back to mattermost server. OnTime and GoodJob rewards are calculated here.
- **jarvisBot/src/question_handler.py**: Parses questions on valid keywords to find a match. GoodQuestion rewards are calculated here.
- **jarvisBot/src/notifier.py**: Used by event_handler to send out messages on direct message channels.
- **jarvisBot/src/db_connector.py**: Utility to fetch data from database in required format.
- **jarvisBot/src/git_connector.py**: Utility to calll git APIs and fetch data from repositories.
- **jarvisBot/src/form_reader.py**: Utility to call google doc APIs and fetch data from the document in a standardized format.
- **jarvisBot/src/queryDB.py**: Independent utility to notify professor about ungraded submissions after deadline. Runs on a daily basis and is self-triggered.

## Continuous Integration Service

For the CI service, we created a server and installed jenkins and a local copy of mattermost. The aim is to trigger a build on each commit made to the code and test the code by running the integration tests.
We have used post-commit git hooks in order to trigger the jenkins job on the server. Since we are just changing the backend code of our bot, the jenkins job is configured to copy the changed code and deploy it in its workspace. The job contains three steps 
1) It will install all the dependencies 
2) Start running the bot listener 
3) Execute selenium tests

Here we have used nosetests tool in order to run the selenium tests. It picks up all the files from the tests folder which have prefix "test_" in their function name. After executing all the tests, it gives us a report which shows if we have passed all the tests and our build is successfull.





[Screencast Folder](https://drive.google.com/open?id=1LW3ew_uPxx6Ip9BDZ1nHXYLXVoNc1yeU)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
