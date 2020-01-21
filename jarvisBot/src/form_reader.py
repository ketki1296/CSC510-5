import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re


class FormReader:

    def fetch_sheet(self, url):
        all_list = self.get_data(url)
        student_links = {}
        all_list = all_list[1:]
        for i in range(len(all_list)):
            if ',' in all_list[i][0]:
                student_tuple_list = (str(all_list[i][0])).split(',')
                student_tuple = tuple(i for i in student_tuple_list)
                student_links[student_tuple] = all_list[i][1]
            else:
                student_tuple = (all_list[i][0],)
                student_links[student_tuple] = all_list[i][1]
        return student_links

    def get_data(self, url):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        sh = client.open_by_url(str(url))
        worksheet = sh.get_worksheet(0)
        all_list = worksheet.get_all_values()
        return all_list
