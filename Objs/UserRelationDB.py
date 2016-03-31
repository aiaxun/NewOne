#!/usr/bin/python
#coding: utf-8

class UserRelationDB():
    def __init__(self, pool):
        self.conn = pool.connection()
        self.cursor = self.conn.cursor()

    def get_following(self,username):
        following = []
        query = "select following from UserRelations where username='%s'" % (username)
        lines = self.cursor.execute(query)
        if lines > 0:
            results = self.cursor.fetchall()
            for rows in results:
                following.append(rows[0])

        return following

    def get_followers(self, username):
        followers = []
        query = "select username from UserRelations where following='%s'" % (username)
        lines = self.cursor.execute(query)
        if lines > 0:
            results = self.cursor.fetchall()
            for rows in results:
                followers.append(rows[0])

        return followers

    def add_relation(self,username, following):
        query = "insert into UserRelations(username, following, hashCode) VALUES " +\
                "('%s','%s','%d')" % (username, following, hash(username+'#'+following))
        lines = self.cursor.execute(query)
        self.cursor.commit()
        return lines

    def add_relations(self, username, following):
        lines = 0
        for name in following:
            lines += self.add_relation(username, name)
        return lines