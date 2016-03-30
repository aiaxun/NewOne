#!/usr/bin/python
#coding: utf-8

# use database to map whether url has been visited
class TaskDone():
    def __init__(self,pool):
        self.conn = pool.connection()
        self.cursor = self.conn.cursor()

    def isDone(self,url):
        hc = hash(url)
        query = "select url from URLVisited where hashCode=%d" % (hc)
        if self.cursor.execute(query):
            return True
        else:
            return False

    def setUrlDone(self, url):
        hashCode = hash(url)
        query = "insert into URLVisited(`url`,`hashCode`,`visited`) values('%s','%d','1') " % (url, hashCode)
        self.cursor.execute(query)

    def close(self):
        self.conn.close()

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
    def add_user_information(self, user):
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
            if self.cursor.execute(query):
                print "insert one user_information to GithubUser"
        except:
            print "error occured when insert user information"
            print query

        # Insert table UserRelations
        followers   = info['followers']
        following   = info['following']
        query = "Insert into UserRelations(username,following,hashCode) VALUES "
        # Here, hashCode is limited by qunique and username, following are both primary key.
        # so I choose to insert one by one, to make sure workflow correct
        for user in followers:
            q = query+"('%s','%s','%d')," % (user,username,hash(user+"###"+username))
            try:
                self.cursor.execute(q)
            except:
                print q
        for user in following:
            q = query+"('%s','%s','%d')," % (username, user, hash(username+"###"+user))
            try:
                self.cursor.execute(q)
            except:
                print q

class RepositoryDB():
    def __init__(self,pool):
        self.conn = pool.connection()
        self.cursor = self.conn.cursor()

    def has_Repository(self, username, reponame):
        query = "select id from GithubRepository where hashCode='%s'" % (hash(username+"#"+reponame))
        #query = "select id from GithubRepository where username='%s' and reponame='%s'"%(username, reponame)
        lines = self.cursor.execute(query)
        if lines > 0:
            return True
        else:
            return False

    def addRepository(self, repository):
        info = repository.get_dict()
        username        = info['username']
        reponame        = info['reponame']
        hashCode        = info['hashCode']
        contributors    = info['contributors']
        watchers        = info['watchers']
        stargazers      = info['stargazers']
        members         = info['members']
        readme          = info['readme']
        about           = info['about']
        query = "INSERT INTO GithubRepository(username, reponame, hashCode, about, readme) VALUES "+\
            "('%s','%s','%d','%s','%s')" % (username, reponame, hashCode, about, readme)
        try:
            self.cursor.execute(query)
        except:
            print query
            print "error when adding repository"
        insert_to_watcher = "INSERT INTO Watchers(owner, repository, watcher, hashCode) VALUES "
        for watcher in watchers:
            q = insert_to_watcher+"('%s','%s','%s','%d')" % (username,reponame,watcher,hash(username+"#"+reponame+"#"+watcher))
            try:
                self.cursor.execute(q)
            except:
                print q
                print "error when inserting into watchers"

        insert_to_star = "Insert into Star(owner, repository, star, hashCode) VALUES "
        for star in stargazers:
            q = insert_to_star + "('%s','%s','%s','%d')" % (username, reponame, star, hash(username+'#'+reponame+'#'+star))
            try:
                self.cursor.execute(q)
            except:
                print q
                print "error when inserting into Star"


