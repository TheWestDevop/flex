# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

# Create your models here.
class UserType(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=20)


class User(models.Model):
      id               = models.AutoField(primary_key=True)
      username         = models.CharField(max_length=10)
      password         = models.CharField(max_length=200)
      secret           = models.CharField(max_length=200)
      usertype         = models.IntegerField()
      isemailverified  = models.IntegerField()
      isphoneverified  = models.IntegerField()
      status           = models.IntegerField()
      createdate       = models.DateTimeField(default=now)


class Profile(models.Model):
      id         = models.AutoField(primary_key=True)
      uid        = models.IntegerField()
      firstname  = models.CharField(max_length=200)
      lastname   = models.CharField(max_length=200)
      email      = models.EmailField(max_length=100)
      telephone  = models.CharField(max_length=200)
      address    = models.CharField(max_length=200)
      address2   = models.CharField(max_length=200)
      city       = models.IntegerField()
      state      = models.IntegerField()
      country    = models.IntegerField()
      createdate = models.DateTimeField(default=now)


class Country(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=500)


class  State(models.Model):
       id   = models.AutoField(primary_key=True)
       name = models.CharField(max_length=500)
       cid  = models.IntegerField()


class  City(models.Model):
       id   = models.AutoField(primary_key=True)
       name = models.CharField(max_length=500)
       sid  = models.IntegerField()      


class JobType(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=200)


class Job(models.Model):
       id            = models.AutoField(primary_key=True)
       jbtype        = models.IntegerField()
       title         = models.CharField(max_length=200)
       description   = models.CharField(max_length=500)
       budgetmin     = models.BigIntegerField() 
       budgetmax     = models.BigIntegerField()
       isawarded     = models.IntegerField()
       duration      = models.IntegerField(default=1) 
       startdate     = models.DateTimeField(null=True,blank=True)
       enddate       = models.DateTimeField(null=True,blank=True)
       awarddate     = models.DateTimeField(null=True,blank=True)


class JobApplication(models.Model):
      id   = models.AutoField(primary_key=True)
      jid        = models.IntegerField()
      uid       = models.IntegerField()
      awarded       = models.IntegerField(default=0)


class Notifiaction(models.Model):
      id            = models.AutoField(primary_key=True)
      senderid       = models.IntegerField(default=0)
      uid       = models.IntegerField()
      status           = models.IntegerField()
      title         = models.CharField(max_length=200)
      message      = models.TextField()
      isread           = models.IntegerField()
      createdate     = models.DateTimeField(default=now)