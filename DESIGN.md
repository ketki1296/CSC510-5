# JarvisBot

## Problem Statement

Considering a class with a large strength (for example, CSC-510), it becomes difficult for the professor to keep track of students who follow good engineering practices, student participation in the class and ensure students are making the most of the platforms provided by the professor (Github, Mattermost, Slack). For every mistake made, student loses marks but for every good engineering practice and class enthusiasm shown, there are no rewards. Moreover, it is a tedious task for professors to keep track of students who do not submit their deliverables on time. With Jarvis Bot, it helps the professor reward students for following a Good Engineering practice and for being active in class with emojis (representation of rewards) which the professor can use at the end of the course to give out extra credits.

## Bot Description

JarvisBot aims to provide rewards to the students who have followed good Agile practices and good enthusiasm shown throughout the class. It does so by keeping a track of individual student progress for each of the tasks assigned in the class. The good Agile practice that this Bot focuses on is having well defined issues posted on Github for each of the tasks, bugs, or features. In an Agile team environment, it is also important to have a proper communication among the team members. This bot would give out rewards to students who are active in the class and ask relevant question on Stack Overflow and Mattermost platforms. The relevant questions are determined by using the keywords defined by the professor. The Bot will also keep track of student progress by checking if the student has submitted his assignments or projects before the deadline and rewarding them. The bot will provide rewards in the form of emojis to the students and based on these rewards the professor can decide to give extra credits to them at the end of the course.

The  bot is a simple program which would be integrated with different platforms in order to measure the performance of a student in class. We have decided on the following platforms with which it is going to interact with as these platforms are already used in the class for assignment submissions as well as discussions:
1. Mattermost
2. StackOverflow
3. Github

The bot would store the user profile in a MySQL database which would store the user and their rewards earned. The database would get updated whenever the user earn rewards and would return the current rewards information whenever the handle is invoked.

This is a good solution because it automates the tedious task of keeping track of all the activities of the student which the professor otherwise has to keep track in order to give out any extra credits.

JarvisBot belongs to the ‘Responders’ category of bots. It will respond to events and interactions as well. It will interact with the professor for taking input of deadlines for assignments, relevant keywords for the time period and the minimum number of issues that he expects for that assignment. It would send notifications to the professor so that it can start the grading for the assignments or tasks. Each student can interact with the bot to check their rewards that they have earned in the class. The bot will also respond to events such as when the student posts any question on Mattermost or Stack Overflow which is relevant to the time period.

#### Tagline
JarvisBot: *I'll be there for you!*

## Use-Case
```
Use Case: Reward a student when they submit deliverables before time.
1 Preconditions
Bot should have access to the professor's github access token for accessing repositories of students.
2 Main Flow
    Professor creates a homework/project milestone submission with details [S1]. Bot checks with the professor after the deadline if they want to start grading [S2]. Professor informs bot that they are ready to grade the submission [S3]. The bot looks at each submission to check if the last commit is before the deadline [S4]. Bot rewards each student who submitted on time [S5].
3 Subflows
  [S1] Professor creates a submission with the /create-submission command with submission deadline and student submission form (having github repositories) as parameters.
  [S2] Bot checks with the professor everyday after the deadline if they want to start grading.
  [S3] Professor informs bot when they are ready to grade the submission.
  [S4] Bot looks at all submissions and checks if the last commit is before the deadline.
  [S5] Bot rewards and notifies each student who submitted on time with a custom “on-time” emoji.
4 Alternative Flows
  [E1] Some/All of the students have not submitted the repository URL in the form.
  [E2] The Professor himself is not added as a Collaborator to the GitHub repository.
```
```
Use Case: Reward a student when they create github issues for homework/project tasks.
1 Preconditions
Bot should have access to the professor's github access token for accessing repositories of students.
2 Main Flow
    Professor creates a homework/project milestone submission with details [S1]. Bot accesses the student’s GitHub repositories after deadline and checks the number of valid issues created [S2]. Bot rewards the students with a “good-job” emoji who have minimum number of issues created in their GitHub repository [S3].
3 Subflows
  [S1] Professor creates a submission with the /create-submission command with submission deadline, minimum number of tasks and student submission form (having github repositories) as parameters.
  [S2] After the submission deadline, the bot accesses each student’s GitHub repository and checks the number of valid issues having a title, description  and at least one label.
  [S3] Bot rewards students having minimum number of valid issues with a custom “good-job” emoji and notifies them.
4 Alternative Flows
  [E1] Some/All of the students have not submitted the repository URL in the form.
  [E2] The Professor himself is not added as a Collaborator to the GitHub repository.
```
```
Use Case: Reward a student when the professor endorses their question
1 Preconditions
Bot should have access to the course’s stack overflow to access questions.
2 Main Flow
    Professor creates a homework/project milestone submission with details [S1]. Professor adds keywords to that submission [S2] Bot starts listening on the questions channel for this submission [S3]. Bot listens to the stack overflow bot for questions and accesses them [S4]. Bot determines a relevant question and rewards the student [S5].
3 Subflows
  [S1] Professor creates a submission with the /create-submission command with submission deadline and relevant keywords as parameters.
  [S2] Professor adds keywords to the submission with the /add-keywords command with the relevant keywords as parameters.
  [S3] Bot starts listening on the questions channel for questions (having a question mark) with these relevant keywords.
  [S4] Bot listens to the stack overflow bot for questions only and accesses them to see if they have relevant keywords.
  [S5] If a relevant question is found, Bot rewards students with a custom “good-question” emoji and notifies them.
4 Alternative Flows
  [E1] No questions are asked.
```
## Design Sketches
### Bot in action
- A wireframe mockup that shows how the bot rewards students who ask good questions.
![Question](Images/wireframe_question.png?raw=true "Question")

- A wireframe mockup that shows how the user can ask JarvisBot to show their earned rewards.
![Show Rewards](Images/wireframe_reward.png?raw=true "Show Rewards")

### Storyboard
There are two end users who can interact with JarvisBot:

- **Professor**
![Professor](Images/storyboard_professor.png?raw=true "Professor")

- **Student**
![Student](Images/storyboard_user.png?raw=true "Student")

## Architecture Design

The architectural pattern of JarvisBot can be defined as a hybrid of the repository and event triggered patterns. It is a repository model because the rewards of each student are stored in a database. But since it also gives notifications when users earn rewards and user indirectly earns rewards for asking a relevant question - it is also event triggered, the event being asking a question.

![JarvisBot Architecture](Images/Architecture.png?raw=true "JarvisBot Architecture")

#### Components:

- **Listener:** The listener component receives all communication happening on MatterMost. It filters out requests and classifies them into one of two types: Event or Question. For events, the message must have the mention of bot (@jarvisbot) and for questions, the message must be posted in the questions channel and the Question Handler is enabled.

- **Event Handler:** The event handler component is responsible for identifying valid commands (start-submission, add-keywords, rewards and start-grading) and taking necessary actions. This component communicates with external entities (GitHub and Google Forms) and the database using their respective connector components. This component is also responsible for enabling the question handler when the add-keywords command is triggered on a submission. It decides if a student has earned rewards and triggers the notifier component to send out notifications. Whenever a submission is created, the timer component is triggered with the deadline.

- **Timer Component:** This component triggers event handler component when a deadline is reached to determine if each student has created enough tasks. This component also sends out a notification to the professor to start grading after the deadline for submission has passed on a daily basis. It communicates with the Notifier component directly to send out reminder notifications.

- **Question Handler:** This component is used to parse questions and look for keywords supplied by the Event Handler component and determine if the student has earned reward for asking a good question. If the question contains any of the keywords, it is treated as a good question. This component communicates with the Stack Overflow connector component to fetch a question posted on stack overflow. StackBot posts questions in the #questions channel when a question is posted on Stack Overflow.

- **Notifier:** This component is used to send out notifications to MatterMost. It just needs the message and the user details where this message needs to be sent.

- **Connector Components:** These components are responsible for fetching data from different sources or updating data in the database. It fetches data from GitHub, Google Forms and Database and make updates for submissions and rewards in the database.

- **MySQL Database:** It stores information related to submissions (name, deadline and form link) and rewards (how many rewards emojis each user has earned). It responds to requests from the db-connector component.


#### Constraints:
- This bot cannot be accessed on the MatterMost channels and is restricted to post anything on the channels. However, it can read from the questions channel. The reasoning behind this is that the bot should not post any rewards information to a larger audience.
- A User cannot check rewards of any other student. Only a professor can see the rewards of all students using the “rewards” command. A user will see only their rewards when they use the same command.
- A User cannot use any other commands apart from the “rewards” command. However, the professor can use all the commands while interacting with the bot.
- This bot depends on GitHub, Stack Overflow And Google Forms APIs and any changes to this APIs may break the functionality of this bot. Bot will need read-only access tokens to this platforms.

### Additional Design Patterns:
- Object-oriented: This bot will be designed using this pattern based on Call-and-Return patterns. The Event Handler class will act as a primary controller for this bot and interfaces with the other components to accomplish tasks as described in the architecture above.

- Implicit and Explicit Invocation: This bot will be designed to support both implicit and explicit invocations. Implicit invocation occurs when the Question Handler rewards a student for posting a good question and the user has not explicitly interacted with the bot. Explicit invocation is possible where the professor/student can directly interact with the bot.

Specifically, we intend to design the architecture using the following design patterns:
- Singleton: The connectors for 3rd party services e.g, stack overflow, google forms, github are clases for which there is only one single instance.
- Observer: After the Event Handler has computed the rewards, the rewards of users have changed. Now, it has a task to notify the database of the change in order to update it there. It also as to notify the user about their updated rewards.
- State: When there are keywords posted for a submssion made by the professor, the Question Handler is getting invoked and change its state form passive to active. Also, the timer for that assignment would go to active state after the deadline which would in turn trigger a set of actions e.g, disable the Question Handler, Ask the professor if they want to start grading leading to re-computation of rewards.
