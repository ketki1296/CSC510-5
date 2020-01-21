## Steps to setup JarvisBot on a Ubuntu server:
These are the steps that the professor should follow to get JarvisBot up and running.
1. Install Mattermost: 
   * Install Mysql Server/ PostgreSQL database server
   * Install Mattermost Server

More details about these steps can be found here: https://docs.mattermost.com/install/install-ubuntu-1804.html

2. Create tables in database
   * Create a database named: “RewardBot”
   * Create tables using the sql file: schema.sql using the command: 
__mysql -u <DB USERNAME> -p <PASSWORD> < schema.sql__
3. Create jarvisbot in Mattermost server. Note the token generated for this bot.
4. Generate a github personal access token and make a note of it.
5. Forms: To access Google Sheet, enable the Google Drive API and Google Sheets API. The “Email ID” generated according to the credentials entered, share all the future google sheets with the “Email ID”.  
Follow this link for more info on how to enable APIs: https://console.developers.google.com/apis/
6. Set the environment variables for the secrets and usernames.
   * export GITHUBTOKEN="\<token from step 4\>"; export PROFESSOR="\<Your email id\>";
   * export DB_HOST="localhost"; export DB_NAME="RewardBot"; export DB_USER="\<DB USER\>"; export DB_PWD="\<DB PASSWORD\>";
   * For selenium testing only: export PROFESSOR_PWD="\<Your password\>"; export TESTUSER="\<EMAIL\>"; export TESTUSER_PWD="\<PASSWORD\>"; export TESTUSER2="\<EMAIL\>"; export TESTUSER2_PWD="\<PASSWORD\>";
     * Make sure you create two test users in mattermost and use their credentials in the above step.
7. Clone this repository and run the listener.py (Python3) using the command: 
__python3 listener.py__
