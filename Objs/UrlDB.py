#!/usr/bin/python
#coding: utf-8
# use database to map whether url has been visited
class UrlDB():
    def __init__(self,pool):
        self.conn = pool.connection()
        self.cursor = self.conn.cursor()

    def has_url(self,url):
        hc = hash(url)
        query = "select * from URLVisited where hashCode='%d' " % (hc)
        lines = self.cursor.execute(query)
        if lines > 0:
            return True
        else:
            return False

    def set_url_visited(self, url):
        hashCode = hash(url)
        query = "insert into URLVisited(`url`,`hashCode`,`type`,``visited`) values('%s','%d','0','1') " % (url, hashCode)
        self.cursor.execute(query)
        self.cursor.commit()
