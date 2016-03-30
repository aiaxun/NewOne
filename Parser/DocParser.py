#!/usr/bin/python
#coding: utf-8
import urllib2
from bs4 import BeautifulSoup


def download_document(url):
    htmldoc = urllib2.urlopen(url).read()
    return htmldoc

# method    :       parse()
# function  :       extract username list
# fit to    :       the pages contains CSS class of follow-list-item
# notice    :       Just parse one page
# https://github.com/ErisDS/Ghost/stargazers
# https://github.com/ErisDS/Ghost/watchers
# https://github.com/ErisDS/followers(?page=?)
# https://github.com/ErisDS/following
def parse_follow_list_item(soup):
    #soup = BeautifulSoup(html)
    itemlist = soup.findAll("li", "follow-list-item")
    if not itemlist or itemlist == 0:
        return []
    usernames = []
    for li in itemlist:
        atag = li.find('a')  # the first html tag 'a' contains the real homepage of one user
        newname = atag.attrs['href'][1:]
        usernames.append(newname)
    return usernames

# div repo-list-item public source
# h3 repo-list-name
# https://github.com/ErisDS?tab=repositories
# https://github.com/stars/ErisDS
def parse_repo_list_item(soup):
    itemlist = soup.findAll("h3", "repo-list-name")
    if not itemlist or len(itemlist) == 0:
        return []
    repolist = []
    for li in itemlist:
        reponame = li.a.attrs['href'].split('/')[-1]
        repolist.append(reponame)
    return repolist

# use to parse personal home pages
# https://github.com/ErisDS?tab=repositories
def parse_user_basic_information(soup):
    tags = soup.find("div","column one-fourth vcard")
    if not tags:
        return None
    imageurl    = tags.a.attrs['href']
    fullname    = soup.find("div", "vcard-fullname").getText()
    username    = soup.find("div", "vcard-username").getText()
    worksfor    = ""
    homelocation= ""
    email       = ""
    homepage    = ""
    jointime    = ""
    orgnizations= ""
    try:
        lists = soup.findAll("li","vcard-detail py-1 css-truncate css-truncate-target")
        if not lists or len(lists) is 0:
            print "nothing got from https://github.com/", username
        else:
            for li in lists:
                if li.has_attr('itemprop') is True:
                    if li['itemprop'] is 'worksfor':
                        worksfor = li.get_text('itemprop')
                    elif li['itemprop'] is 'homelocation':
                        homelocation = li.get_text('itemprop')
                    elif li['itemprop'] is 'url':
                        homepage = li.get_text('itemprop')
                    else:
                        pass
    except:
        pass
    try:
        email = soup.find('a',"email").getText()
    except:
        print "do not get ",username, " email"
    try:
        jointime = soup.find('time',"join-date")['datetime']
    except:
        print "do not get ", username, " join time"
    try:
        orgnizations = soup.find("div","clearfix").getText().strip()
    except:
        print "do not get ",username, "orgnization"

    return {'username': username, 'fullname': fullname, 'image': imageurl, 'worksfor': worksfor, \
            'homelocation': homelocation, 'jointime': jointime, \
            'email': email, 'homepage': homepage, "orgnizations":orgnizations}

# mainly Readme file
# https://github.com/ErisDS/Ghost
def parse_repository_readme(soup):
    text = ""
    try:
        text = soup.find('article').getText()
    except:
        print "the repository 's readme is empty"
    return text

# mainly find about
# https://github.com/ErisDS/Ghost
def parse_repository_about(soup):
    about = ""
    try:
        about = soup.find('span','repository-meta-content').getText().strip()
    except:
        print "do not find meta content in this repository"

    return about
#https://github.com/ErisDS/Ghost/network/members
def parse_repository_members(soup):
    repos = soup.findAll("div","repo")
    if len(repos) is 0 or not repos:
        return []
    userlist = []
    for r in repos:
        text = r.getText().replace('\n','').replace(' ','')
        userlist.append(text.split('/')[0])
    return userlist
