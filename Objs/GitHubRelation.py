#!/usr/bin/python
#coding: utf-8

# 
class RelatedUser():
    def __init__(self):
        self.userlist = []

    def add(self, username):
        if username not in self.userlist:
            self.userlist.append(username)

    def get(self):
        return self.userlist

    def count(self):
        return self.userlist.count()