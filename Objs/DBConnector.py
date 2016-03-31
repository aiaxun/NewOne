#!/usr/bin/python
#coding: utf-8
import ConfigParser
from DBUtils import PooledDB
import MySQLdb

# create a database connection pool
def create_db_pool(config_file):
    if config_file == "" or config_file is None:
        config_file = "/home/kylin/PycharmProjects/GithubCollector/db.config"
    #print config_file
    conf = ConfigParser.ConfigParser()
    conf.read(config_file)
    # sections = conf.sections()
    try:
        dbhost = conf.get("mysql_database", "host")
        dbname = conf.get("mysql_database", "dbname")
        dbport = conf.getint("mysql_database", "port")
        username = conf.get("mysql_database", "username")
        password = conf.get("mysql_database", "password")
        pool = PooledDB.PooledDB(MySQLdb, 10, 4, 10, 10, False,\
                                 host=dbhost, user=username,passwd=password,db=dbname,port=dbport,charset='utf8')
        #print "create database pool"
        return pool
    except:
        print "failed to connect Database"
        exit(-1)

# get file name from config file
def get_username_list_file(config_file):
    if config_file == "" or config_file is None:
        config_file = "/home/kylin/PycharmProjects/GithubCollector/db.config"
    conf = ConfigParser.ConfigParser()
    conf.read(config_file)
    try:
        filename = conf.get("resource","userlist")
        return filename
    except:
        print "error to get resource userlist file"




