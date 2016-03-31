#!/usr/bin/python
#coding: utf-8

#public methods to create urls
class URLProducer():
    def __init__(self):
        self.baseurl = "https://github.com"

    # Following method used to make types of urls, return url and its type id
    # page type: '1'
    def create_user_homepage_url(self, username):
        return self.baseurl+'/'+username+'?tab=repositories',1

    # page type: '2'
    def create_user_repository_url(self, username, reponame):
        return self.baseurl+'/'+username+'/'+reponame,2

    # page type: '3'
    def create_watchers_url(self, username, reponame):
        return self.baseurl+'/'+username+'/'+reponame+'/watchers',3

    # page type: '4'
    def create_stargazers_url(self, username ,reponame):
        return self.baseurl+'/'+username+'/'+reponame+'/stargazers',4

    # page type: '5'
    def create_following_url(self, username):
        return self.baseurl + '/' + username + '/following',5

    # page type: '6'
    def create_followers_url(self, username):
        return self.baseurl + '/' + username + '/followers',6
    # page type: '7'
    def create_members_url(self, username, reponame):
        return  self.baseurl+'/'+username+'/'+reponame+'/network/members',7

    # page type: '8', orgnizations' home page
    def create_people_url(self, username):
        return self.baseurl+'/org/'+username+'/people',8

    # page type: '9': repositories one user starred\
    def create_starred_url(self, username):
        return self.baseurl + '/stars/'+username,9
