import requests
from requests.models import Response
import os
import json
from mockito import when, mock, unstub
from form_reader import FormReader

headers = {
    'content-type': 'application/json',
    'authorization': 'token ' + os.environ["GITHUBTOKEN"]
}
form_url = "https://github.ncsu.edu/test/HW0-510"
url = "https://api.github.ncsu.edu/repos/test/HW0-510/commits/master"
another_url = "https://api.github.ncsu.edu/repos/test/HW0-510/issues"


def stop_mocking():
    unstub()


def start_mocking_forms():
    response = [["test@ncsu.edu", form_url]]
    when(FormReader).get_data("http://test.com").thenReturn(response)


def start_mocking_git():
    respobj = Response()
    respobj._content = b'{"commit": {"committer": {"date": "2019-09-06T08:20:34Z"}}}'
    when(requests).get(url, headers=headers).thenReturn(respobj)
    another_respobj = Response()
    another_respobj._content = b'[{"url": "https://abc.com"}, {"url": "https://bcd.com"}]'
    when(requests).get(another_url, headers=headers).thenReturn(another_respobj)

