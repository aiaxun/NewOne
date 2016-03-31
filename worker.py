#!/usr/bin/python
#coding: utf-8


from Scanner.ResourceGenerator import *



if __name__ == "__main__":
    init()
    for i in range(3):
        GetUserInformation  = UserThread()
        GetUserInformation.start()
        GetRepositoryInfomation = RepoThread()
        GetRepositoryInfomation.start()

