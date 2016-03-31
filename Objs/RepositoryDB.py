#!/usr/bin/python
#coding: utf-8
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

    def add_repository_to_db(self, repository):
        info = repository.get_dict()
        username        = info['username']
        reponame        = info['reponame']
        hashCode        = info['hashCode']
        #contributors    = info['contributors']
        watchers        = info['watchers']
        stargazers      = info['stargazers']
        members         = info['members']
        readme          = info['readme']
        about           = info['about']
        readme = unicode(readme.replace("\"", " ").replace("\'", ' '))
        about  = unicode(about.replace("\"", " ").replace("\'", ' '))
        query = "INSERT INTO GithubRepository(username, reponame, hashCode, about, readme) VALUES "+\
            """("%s","%s","%d","%s","%s")""" % (username, reponame, hashCode, about, readme)
        try:
            self.cursor.execute(query)
        except:
            print query
            print "error when adding repository"

        print """**************************************************8""",len(watchers), len(stargazers)

        insert_to_watcher = "INSERT INTO Watchers(owner, repository, watcher, hashCode) VALUES "
        for watcher in watchers:
            try:
                q = insert_to_watcher+"('%s','%s','%s','%d')" % (username,reponame,watcher,hash(username+"#"+reponame+"#"+watcher))
                print q
                self.cursor.execute(q)
                self.conn.commit()
            except:
                print q
                print "error when inserting into watchers"
        #self.conn.commit()

        insert_to_star = "Insert into Star(owner, repository, star, hashCode) VALUES "
        for star in stargazers:
            q = insert_to_star + "('%s','%s','%s','%d')" % (username, reponame, star, hash(username+'#'+reponame+'#'+star))
            try:
                self.cursor.execute(q)
                self.conn.commit()
            except:
                print q
                print "error when inserting into Star"

