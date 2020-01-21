# JarvisBot

## Problem Statement

Considering a class with a large strength (for example, CSC-510), it becomes difficult for the professor to keep track of students who follow good engineering practices, student participation in the class and ensure students are making the most of the platforms provided by the professor (Github, Mattermost). For every mistake made, student loses marks but for every good engineering practice and class enthusiasm shown, there are no rewards. Moreover, it is a tedious task for professors to keep track of students who do not submit their deliverables on time. This bot will help the professor in keeping track of each student's activities like on-time submissions, following good practices and asking relevant questions. Each time a student follows these activities, they are rewarded with an emoji. This will encourage the students to follow good practices and may increase positive discussion as the number of rewards earned summarizes the student's performance and participation in the course. The professor can announce the top students in the class. Additionally, while grading, the professor can simply look up the rewards earned by a student to determine if they have earned some extra credit.

## Features
All interactions with the bot are restricted to direct message channel. Bot does not respond to messages on channels. Some of the key features of this bot are:
- **Rewards for submitting on-time**: Reward a student (On-Time emoji) when they submit a deliverable (Ex: Homework or Project milestone) before the deadline.
  - Professor creates a submission (Ex: Homework #1 or Design Milestone) with **deadline**, minimum number of github issues and a **google docs link** for submissions. This Google Docs link has each students submission (i.e., their github repository URL). This is usually the responses sheet from the Google Form used for collecting student responses. Command: create-submission.
  - Students make their submissions before the deadline and make no commits after deadline.
  - When the professor and TAs are ready to grade the submission (typically a few days after submission deadline), the professor asks jarvisbot to grade for reward calculations. Command: start-grading.
  - The bot checks each students' submission and compares the last commit time against the deadline. If last commit was before deadline, the student is rewarded with an On-Time emoji and notified via direct message channel.
- **Rewards for creating minimum number of github issues**: Reward a student (Good-Job emoji) when they create minimum number of issues (set by professor) in github for a particular submission.
  - Professor creates a submission (Ex: Homework #1 or Design Milestone) with deadline, **minimum number of github issues** and a **google docs link** for submissions. Command: create-submission
  - Students create minimum of issues in their github repositories before the submission deadline.
  - When the professor and TAs are ready to grade the submission (typically a few days after submission deadline), the professor asks jarvisbot to grade for reward calculations. Command: start-grading.
  - The bot checks each students' submission for number of issues created before deadline. If it is more than the minimum defined, then they are rewarded with an Good-Job emoji and notified via direct message channel.
- **Rewards for asking relevant questions**: Reward a student (Good-Question) for asking a question relevant to the submission.
  - Professor creates a submission. Command: create-submission
  - Professor adds keywords for that submission. Command: add-keywords
  - Students start working on their submissions and post questions on #questions channel. If this question is relevant (i.e., contains keywords defined by the professor), the student are rewarded with an Good-Question reward and notified via direct message channel.
  - Bot ignores and filters anything other than questions.
- **Professor can see rewards of all students**:
  - Professor can see all rewards earned by each student. Command: show-rewards.
- **Students can see only their earned rewards**:
  - Students can see their earned rewards. Command: show-rewards.
  - Students cannot see rewards of other students. Only professor can see everyone's rewards.
  
### Screenshots:
- Professor:
![Professor](Images/Report-1.JPG?raw=true "Professor")

- Student (Question):
![Student 1](Images/Report-2.JPG?raw=true "Student 1")

- Student (Rewards):
![Student 2](Images/Report-3.JPG?raw=true "Student 2")

## Reflection on development process and project:
When we look back to the time we started working on this project, we realize how much we've learnt about building a software. We realized that while having programming skills is important, it is not enough. To work in a team and achieve efficient collaboration, this project helped us understand the value of each software practice - when it works best and what can go wrong.

During our development process, we made a few mistakes in design and realized those during development. For our scenario, we tried to work with the initial design (with a small flaw) for a long time before we decided to change the design (required rework of a major portion of our code). This design decision was to enable the bot to automatically trigger itself after each submission's deadline and start rewarding students immediately. This requires no intervention from professor, which was our initial aim: to automate as much as possible. However, this design made testing (both manual and selenium) a tedious task and made it very difficult to showcase or demonstrate the features as we could no longer control when it would trigger. Another problem with this was a conceptual mistake. When a porfessor assigns a deadline, that does not mean they would always want to start grading immediately. Consider a situation where the preofessor wants to check if there were late submissions and we are working with GitHub repositories. If the bot does not wait for a buffer time before grading, it would never find out about late submissions. After realizing this, we were quick to come with a simple and effective design - wait for professor's input to start grading.

Overall, we feel that the project we set out to work on meets it's requirements and has a robust design. The complete project has been a brilliant experience, allowing us to understand software design, development, testing, automation, agile practices, continuous integration and configuration management. It gives us a strong sense of achievement after being able to do all these as part of our project.

## Limitations and Futute Work:
- The questions rewarded by this bot can be improved with integration with stackbot. Questions asked on stack overlflow can directly be given to this bot and the student can be rewarded. Currently there is no support for questions asked on Stack Overflow.
- Improvements in detecting questions in the questions channel. Rhetorical questions need to be identified. Possible integration with other bots.
- Improvements in identification of relevant issues created on github to help ignore dummy issues. Defining a set of keywords to be found in the issues could be a possible solution.

## Project Presentation

[Screencast link](https://drive.google.com/open?id=1v8DH2mteDMFtxh2MOGqFUR7WTZglz7_r)
