import mysql.connector
import os
import configparser

config=configparser.ConfigParser()
config.read('config.ini')
class dbConnector:

    def __init__(self):
        self.connect = self.get_connection()

    def get_connection(self):
        return mysql.connector.connect(host=config.get('myvars','DB_HOST'), database=config.get('myvars','DB_NAME'), user=config.get('myvars','DB_USER'),
                                               password=config.get('myvars','DB_PWD'), buffered = True)

    def get_submission(self, submission_name):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()

        cur = connect.cursor()
        cur.execute("Select Name from Submission where Name=%s;", (submission_name,))
        if cur.rowcount >= 1:
            cur.close()
            connect.close()
            return True
        else:
            cur.close()
            connect.close()
            return False


    def add_submission(self, name, date, issues, form):
        
        connect = self.get_connection()
        if not self.connect.is_connected():
            self.connect = self.get_connection()

        cur = connect.cursor()
        cur.execute("Insert into Submission (Name, Deadline, Sub_Link, Num_Issues) values (%s, %s, %s, %s)",
                    (name, date, form, issues))
        connect.commit()
        cur.close()
        connect.close()

    def add_keywords(self, name, keywords):
        connect = self.get_connection()
        if not self.connect.is_connected():
            self.connect = self.get_connection()

        cur = connect.cursor()
        cur.execute("Update Submission set Keywords = %s where Name = %s", (keywords, name))
        connect.commit()
        cur.close()
        connect.close()

    # def calculate_rewards(self, Unty_id,Name):
    #     cur = self.connect.cursor()
    #     result=getrewards(Unity_id)
    #     for row in result:
    #         OnTime=row[0]
    #         GoodJob=row[1]
    #         GoodQuestion=row[2]
    #     GQ=IsGoodQuestion(Unity_id,Name)
    #     OT=IsOnTime(Unity_id)
    #     GJ=IsGoodJob(Unity_id)
    #     GoodQuestion+=GQ
    #     GoodJob+=GJ
    #     OnTime+=OT
    #     update_reward_table(Unity_id,OnTime,GoodJob,GoodQuestion)
    #     cur.close()

    def get_submission_details(self, Name):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()
        cur = connect.cursor()
        cur.execute("Select * from Submission where Name=%s", (Name,))
        for row in cur:
            rows = row
        connect.commit()
        cur.close()
        connect.close()
        return rows

    def update_reward_table(self, Unity_id, Reward_Type):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()

        self.user_exists_reward_table(Unity_id)
        cur = connect.cursor()
        if Reward_Type == 'OnTime':
            cur.execute("Update Reward Set OnTime=OnTime+1 where Unity_id=%s",
                        (Unity_id,))
        elif Reward_Type == 'GoodQuestion':
            cur.execute("Update Reward Set GoodQuestion=GoodQuestion+1 where Unity_id=%s",
                        (Unity_id,))
        elif Reward_Type == 'GoodJob':
            cur.execute("Update Reward Set GoodJob=GoodJob+1 where Unity_id=%s",
                        (Unity_id,))

        connect.commit()
        cur.close()
        connect.close()

    def update_submission_grading(self, Name, Grade_Flag):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()
        cur = connect.cursor()
        if Grade_Flag:
            cur.execute("Update Submission Set Is_Graded=1 where Name=%s",
                        (Name,))
        else:
            cur.execute("Update Submission Set Is_Graded=0 where Name=%s",
                        (Name,))
        connect.commit()
        cur.close()
        connect.close()

    def get_keywords(self, Name):
        connect = self.get_connection()
        if not self.connect.is_connected():
            self.connect = self.get_connection()
        cur = connect.cursor()
        cur.execute("Select Keywords from Submission where Name=%s", (Name,))
        rows = ""
        for row in cur:
            rows = row
        # connect.commit()
        cur.close()
        connect.close()
        return rows

    def get_rewards(self, unityid):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()
        cur = connect.cursor()
        cur.execute("Select OnTime,GoodJob,GoodQuestion from Reward where Unity_id=%s", (unityid,))
        reward=[]
        for row in cur:
            reward.append(row[0])
            reward.append(row[1])
            reward.append(row[2])
        cur.close()
        connect.close()
        return reward


    def get_students(self):
        connect = self.get_connection()

        students=[]
        if not self.connect.is_connected():
            self.connect = self.get_connection()

        cur = connect.cursor()
        cur.execute("Select Unity_id from Reward")
        for row in cur:
           # if '@' in row[0]:
            #    students.append(str(row[0].split('@')[0]))
            #else:
                students.append(str(row[0]))
        cur.close()
        connect.close()
        return students

    def get_submission_details(self, submission_name):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()
        
        cur = connect.cursor()
        cur.execute("Select Name,Sub_Link ,Deadline,Num_Issues,Keywords,Is_Graded from Submission where Name=%s;",
                    (submission_name,))
        result = {}
        for row in cur:
            result['Name'] = row[0]
            result['Sub_Link'] = row[1]
            result['Deadline'] = row[2].strftime("%Y-%m-%dT%H:%M:%SZ")
            result['Num_Issues'] = row[3]
            result['Keywords'] = row[4]
            result['Is_Graded'] = row[5]
        # # if cur.rowcount:
        #     create a dict from the result as mocked above. 
        #     pass
        # else:
        cur.close()
        connect.close()
        return result

    def get_tags_valid_submissions(self, deadline):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()

        cur = connect.cursor()
        cur.execute("Select Name, Keywords from Submission where Deadline>=%s;", (deadline,))
        result = {}
        keyword = []
        for row in cur:
            if row[1] is not None:
                result[str(row[0])] = str(row[1]).split(',')
                keyword.extend(result[str(row[0])])
        # print(keyword)
        cur.close()
        connect.close()
        return keyword

    def start_grading(self):
        pass

    def get_ungraded_submissions(self, currentDate):
        if not self.connect.is_connected():
            self.connect = self.get_connection()

        connect = mysql.connector.connect(host=config.get('myvars','DB_HOST'), database=config.get('myvars','DB_NAME'), user=config.get('myvars','DB_USER'),
                                               password=config.get('myvars','DB_PWD'), buffered = True)
        cur = connect.cursor()
        cur.execute("Select Name, Deadline, Sub_Link,Num_Issues from Submission where Deadline < %s and Is_Graded = 0;",
                    (currentDate,))
        result = {}
        for row in cur:
            params = {'Deadline': row[1].strftime("%Y-%m-%dT%H:%M:%SZ"), 'Sub_Link': row[2], 'Num_Issues': row[3]}
            result[row[0]] = params
        # print(keyword)
        cur.close()
        connect.close()
        return result

    def user_exists_reward_table(self, Unity_id):
        connect = self.get_connection()

        if not self.connect.is_connected():
            self.connect = self.get_connection()

        cur = connect.cursor()
        cur.execute("Select * from Reward where Unity_id=%s", (Unity_id,))
        if cur.rowcount <= 0:
            cur.execute("Insert into Reward (Unity_id, OnTime, GoodJob, GoodQuestion) values (%s, 0, 0, 0)",
                        (Unity_id,))
            connect.commit()
        cur.close()
        connect.close()

