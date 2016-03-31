#!/usr/bin/python
#coding: utf-8
from Parser.DocParser import *
from Scanner.URLProducer import *
from bs4 import BeautifulSoup

# List All kinds of pages and its method to parse
class BasicPage():
    def __init__(self, username):
        self.username = username
        self.owner = self.username
        self.url = ""
        self.doc = ""
        self.status = ""    # page status: 404?
        self.soup = None

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def open(self):
        self.doc = download_document(self.url)
        if self.doc is "404" or self.doc is "":
            self.status = "404"
        else:
            self.soup = BeautifulSoup(self.doc)

    def is_corrent(self):
        if self.soup is None or self.doc is "" or self.doc is "404" or self.status is "404":
            return False
        else :
            return True

class UserHomePage(BasicPage):
    def __init__(self, username):
        BasicPage.__init__(self, username)
        homepage = URLProducer().create_user_homepage_url(username)
        self.set_url(homepage[0])
        self.open()


    def get_user_dict(self):
        if self.is_corrent() is False:
            return []
        user_dict = parse_user_basic_information(self.soup)
        return user_dict

    def get_user_repositories(self):
        if self.is_corrent() is False:
            return []
        repolists = parse_repo_list_item(self.soup)
        return repolists


class RepositoryPage(BasicPage):
    def __init__(self, username, reponame):
        BasicPage.__init__(self, username)
        self.reponame = reponame
        repourl = URLProducer().create_user_repository_url(username,reponame)
        self.set_url(repourl[0])
        self.open()

    # Readme and about of a repository
    def get_introduce(self):
        if self.is_corrent() is False:
            return "",""
        about = parse_repository_about(self.soup)
        readme = parse_repository_readme(self.soup)
        return (about, readme)


class FollowingPage(BasicPage):
    def __init__(self, username):
        BasicPage.__init__(self, username)
        pageurl = URLProducer().create_following_url(username)
        self.set_url(pageurl[0])
        self.open()

    def get_following(self):
        if self.is_corrent() is False:
            return []
        following = parse_follow_list_item(self.soup)
        return following

class FollowerPage(BasicPage):
    def __init__(self, username):
        BasicPage.__init__(self,username)
        pageurl = URLProducer().create_followers_url(username)
        self.set_url(pageurl[0])
        self.open()

    def get_followers(self):
        if self.is_corrent() is False:
            return []
        followers = parse_follow_list_item(self.soup)
        return followers

class MemberPage(BasicPage):
    def __init__(self, username,reponame):
        BasicPage.__init__(self,username)
        self.reponame = reponame
        pageurl = URLProducer().create_members_url(username, reponame)
        self.set_url(pageurl[0])
        self.open()

    def get_members(self):
        if self.is_corrent() is False:
            return []
        members = parse_repository_members(self.soup)
        return members

class PeoplePage(BasicPage):
    def __init__(self, username):
        BasicPage.__init__(self,username)
        pageurl = URLProducer().create_people_url(username)
        self.set_url(pageurl[0])
        self.open()

    def get_people(self):
        if self.is_corrent() is False:
            return []
        peopel = parse_repository_people(self.soup)

class WatchersPage(BasicPage):
    def __init__(self,username, reponame):
        BasicPage.__init__(self,username)
        pageurl = URLProducer().create_watchers_url(username,reponame)
        self.set_url(pageurl[0])
        self.open()

    def get_watchers(self):
        if self.is_corrent() is False:
            return []
        watchers = parse_repository_watchers(self.soup)

class StargazersPage(BasicPage):
    def __init__(self,username,reponame):
        BasicPage.__init__(self, username)
        pageurl = URLProducer().create_stargazers_url(username, reponame)
        self.set_url(pageurl[0])
        self.open()

    def get_stargazers(self):
        if self.is_corrent() is False:
            return []
        stargazers = parse_repository_stargazers(self.soup)
        return stargazers

class StarredPage(BasicPage):
    def __init__(self,username):
        BasicPage.__init__(self, username)
        pageurl = URLProducer().create_starred_url(username)
        self.set_url(pageurl[0])
        self.open()

    def get_starred_repositories(self):
        if self.is_corrent() is False:
            return []
        starred = parse_repo_list_item(self.soup)
        return starred

