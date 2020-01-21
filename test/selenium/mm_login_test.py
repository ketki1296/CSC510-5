import datetime
import os
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary

link="https://docs.google.com/spreadsheets/d/1YzP8PrQ_wncYIRF5d45BlmCIe_-1oIKQpdNDjFiZNhI/edit#gid=0"
# Env Variables: PROFESSOR, PROFESSOR_PWD, TESTUSER, TESTUSER_PWD, TESTUSER2, TESTUSER2_PWD

class MattermostSeleniumTest(unittest.TestCase):
    def setUp(self):
        self.teamname = "csc-510-f19"
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")
        chromeOptions.add_argument("--disable-dev-shm-using")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        chromeOptions.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path="/usr/bin/chromedriver")
        self.url = "http://34.66.232.72:8065/"
        self.driver.get(self.url)
        sleep(2)

    def login(self, email, password):
        self.driver.find_element_by_name('loginId').send_keys(email)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('loginButton').click()
        sleep(2)

    def logout(self):
        self.driver.find_element_by_id('headerInfo').click()
        self.driver.find_element_by_id('logout').click()
        sleep(2)

    def finish(self):
        self.driver.quit()

    def postmessage(self, channel, msg=None):
        postchannel = self.url + self.teamname + channel
        self.driver.get(postchannel)
        sleep(2)
        if msg:
            element = self.driver.find_element_by_id('post_textbox')
            element.send_keys(msg)
            element.submit()
            sleep(1)
        a = self.driver.find_elements_by_class_name("post-message__text")
        return a[-1].text

    def test_use_case_1_happy(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel1-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 " + link)
        self.logout()

        self.login(os.environ["TESTUSER"], os.environ["TESTUSER_PWD"])
        self.postmessage('/messages/@jarvisbot', 'show-rewards')
        self.logout()
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        assert "Grading Done" == self.postmessage('/messages/@jarvisbot', 'start-grading ' + name)
        self.logout()
        self.login(os.environ["TESTUSER"], os.environ["TESTUSER_PWD"])
        assert "You received an On-Time Reward for " + name == self.postmessage('/messages/@jarvisbot')
        self.logout()

    def test_use_case_1_sad(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        name = 'test-sel1'
        date = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M")
        assert """Error invalid parameters. Usage: create-submission <name> 
                                         <Deadline YYYY/MM/DD-HH:MM> <# issues> <Submission Link>""" == self.postmessage(
            '/messages/@jarvisbot', 'create-submission '
                                    + name + " " + date + link)
        self.logout()

    def test_use_case_1_sad_2(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel1-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link)
        assert "Name already exists. Please provide a new Name." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link)
        self.logout()

    def test_use_case_1_sad_3(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M")
        wrong_date = datetime.datetime.now().strftime("%Y/%m/%d")
        name = 'test-sel1-' + date
        assert "Incorrect date format, should be YYYY/MM/DD-HH:MM." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + wrong_date + " 2 "+link)
        self.logout()

    def test_use_case_2_happy(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now()
        date = date.strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel2-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link)
        self.logout()
        self.login(os.environ["TESTUSER"], os.environ["TESTUSER_PWD"])
        self.postmessage('/messages/@jarvisbot', 'show-rewards')
        sleep(60)
        assert "You received a Good-Job Reward for creating tasks." == self.postmessage('/messages/@jarvisbot')
        self.logout()

    def test_use_case_2_sad(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now()
        date = date.strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel2-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link)
        self.logout()
        self.login(os.environ["TESTUSER2"], os.environ["TESTUSER2_PWD"])
        self.postmessage('/messages/@jarvisbot', 'show-rewards')
        sleep(60)
        assert "You received a Good-Job Reward for creating tasks." != self.postmessage('/messages/@jarvisbot')
        self.logout()

    def test_use_case_2_sad2(self):
        self.login(os.environ["PROFESSOR"],os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now()
        date = date.strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel2-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link)
        self.logout()
        self.login(os.environ["TESTUSER3"],os.environ["TESTUSER3_PWD"])
        self.postmessage('/messages/@jarvisbot', 'show-rewards')
        sleep(60)
        assert "You received a Good-Job Reward for creating tasks." != self.postmessage('/messages/@jarvisbot')
        self.logout()

    def test_use_case_3_happy(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now() + datetime.timedelta(minutes=5)
        date = date.strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel3-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link)
        assert "Keywords added." == self.postmessage('/messages/@jarvisbot',
                                                     'add-keywords ' + name + ' graphql,postgres')
        self.logout()
        self.login(os.environ["TESTUSER"], os.environ["TESTUSER_PWD"])
        self.postmessage('/channels/questions', "where is graphql used in the industry?")
        sleep(1)
        assert "You received a Good Question Reward for posting a relevant question" == self.postmessage(
            '/messages/@jarvisbot')
        self.logout()

    def test_use_case_3_sad(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now() - datetime.timedelta(minutes=5)
        date = date.strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel3-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link )
        assert "Keywords added." == self.postmessage('/messages/@jarvisbot',
                                                     'add-keywords ' + name + ' mockito,puppeteer')
        self.logout()
        self.login(os.environ["TESTUSER"], os.environ["TESTUSER_PWD"])
        self.postmessage('/messages/@jarvisbot', 'show-rewards')
        self.postmessage('/channels/questions', "where is mockito used in the industry?")
        sleep(1)
        assert "You received a Good Question Reward for posting a relevant question" != self.postmessage(
            '/messages/@jarvisbot')
        self.logout()

    def test_use_case_3_sad_2(self):
        self.login(os.environ["PROFESSOR"], os.environ["PROFESSOR_PWD"])
        date = datetime.datetime.now() + datetime.timedelta(minutes=5)
        date = date.strftime("%Y/%m/%d-%H:%M")
        name = 'test-sel3-' + date
        assert "Submission Created." == self.postmessage('/messages/@jarvisbot',
                                                         'create-submission ' + name + " " + date + " 2 "+link)
        assert "Keywords added." == self.postmessage('/messages/@jarvisbot',
                                                     'add-keywords ' + name + ' mockito,puppeteer')
        self.logout()
        self.login(os.environ["TESTUSER"], os.environ["TESTUSER_PWD"])
        self.postmessage('/messages/@jarvisbot', 'show-rewards')
        self.postmessage('/channels/questions', "What is the deadline?")
        sleep(1)
        assert "You received a Good Question Reward for posting a relevant question" != self.postmessage(
            '/messages/@jarvisbot')
        self.logout()

    def tearDown(self):
        self.driver.close()


# if __name__ == '__main__':
#     test = selenium_test()
#     test.use_case_1_happy()
#     test.use_case_1_sad()
#     test.use_case_2_sad2()
#     test.use_case_2_sad()
#     test.use_case_3_happy()
#     test.use_case_3_sad()
#     test.finish()
