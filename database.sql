create table usertype(id int primary key auto_increment,name varchar(20));
create table user(id int primary key auto_increment,username varchar(20),password varchar(200),secret varchar(200),usertype int,isemailverified int,isphoneverified int,status int,createdate datetime);
create table profile(id int primary key auto_increment,uid int,firstname varchar(200),lastname varchar(200),email varchar(100),phone varchar(50),address varchar(200),address2 varchar(200),city int,state int,country int,createdate datetime);


create table country(id int primary key auto_increment,name varchar(500));
create table state(id int primary key auto_increment,cid int,name varchar(500));
create table city(id int primary key auto_increment,sid int,name varchar(500));
create table job_type(id int primary key auto_increment,name varchar(200));

create table job(id int primary key auto_increment,jbtype int,title varchar(200),
description varchar(500),budgetmin double,budgetmax double,isawarded int,
duration int default 1,startdate datetime,enddate datetime,awarddate datetime);

create table job_application(id int primary key auto_increment,jid int,uid int,awarded int default 0);

create table notification(id int primary key auto_increment,senderid int default 0,uid int,status int,
title varchar(200),message longtext,isread int,createdate datetime);