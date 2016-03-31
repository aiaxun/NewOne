#!/usr/bin/python
#coding: utf-8

import threading
from Objs.RepositoryDB import *
from Objs.GitHubRepository import *
from Scanner.UsernameProducter import *
import time
from Parser.DocumentPages import *
from Objs.GitHubUser import *
from Objs.UserDB import *
"""
@author : Shenqintao
@date   : 2016.03.30
Filename: ResourceGenerator.py
"""
# Resource Pool
# Use Producer and Consumer Model, using multiThreads
# Thread  -> Produce urls to visit and put them to UrlQueue
# Thread  -> Get A Url to parse and put the result to user_info_queue -> then store
#


def init():
    global GitUsernameList
    global GitRepositoryList
    GitRepositoryList = Queue.Queue()
    GitUsernameList = UsernameProducer()
    GitUsernameList.init_queue()
    if GitUsernameList.empty():
        print "Now User Queue is empty, will begin from cocos-2d and lua"
        GitUsernameList.put("lua")
        GitUsernameList.put("cocos-2d")


class UserThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pool = create_db_pool("")

    def run(self):
        while True:
            if GitUsernameList.empty():
                time.sleep(3)
                continue
            username = GitUsernameList.get()
            if UserDB(self.pool).has_user(username) is True:
                continue
            print "Thread 1 ",username, " there is ", GitUsernameList.qsize()
            t1 = time.time()
            homepage = UserHomePage(username)
            user_dict = homepage.get_user_dict()
            user_following = FollowingPage(username).get_following()
            user_followers = FollowerPage(username).get_followers()
            gituser = User(username)
            if user_dict:
                gituser.set_basic_information(user_dict)
                gituser.set_followers(user_followers)
                gituser.set_following(user_following)
                u = UserDB(self.pool)
                u.add_user_to_db(gituser)
                u.add_relations_to_db(gituser)
                user_repo = homepage.get_user_repositories()
                GitRepositoryList.put((username, user_repo))

                new_user_list = list(set(user_following+user_followers))
                GitUsernameList.add_users(new_user_list)
            t2 = time.time()
            print "use time: ", t2-t1
            #GitUsernameList.task_done()
            #user_dict = UserHomePage()

class RepoThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pool = create_db_pool("")

    def run(self):
        while True:
            if GitRepositoryList.empty() is True:
                time.sleep(3)
                continue
            username,repolist = GitRepositoryList.get()
            for reponame in repolist:
                print "Thread 2 ", username, reponame, GitRepositoryList.qsize()
                t1 = time.time()
                about, readme = RepositoryPage(username,reponame).get_introduce()
                watchers = WatchersPage(username, reponame).get_watchers()
                if not watchers:
                    watchers = []
                stargazers = StargazersPage(username,reponame).get_stargazers()
                if stargazers is None:
                    stargazers = []
                members = MemberPage(username, reponame).get_members()
                if not members:
                    members = []

                new_repo = Repository(username, reponame)
                new_repo.set_watchers(watchers)
                new_repo.set_stargazers(stargazers)
                new_repo.set_about(about)
                new_repo.set_readme(readme)
                new_repo.set_members(members)
                RepositoryDB(self.pool).add_repository_to_db(new_repo)
                #new_repo.set_people(people)
                new_user_list = list(set(watchers+stargazers+members))

                GitUsernameList.add_users(new_user_list)
                #GitRepositoryList.task_done()
                t2 = time.time()
                print "using time :",t2-t1


