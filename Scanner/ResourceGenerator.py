#!/usr/bin/python
#coding: utf-8

import Queue

"""
@author : Shenqintao
@date   : 2016.03.30
Filename: ResourceGenerator.py
"""
# Resource Pool
class SeedRepositoriesQueue():
    def __init__(self, queue_len):
        if not queue_len:
            queue_len = 100
        self.queue = Queue.Queue(maxsize=queue_len)
        self.baseUrl = ""

    def set_baseurl(self, baseUrl):
        self.baseUrl = baseUrl

    def enqueue(self, username, reponame):
        url = self.baseUrl + "/" + username + "/" + reponame
        self.queue.put(url)

    def get(self):
        return self.queue.get()

    def count(self):
        return self.queue.qsize()

class SeedUsersQueue():
    def __init__(self, queue_len):
        if not queue_len:
            queue_len = 100
        self.queue = Queue.Queue(maxsize=queue_len)
        self.baseurl = ""

    def set_baseurl(self, baseurl):
        self.baseurl = baseurl

    def enqueue(self, username):
        url = self.baseurl+'/'+username+"?tab=repositories"
        self.queue.put(url)

    def get(self):
        return self.queue.get()

    def count(self):
        return self.queue.qsize()
