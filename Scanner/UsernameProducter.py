#!/usr/bin/python
#coding: utf-8

import Queue

from Objs.DBConnector import *
import pandas as pd

class UsernameProducer(Queue.Queue):
    def __init__(self):
        Queue.Queue.__init__(self,maxsize=2048)
        # each item in user_to_visit queue contains just username, type: str

    def init_queue(self):
        filename = get_username_list_file("")
        userlists = self.get_username_from_file(filename)           # file name is get from config file
        for username in userlists:
            self.put(username)

    # when use it first time, It maybe useful to get a username list from local file as seeds
    def get_username_from_file(self, filename):
        try:
            table = pd.read_csv(filename)
            return list(table['username'])
        except:
            print "fail to read file"

    def add_users(self, users):
        for user in users:
            if self.full() is False:
                self.put(user)

