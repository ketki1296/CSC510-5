from mattermostdriver import Driver
import os
import configparser
config=configparser.ConfigParser()
config.read('config.ini')
def get_driver():
    return Driver({
        'url': config.get('myvars','HOST'),
        'scheme': 'http',
        'port': 8065,
        'basepath': '/api/v4',
        'verify': True,
        'token': config.get('myvars','BOTTOKEN'),
        'debug': False
    });
