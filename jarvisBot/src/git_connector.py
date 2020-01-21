# imports
import sched, time, datetime, os
from datetime import datetime, timedelta
import os
import json
import requests
import configparser

config=configparser.ConfigParser()
config.read('config.ini')
header = {
    "content-type": "application/json",
    "authorization": "token " + config.get('myvars','GITHUBTOKEN')
}


def get_api_url(url):
    if url[-4:] == '.git':
        url = url[:-4]
    return url.replace("github", "api.github").replace("/", "/repos/", 3).replace("/repos/", "/", 2)


def fetch_last_commit(repo_url):
    url = get_api_url(repo_url) + "/commits/master"
    try:
        response = requests.get(url, headers=header).json()
        date = response["commit"]["committer"]["date"]
    except:
        print('Invalid repo Url ', url)
        return None
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ") - timedelta(seconds=18000)


def fetch_num_of_tasks(repo_url, deadline):
    url = get_api_url(repo_url) + "/issues"
    response = requests.get(url, headers=header).json()
    valid_responses = 0
    for item in response:
        task_creation_time = datetime.strptime(item["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        if task_creation_time <= deadline:
            valid_responses += 1
    return valid_responses
