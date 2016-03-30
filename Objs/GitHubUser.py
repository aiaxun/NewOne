#!/usr/bin/python
#coding: utf-8

from json import *

class User():
    def __init__(self, username):
        self.username       = username  # unique flag for each user
        self.email          = ""        # maybe some user do not show their email address
        self.fullname       = ""
        self.photourl       = ""
        self.repos          = []        # repositories the user own
        self.homepage       = ""        # some users show their own website address
        self.homelocation   = ""        # users' location information
        self.jointime       = ""        #
        self.worksfor       = ""        # work team
        self.orgnizations   = []        # orgnizations, maybe more than one
        self.followers      = []        # will store User() objects of followers
        self.following      = []        # ..
        self.starred        = []        # repositories the user starred
        self.hashcode       = hash(username)
                                        # in Github, the username is different from each other

    # the content of user_dict could be collected from https://github.com/username?tab=repositories
    def set_basic_information(self, user_dict):
        self.email          = user_dict['email']
        self.fullname       = user_dict['fullname']
        self.photourl       = user_dict['image']
        self.homelocation   = user_dict['homelocation']
        self.homepage       = user_dict['homepage']
        self.worksfor       = user_dict['worksfor']
        self.orgnizations   = user_dict['orgnizations']
        self.jointime       = user_dict['jointime']
        self.repos          = user_dict['repositories']

    # the follow information would be collected from other related pages: star, following, followers
    #self.followers
    #self.following
    #self.starred
    def set_followers(self, followers):
        self.followers = followers

    def set_following(self, following):
        self.following = following

    def set_starred(self, starred):
        self.starred = starred

    # use to get user information
    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def get_starred(self):
        return self.starred

    def get_username(self):
        return self.username

    def get_dict(self):
        self.dict = {'username':    self.username, \
                     'email':       self.email, \
                     'fullname':    self.fullname,\
                     'image':       self.photourl, \
                     'homelocation':self.homelocation,\
                     'homepage':    self.homepage, \
                     'worksfor':    self.worksfor, \
                     'orgnizations':self.orgnizations, \
                     'jointime':    self.jointime, \
                     'repositories':self.repos, \
                     'followers':   self.followers, \
                     'following':   self.following, \
                     'starred':     self.starred, \
                     'hashcode':    self.hashcode}
        return self.dict

    # make it easier to write to files
    def to_json(self):
        self.get_dict()
        return JSONEncoder().encode(self.dict)

# There is a little different between personal user and orgnization user
# html tags <div class="org-main">... maybe easier to be found and handle
class OrgnizationUser(User):
    def __init__(self, username):
        User.__init__(username)
        self.people         = []
        self.website_url    = []
