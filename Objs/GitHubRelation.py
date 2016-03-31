#!/usr/bin/python
#coding: utf-8

# 
class RelatedUser():
    def __init__(self):
        self.following = []
        self.followers = []

    def add_following(self, username):
        self.following.append(username)

    def add_followers(self, username):
        self.followers.append(username)

    def get_following(self):
        return self.following

    def get_followers(self):
        return  self.followers