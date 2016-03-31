#!/usr/bin/python
#coding: utf-8

from json import *
# if we want to get members in a repository, just visit and parse
#       https://github.com/username/repository_name/network/members
# and it is neccessary to remove names which are duplicated when using

class Repository():
    def __init__(self,username, reponame):
        self.username       = username
        self.reponame       = reponame      # from given username and reponame, we can visit the repository
        self.hashCode       = hash(username+"#"+reponame)
        self.contributors   = []            # do not consider now
        self.watchers       = []            #
        self.stargazers     = []
        self.members        = []            # visit the resource at */network/members
        self.people         = []
        self.about          = ""            # about
        self.readme         = ""            # some repositories do not maintain Readme.me files
                                            # when we could not find <div id="readme" class="readme"> tags
                                            # and then, just use soup.getText() method
    def get_dict(self):
        self.dict = {"username":        self.username, \
                     "reponame":        self.reponame, \
                     "hashCode":        self.hashCode,\
                     "people":          self.people, \
                     "watchers":        self.watchers, \
                     "stargazers":      self.stargazers, \
                     "members":         self.members, \
                     "about":           self.about,\
                     "readme":          self.readme}

        return self.dict

    def set_about(self, about):
        self.about = about

    def set_watchers(self, watchers):
        self.watchers = watchers

    def set_members(self,members):
        self.members = members

    def set_readme(self, readme):
        self.readme = readme

    def set_stargazers(self, stargazers):
        self.stargazers = stargazers

    def set_people(self, people):
        self.people = people

    def set_contributors(self, contri):
        self.contributors = contri

    def to_json(self):
        self.get_dict()
        return JSONEncoder().encode(self.dict)
