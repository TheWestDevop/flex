# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models.models import Job,JobApplication,JobType,User,UserType,Country,City,State,Notifiaction,Profile
# Register your models here.
admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(JobType)
admin.site.register(User)
admin.site.register(UserType)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Profile)
admin.site.register(Notifiaction)