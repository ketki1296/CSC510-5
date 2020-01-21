## Story Creation and Assignment
Sprint 1:
Screenshot of Kanban Board:
![Stories - Sprint 1](Images/Stories-sprint1.png?raw=true "Stories - Sprint 1")

Sprint 2:
Screenshot of Kanban Board:
![Stories - Sprint 2](Images/Stories-sprint2.png?raw=true "Stories - Sprint 2")


## Process Notes (Practices followed by the team)
#### Sprint planning phase 
This included identification and planning of tasks that can be finished by the end of this sprint. This is followed by assignment of stories to a team member based on their expertise and available bandwidth.
We followed the following methodology for sprint planning:
* Review the current status of the project to identify pending tasks.
* Story Creation
  * All members of the team identified pending tasks and created stories for them.
  * All the work involved was identified for each story by the member.
  * Initial points were assigned by each member.
  * Each point was valued at roughly 2 hours of work for one person.
* Grooming
  * After all the stories were created, each story was reviewed for amount of effort.
    * Each member identified points based on the effort (as described by the story creator.)
    * The story was then assigned points based on agreement from each member. Disparity was then resolved by more discussion.
* Assignment of Stories
  * Each story was then assigned to a team member based on two factors:
    * Expertise: Member is familiar with the domain for that story.
    * Bandwidth: Member has enough bandwidth to finish the task.

This methodology was used for sprint planning in both the sprints.


#### Mid Sprint Review
The idea behind having this meeting is to review the story completion progress and provide an opportunity for team members to raise any obstacles for issues they face during the sprint. 

During the sprint, a team can raise two flags when they are stuck and require help/intervention of other team members. A Red Flag is raised when there is a serious concern that is completely halting the execution of a User Story. For example, a red flag can be raised when a story faces an unseen dependency that arises. 

A Yellow Flag is raised when a team member is facing a  problem and hasn’t been able to resolve it for more than 30 minutes. This is an indication that other team members can interfere and help fix this issue.

The requirement for this meeting to occur is for a Red flag to be raised before the middle of the sprint.


#### Sprint Retrospective
The idea is to reflect on the process for the sprint by gathering feedback from each member as to how the process can be improved. This meeting occurs at the end of the sprint. The template we followed for retrospective meeting was as follows:
* What went well - continue doing: Determine the practices and things that went well and we should continue doing to improve collaboration among the team.
* What did not go well - stop doing: Identify what practices should be avoided for better collaboration.
* What should we start doing: Discuss ideas about what the team can start doing to improve the efficiency as a team.
 

### Core and Corollary Practices
One core practices that the team wasn’t following before this process was Reflecting on the process to determine what is working and what is not. So as a core practice, the team started following Sprint Retrospective as part of this process. More details on the retrospective process is described in the above section. End of Sprint section has the outcome for each of the iterations.

We followed a couple of Corollary practices as deemed necessary by the team:
* Raising flags (red and yellow) based on the severity of issue faced. This is described in the “Mid Sprint review” sub-section of “Process Notes” section.
* Scheduling the JarvisBot server to be shared by multiple team members: Since the team has a single setup for testing the changes, it was necessary to come up with a mechanism to avoid conflicts of usage.
  * Each team member was allocated a time frame for each day. For instance, Kushal was assigned 11PM to 2AM
  * Members can only use the server during this time.
  * If the team member needs to access the server during any other time, they need to make sure that they get acknowledgement from the member who is allocated that time frame.
  
## End of Sprint Reflection
### End of Sprint-1
We were able to complete 11/12 tasks at the end of Sprint 1. The team discussed and agreed to carry forward the story ‘selenium test_case use_case2’ to the next sprint because of an  unforeseen dependency related to mocking data removal. The story was tightly coupled with the mocking data which was removed as part of one of the stories leading to complete failure of this test-case scenario. To fix this, it was necessary to completely revamp the selenium test-cases to work with real data. 

A new story was created for this task but as none  of the team members had the bandwidth to work on it at the time, it was scheduled for sprint 2 and the existing story was carry-forwarded.

#### Reflection - 1
| What Went Well (Continue Doing) | What Did Not Go Well (Discontinue) | What should we start doing |
|---------------------------------|------------------------------------|----------------------------|
| Well-defined tasks which led to completion of all but one tasks for sprint one. | We didn’t identify dependencies for all the tasks which led to the carry-on for next sprint | Clearly define dependencies for all tasks to avoid being stuck on any task |
| Good Collaboration and communication among team members | | |



### End of Sprint-2
We completed all the tasks for the sprint with an exception of code-coverage tasks which the team realised and decided was not required for this milestone. For this we created another label as ‘Discontinued’ on story-board and moved all the code coverage tasks to this label. 

At the end of the sprint, we were able to complete all the use-cases with 100% functionality and cover all the edge-cases for them.

#### Reflection - 2

| What Went Well (Continue Doing) | What Did Not Go Well (Discontinue) | What should we start doing |
|------------------------|--------------------------|---------------------|
| We were able to cover all the tasks &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| We didn’t properly think of edge cases before but during the integration we realised these cases and incorporated them all during testing. This hindered the completion of a couple of stories depended on mocking removal | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|







### Meeting Notes

##### Sprint 1
##### Sprint Planning Meeting
##### Date: Oct 24,2019
##### Attendees: Ketaki, Bhavya, Jay, Kushal

* Meeting Notes:
  * Reviewed the work done so far and identified the pending items.
  * Streamlined them by breaking them into smaller parts for division into stories.
  * Created stories for each of the identified pending tasks.
  * Identified any dependencies for each story.
  * Groomed these stories - assigned points for each story based on the effort required and any dependencies.
  * Assigned these tasks to each member based on expertise and availability.
  * Raise red flag (Post a message on mattermost project channel) when faced with a blocking issue.
  * Decided to raise a yellow flag when stuck with a problem for more than 30 minutes.
* Goals:
  * Finish all the assigned stories by Sprint end, i.e., Nov 1, 2019.
* Next Meeting: Oct 29, 2019 for Mid Sprint Review (May be cancelled if no blocking issues found)

##### Mid-Sprint Meeting
##### Date: 29th October, 2019
##### Attendees: Ketaki, Bhavya, Jay, Kushal

* Meeting Notes:
  * This meeting was called because of the Red Flag raised by Bhavya for the story Selenium Testing for Use-Case 2.
  * The above story was reviewed and accordingly decided to be blocked because the members were busy with other commitments.
* Next Meeting: November 1, 2019 for a final meeting before Sprint-1 deadline and for Retrospection.

##### ‘Sprint Retrospective and Planning’ Meeting:
##### Date: 1st November, 2019
##### Attendees: Ketaki, Bhavya, Jay, Kushal

* What Went Well (Continue Doing): Well-defined tasks which led to completion of all but one tasks for sprint one
* What Did Not Go Well (Discontinue): We didn’t identify dependencies for all the tasks which led to the carry-on for next sprint
* What should we start doing: Clearly define dependencies for all tasks to avoid being stuck on any task. Remove mocking to test the data from APIs instead.

* Meeting Notes:
  * Reviewed the tasks, revisited the code and analyzed the progress - completed and incomplete tasks.
  * One incomplete story identified due to a dependency based on tight coupling of Selenium tests with Mocking. Carry-forward this story and move to complete on this board.
  * Created new stories based on the methodology apart from the existing carry-forwarded story.
  * Analyzed dependencies of all the created stories (discussed as part of retrospective):
  * Reviewed any dependencies for each story and also any other blocking issues that we might face.
  * Analyzed the dependencies and unknowns, if any.
  * Prioritized tasks and stories. And placed them in the order in which they need to be completed.
* Next Meeting: November 3, 2019 for discussion about the next sprint and pending tasks. 

##### Sprint 2
##### Sprint Planning Meeting
##### Date: 3rd November, 2019
##### Attendees: Ketaki, Bhavya, Jay, Kushal

* Meeting Notes:
  * Reviewed the work done so far and identified the pending items(especially the one that went through a Carry-Forward). 
  * The requirements of the Sprint were assessed.
  * Accordingly, Stories were created for the following Sprint.
  * Groomed these stories - assigned points for each story based on the effort required and any dependencies.
  * Assigned these tasks to each member based on expertise and availability.
  * Raise red flag (Post a message on mattermost project channel) when faced with a blocking issue.
  * Decided to raise a yellow flag when stuck with a problem for more than 30 minutes.
 * Next Meeting: November 5, 2019 for a middle Sprint Meeting to update on project plans and assess the situation.

##### Mid-Sprint Planning:
##### Date: 5th November, 2019
##### Attendees: Ketaki, Bhavya, Jay, Kushal

* Meeting Notes:
  * Few of the stories were thought over and needed more work than was expected.
  * Since in the middle of sprint, the project plans and priorities of tasks changed so story for code coverage was planned to be removed.
* Next Meeting: November 7, 2019 for a Demo Preparation Meeting.
  
##### Demo Preparation Meeting and Sprint Retrospective
##### Date: 7th November
##### Attendees: Ketaki, Bhavya, Jay, Kushal

* Agenda:
  * Meet to prepare for the TA demo

* Meeting Notes:
  * Create new GIT Repo and New Google Form with entries for the demo.
  * Ensured all the use cases are working fine without anything of Mocking and Selenium.

* What Went Well (Continue Doing): We were able to cover all the tasks 
* What Did Not Go Well (Discontinue): We didn’t properly think of edge cases before but during the integration we realised these cases and incorporated them all during testing. This hindered the completion of a couple of stories depended on mocking removal.

 


