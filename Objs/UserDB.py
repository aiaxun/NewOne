#!/usr/bin/python
#coding: utf-8

class UserDB():
    def __init__(self,pool):
        self.conn = pool.connection()
        self.cursor = self.conn.cursor()

    def has_user(self, username):
        hashCode = hash(username)
        query = "select * from GitHubUser where hashcode=%d" % (hashCode)
        l = self.cursor.execute(query)
        if l:
            return True
        else:
            return False
    # when user dict is able to use, its follower, following, starred has been prepared
    # so, here we insert those messages into database excludes starred.
    def add_user_to_db(self, user):
        info = user.get_dict()
        username    = info['username']
        hashcode    = info['hashcode']
        email       = info['email']
        fullname    = info['fullname']
        photourl    = info['image']
        homepage    = info['homepage']
        worksfor    = info['worksfor']
        jointime    = info['jointime']
        homelocation= info['homelocation']
        orgnizations= info['orgnizations']
        query = "Insert into GitHubUser(username, hashcode, fullname, email, "+\
                "photourl, homepage, homelocation, jointime, worksfor, orgnizations) "+\
                "values ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                (username, hashcode, fullname, email, photourl, homepage, homelocation, \
                 jointime, worksfor, orgnizations)
        try:
            line =  self.cursor.execute(query)

            if line > 0:
                print "insert one user_information to GithubUser"
                #print query
        except:
            print "error occured when insert user information"


    def add_relations_to_db(self,user):
        # Insert table UserRelations
        following = user.get_following()
        followers = user.get_followers()
        username  = user.get_username()

        query = "Insert into UserRelations(username,following,hashCode) VALUES "
        # Here, hashCode is limited by qunique and username, following are both primary key.
        # so I choose to insert one by one, to make sure workflow correct
        if not followers:
            followers = []
        if not following:
            following = []
        for user in followers:
            q = query+"('%s','%s','%d');" % (user,username,hash(user+"###"+username))
            try:
                self.cursor.execute(q)
            except:
                print "Error"
        for user in following:
            q = query+"('%s','%s','%d');" % (username, user, hash(username+"###"+user))
            try:
                self.cursor.execute(q)
            except:
                print "error"
        self.conn.commit()