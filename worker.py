#!/usr/bin/python
#coding: utf-8

from Objs.GitHubUser import *
from Objs.GitHubRepository import *
from Parser.DocParser import *
from Scanner.ResourceGenerator import *
from DBUtils import PooledDB

def create_db_pool(config_file):
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
        return pool
    except:
        exit(-1)

def worker():
    config = "./db.config"
    DBPool = create_db_pool(config)
    con = DBPool.connection()
    cur = con.cursor()
    cur.execute("desc URLVisited")
    r = cur.fetchone()
    print r

if __name__ == "__main__":
    worker()