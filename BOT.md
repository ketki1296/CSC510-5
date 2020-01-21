# Jarvis Bot:

Environment of implementation:

Python3

#### Infrastructure Setup:

We have installed mattermost on a GCP Linux machine and then we created a bot with the role ‘User’. The bot has a Bot Token which we use for authentication during call for listener and notifier components in our design. We then use the “mattermostdriver” module in python to communicate with Mattermost server using the token. 

### Bot Platform:

This bot is fully functional and integrated with mattermost. It responds to all the defined commands:
create-submission, add-keywords, start-grading and show-rewards

### Bot Integration:

All the use-cases have been implemented as defined in the use-cases. As a mattermost user, you can have a complete conversation with jarvis. For professor, it has conversations about creating submissions, adding keywords and starting the grading process. It also shows rewards for professor and students. Professor can see all the students rewards and students can see only their rewards.

#### Files:
* Db.connector.py: 
This file consists of functions used for read, write and update operations in database
* Event_handler.py: 
This file consists of events which happen whenever a student or the professor sends a direct message to the JarvisBot.
* Form_reader.py: 
This file is used to get the data from the Google Sheet submitted by the professor for Homework submissions and Project submissions.
* Git_connector.py: 
This file consists of functions for getting the data required for calculating rewards from Github using GIT APIs. 
* Listener.py: 
This file consists of a function to listen for any user activity taking place on 
* Mocker.py: 
This file is used to Mock our external services like github and reading from a google form.
* Notifier.py: 
This file is used by the bot to send messages to a direct message channel.
* queryDB.py: 
This module sends out notifications of reminder to start grading submissions after their deadlines (once a day). It also checks the number of issues in a students submission repo after deadline and rewards them if they have the minimum number of issues created.
* Question_handler.py: 
It consists of a function to identify if the question asked is a GoodQuestion for which we need to assign rewards to the user.

##### Modules used: 
We have defined the requirements.txt file which helps us install all the libraries that are needed to run the Bot

##### Environment Variables:
We also need to set few environment variables so that our Bot has all the permissions to post and fetch any data that is required.

* PROFESSOR: It is the email Id of professor that is required
* GITHUBTOKEN: It is the Github personal access token with permission of ‘Repo’
* BOTTOKEN: Mattermost token for bot


### Use Case Refinement:

For Use Case 1 and 2, we have a constraint where the professor needs to share the student’s homework submission forms with an email id to be used by the bot to access the Google form. However, we have mocked the data from Google forms for this submission.

For Use Case 3, we have streamlined the use-case to listen on questions directly on the channel only. This means that jarvis cannot read a question posted on stack overflow. This decision was taken as to avoid integration with Stack Overflow APIs because they have already been implemented by the stackbot.


### Mocking Infrastructure

We have used the framework “Mockito” in python to enable mocking for jarvis bot.
##### File: *Mocker.py*
##### Methods: *start_mocking_git, start_mocking_forms and stop_mocking.*

In this setup, Mocking has been used in three scenarios:

* API calls to a defined github repo for getting time of last commit has been mocked to respond with a pre-filled response object.
* API calls to a defined github repo for getting the number of issues has been mocked with a pre-determined response.
* API calls to get data from a google forms url has been mocked to return a dictionary of users as keys and their corresponding github repositories as values.

For use-case 1 and 2, we need to access the google forms to retrieve the students’ submissions and then for each of those submissions, we need to access github to determine the student’s ability to earn the reward. These calls have been mocked.

Note that these mocker functions are started just before the github and google form URL calls 

### Selenium Testing Infrastructure 

We have written selenium test cases in python to test all the use cases for a positive flow and an alternative flow. 
#### Use Case 1:
##### Positive flow: 
1) We first go to the server link where our Mattermost server is running and log in using professor’s email ID.
2) Professor creates a new submission in the Jarvisbot channel using `create-submission` keyword
3) Next we log out of professor’s account and log in using a test student’s account. We first check the rewards the student currently has from the Jarvisbot channel. After this we log out of test student’s account.
4) We again log in using professor’s account and ask Jarvisbot to start grading the homework that was just created
5) When log in using test student’s account we see that the student has got an reward for being On-Time.

##### Alternative Flow:
1) Here we first go the server link where our Mattermost server is running and log in using professor’s email Id
2) Professor tries to create a new submission but does not enter the required number of parameters
3) We get an error message from Jarvisbot which shows the parameters that are required

#### Use Case2
##### Positive flow:
1) Here we first log in to mattermost server using professors email Id and create a new submission with a deadline
2) Student submits his homework with the required number of git issues created
3) Student logs in to his account and after the deadline checks if he has received a reward ‘Good-Job’ in the Jarvis bot channel
	
##### Alternative flow:
1) Here we first log in to mattermost server using professors email Id and create a new submission with a deadline
2) Student does not submit his repository link
3) When the deadline gets over, the student does not get a reward for ‘Good-Job’. As a result, when he logs into his account and checks with Jarvisbot, he doesn’t get any notification of a Reward
#### Use Case 3
##### Positive flow:
1) Here we first log in to mattermost server using professors email Id and create a new submission with a deadline
2) He tells Jarvisbot to add all the keywords which are relevant to the submission using `add-keywords`
3) Then when a test student asks a valid question which contains atleast one of the keyword, Jarvisbot gives that student a reward for asking ‘Good-Question’

##### Alternative flow:
1) Here we first log in to mattermost server using professors email Id and create a new submission with a deadline
2) He tells Jarvisbot to add all the keywords which are relevant to the submission using `add-keywords`
3)A test Student asks some question in the questions channel which does not include any relevant keywords. Jarvisbot does not reward that student for asking that question

The Mocking and Selenium testing have been demonstrated in the screencast.

### Screencast

[Screencast Link](https://drive.google.com/drive/folders/1WHgBSHN6xnKg0ziFnx9ONl0KrCFtsrjP?usp=sharing)
