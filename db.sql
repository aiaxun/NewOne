Create database if not exists `GithubCollector` DEFAULT CHARSET utf8;

use GithubCollector;

Create table if not exists `URLVisited` (
    `id`   bigint(20) NOT NULL auto_increment PRIMARY KEY,
    `url`  varchar(255) UNIQUE NOT NULL,
    `hashcode` varchar(40) NOT NULL,
    `visited` boolean NOT NULL
)ENGINE='InnoDB' CHARSET=utf8;

Create table if not exists `GitHubUser` (
    `id`   int(12) NOT NULL auto_increment PRIMARY KEY,
    `username` varchar(255) NOT NULL,
    `hashcode` varchar(40) NOT NULL,
    `fullname` varchar(255),
    `email` varchar(255),
    `photourl` varchar(255),
    `homepage` varchar(255),
    `homelocation` varchar(255),
    `jointime` varchar(20),
    `worksfor` varchar(80),
    `orgnizations` varchar(255)
)ENGINE=innodb DEFAULT CHARSET=utf8;

# store repositories basic message: owner and descripe
Create table if not exists `GithubRepository` (
    `id`  int(12) Not NULL auto_increment,
    `username` varchar(255) NOT NULL,
    `reponame` varchar(255) NOT NULL,
    `hashCode` varchar(40) NOT NULL,
    `about` text,
    `readme` text,
    primary key(`id`,`username`,`reponame`)
)engine=innodb DEFAULT CHARSET=utf8;

# record relations between users: follower, following
# hashCode generte: hash(username+"###"+following)
Create TABLE IF NOT EXISTS `UserRelations` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL ,
    `following` VARCHAR(255) NOT NULL ,
    `hashCode` VARCHAR(40) NOT NULL UNIQUE ,
    PRIMARY KEY (id,username,following)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

# this table is used to store urls prepare to visit next time started
# type:
# '1': UserHomePage
# '2': Repository Page
# '3': Watchers Page
# '4': Stargazers Page
# '5': Following Page
# '6': Followers Page
# '7': Members Page
# '8': People Page
#
Create table if not EXISTS `toVisit` (
    `id` int not null PRIMARY KEY ,
    `url` VARCHAR(255) not null,
    `types` CHAR(1) NOT NULL ,
    `hashCode` VARCHAR(40) not NULL UNIQUE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

# relations between user and repository
# hashcode: hash(owner+"#"+repository+"#")
CREATE TABLE IF NOT EXISTS `Watchers` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `owner` VARCHAR(255) NOT NULL ,
    `repository` VARCHAR(255) NOT NULL ,
    `watcher` VARCHAR(255) NOT NULL,
    `hashCode` VARCHAR(40) NOT NULL UNIQUE,
    PRIMARY KEY (id,owner,repository)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

# relations between user and repository
CREATE TABLE IF NOT EXISTS `Star` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `owner` VARCHAR(255) NOT NULL ,
    `repository` VARCHAR(255) NOT NULL ,
    `star` VARCHAR(255) NOT NULL,
    `hashCode` VARCHAR(40) NOT NULL UNIQUE,
    PRIMARY KEY (id,owner,repository)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;