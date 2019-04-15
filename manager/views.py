# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as AuthLogOut
from models.models import Job,JobApplication,JobType,User,UserType,Country,City,State,Notifiaction,Profile,Admin,AdminType
import random,string,hashlib
# Create your views here.

#CRUD for User Model  ----------------------------------------------------------------------------------------------
def list_user(request):
    users = User.objects.all()
    return render(request,'index.html',{'users':users}) 


def create_user(request):
    if request.method == 'POST':
            username = request.POST.get( 'username')
            password = request.POST.get('password')
            secret  = request.POST.get('secret')
            usertype = int(request.POST.get('usertype'))
            isemailverified = 0
            isphoneverified = 0
            status = 0

            obj = User.objects.create(
               username = username,
               password = password,
               secret  = secret ,
               usertype = usertype,
               isemailverified = isemailverified,
               status = status,
               isphoneverified = isphoneverified,
            )
            
            return redirect('list_user')
    else:
         return render(request,'forms/user.html') 


def update_user(request,id):

    
    user  = User.objects.get(id=id)

    

    if request.method == 'POST':
            user.username = request.POST.get( 'username')
            user.password = request.POST.get('password')
            user.secret  = request.POST.get('secret')
            user.usertype = int(request.POST.get('usertype'))
            user.isemailverified = 0
            user.isphoneverified = 0
            user.status = 0
            user.save()

            return redirect('list_user')


    return render(request,'forms/user.html',{'user':user})



def delete_user(request,id):
     
    user = User.objects.get(id=id)
     
    if request.method == 'POST':
        user.delete()
        return redirect('list_user')
      

    return render(request,'delete.html',{'user': user}) 


#CRUD for Profile Model  ----------------------------------------------------------------------------------------------

def list_profile(request):
    profiles = Profile.objects.all()
    return render(request,'index.html',{'profiles':profiles}) 


def create_profile(request):
    if request.method == 'POST':
            uid= request.POST.get( 'uid')
            firstname = request.POST.get('firstname')
            lastname  = request.POST.get('lastname')
            email = int(request.POST.get('email'))
            telephone = request.POST.get('telephone')
            address = request.POST.get('address')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')

            obj = Profile.objects.create(
               firstname = firstname,
               lastname = lastname,
               email  = email,
               telephone = telephone,
               address = address,
               address2 = address2,
               city = city,
               state =  state,
               country = country,
            )
            
            return redirect('list_profile')
    else:
         return render(request,'forms/profile.html') 


def update_profile(request,id):

    
    profile  = Profile.objects.get(id=id)

    

    if request.method == 'POST':

            profile.uid= int(request.POST.get( 'uid'))
            profile.firstname = request.POST.get('firstname')
            profile.lastname  = request.POST.get('lastname')
            profile.email = int(request.POST.get('email'))
            profile.telephone = request.POST.get('telephone')
            profile.address = request.POST.get('address')
            profile.address2 = request.POST.get('address2')
            profile.city = request.POST.get('city')
            profile.state = request.POST.get('state')
            profile.country = request.POST.get('country')
            profile.save()

            return redirect('list_profile')


    return render(request,'forms/profile.html',{'profile':profile})



def delete_profile(request,id):
     
    profile = Profile.objects.get(id=id)
     
    if request.method == 'POST':
        profile.delete()
        return redirect('list_profile')
      

    return render(request,'delete.html',{'profile': profile}) 



#CRUD for UserType Model ----------------------------------------------------------------------------------------------

def list_usertype(request):
    usertypes = UserType.objects.all()
    return render(request,'usertype.html',{'usertypes':usertypes}) 


def create_usertype(request):
    if request.method == 'POST':
           name = request.POST.get( 'name')
           obj = User.objects.create(name = name)
           return redirect('list_usertype')
    else:
         return render(request,'forms/usertype.html') 


def update_usertype(request,id):
   
    usertype  = UserType.objects.get(id=id)   

    if request.method == 'POST':
            usertype.name = request.POST.get( 'name')
            usertype.save()

            return redirect('list_user')

    return render(request,'forms/user.html',{'usertype':usertype})



def delete_usertype(request,id):
     
    usertype = UserType.objects.get(id=id)
     
    if request.method == 'POST':
        usertype.delete()
        return redirect('list_usertype')
      

    return render(request,'delete.html',{'usertype': usertype}) 


#CRUD for Country Model ----------------------------------------------------------------------------------------------

def list_country(request):
    countries = Country.objects.all()
    return render(request,'country.html',{'countries':countries}) 


def create_country(request):
    if request.method == 'POST':
           country = request.POST.get('name')
           obj = Country.objects.create(name = country)
           return redirect('list_country')
    else:
         return render(request,'forms/country.html') 


def update_country(request,id):
   
    country  = Country.objects.get(id=id)   

    if request.method == 'POST':
            country.name = request.POST.get('name')
            country.save()

            return redirect('list_country')

    return render(request,'forms/country.html',{'country':country})



def delete_country(request,id):
     
    country = Country.objects.get(id=id)
     
    if request.method == 'POST':
        country.delete()
        return redirect('list_country')
      

    return render(request,'delete.html',{'country': country}) 


#CRUD for State Model ----------------------------------------------------------------------------------------------

def list_state(request):
    states = State.objects.all()
    return render(request,'state.html',{'states':states}) 


def create_state(request):
    if request.method == 'POST':
           state = request.POST.get('name')
           cid = int(request.POST.get('cid'))
           obj = State.objects.create(
               name = state,
               cid  = cid
               )
           return redirect('list_state')
    else:
         return render(request,'forms/state.html') 


def update_state(request,id):
   
    state  = State.objects.get(id=id)   

    if request.method == 'POST':
            state.name = request.POST.get('name')
            state.cid  = int(request.POST.get('cid'))
            state.save()

            return redirect('list_state')

    return render(request,'forms/state.html',{'state':state})



def delete_state(request,id):
     
    state = State.objects.get(id=id)
     
    if request.method == 'POST':
        state.delete()
        return redirect('list_state')
      

    return render(request,'delete.html',{'state': state}) 

#CRUD for City Model ----------------------------------------------------------------------------------------------

def list_city(request):
    cities = City.objects.all()
    return render(request,'cities.html',{'cities': cities}) 


def create_city(request):
    if request.method == 'POST':
           city = request.POST.get('name')
           sid = int(request.POST.get('sid'))
           obj = City.objects.create(
               name = city,
               sid  = sid
               )
           return redirect('list_city')
    else:
         return render(request,'forms/city.html') 


def update_city(request,id):
   
    city  = City.objects.get(id=id)   

    if request.method == 'POST':
            city.name = request.POST.get('name')
            city.sid  = int(request.POST.get('sid'))
            city.save()

            return redirect('list_city')

    return render(request,'forms/city.html',{'city':city})


def delete_city(request,id):
     
    city = City.objects.get(id=id)
     
    if request.method == 'POST':
        city.delete()
        return redirect('list_city')
      

    return render(request,'delete.html',{'city': city}) 


#CRUD for JobType Model ----------------------------------------------------------------------------------------------

def list_jobtype(request):
    jobtypes = JobType.objects.all()
    return render(request,'jobtype.html',{'jobtypes':jobtypes}) 


def create_jobtype(request):
    if request.method == 'POST':
           jobtype = request.POST.get('name')
           obj = JobType.objects.create(name = jobtype)
           return redirect('list_jobtype')
    else:
         return render(request,'forms/jobtype.html') 


def update_jobtype(request,id):
   
    jobtype = JobType.objects.get(id=id)   

    if request.method == 'POST':
            jobtype.name = request.POST.get('name')
            jobtype.save()

            return redirect('list_jobtype')

    return render(request,'forms/jobtype.html',{'jobtype':jobtype})



def delete_jobtype(request,id):
     
    jobtype = JobType.objects.get(id=id)
     
    if request.method == 'POST':
        jobtype.delete()
        return redirect('list_jobtype')
      

    return render(request,'delete.html',{'jobtype': jobtype}) 


#CRUD for JobApplication Model----------------------------------------------------------------------------------------------

def list_job_application(request):
    job_applications = JobApplication.objects.all()
    return render(request,'job_applications.html',{'job_applications': job_applications}) 


def create_job_application(request):
    if request.method == 'POST':
           jid = int(request.POST.get('jid'))
           uid  = int(request.POST.get('uid'))
           awarded = int(request.POST.get('awarded'))
           obj = JobApplication.objects.create(
               jid = jid,
               uid  = uid,
               awarded = awarded
               )
           return redirect('list_job_application')
    else:
         return render(request,'forms/job_application.html') 


def update_job_application(request,id):
   
    job_application  = JobApplication.objects.get(id=id)   

    if request.method == 'POST':
            job_application.jid = int(request.POST.get('jid'))
            job_application.uid  = int(request.POST.get('uid'))
            job_application.awarded = int(request.POST.get('awarded'))

            job_application.save()

            return redirect('list_job_application')

    return render(request,'forms/job_application.html',{'job_application':job_application})


def delete_job_application(request,id):
     
    job_application = JobApplication.objects.get(id=id)
     
    if request.method == 'POST':
        job_application.delete()
        return redirect('list_job_application')
      

    return render(request,'delete.html',{'job_application': job_application}) 


#CRUD for Notification Model----------------------------------------------------------------------------------------------

def list_notification(request):
    notifications = Notification.objects.all()
    return render(request,'notificaton.html',{'notifications':notifications}) 


def create_notification(request):
    if request.method == 'POST':
            senderid = int(request.POST.get('senderid'))
            uid = int(request.POST.get('uid'))
            status  = int(request.POST.get('status'))
            title = request.POST.get('title')
            message = request.POST.get('message')
            isread = int(request.POST.get('isread'))
            

            obj = User.objects.create(
               senderid = senderid,
               uid = uid,
               status = status ,
               title = title,
               message = message,
               isread = isread,
            )
            
            return redirect('list_notification')
    else:
         return render(request,'forms/notification.html') 


def update_notification(request,id):

    
    notification  = Notifiaction.objects.get(id=id)

    

    if request.method == 'POST':
            notification.senderid = int(request.POST.get('senderid'))
            notification.uid = int(request.POST.get('uid'))
            notification.status  = int(request.POST.get('status'))
            notification.title = request.POST.get('title')
            notification.message = request.POST.get('message')
            notification.isread = int(request.POST.get('isread'))
            notification.save()

            return redirect('list_notification')


    return render(request,'forms/user.html',{'notification':notification})



def delete_notification(request,id):
     
    notification = Notification.objects.get(id=id)
     
    if request.method == 'POST':
        notification.delete()
        return redirect('list_notification')
      

    return render(request,'delete.html',{'notification': notification}) 


#CRUD for Job Model----------------------------------------------------------------------------------------------

def list_job(request):
    jobs = Job.objects.all()
    return render(request,'job.html',{'jobs':jobs}) 


def create_job(request):
    if request.method == 'POST':
           jbtype = int(request.POST.get('jbtype'))
           title = request.POST.get('title')
           description = request.POST.get('description')
           budgetmin = double(request.POST.get('budgetmin'))
           budgetmax = double(request.POST.get('budgetmax'))
           isawarded = int(request.POST.get('isawarded'))
           duration =  int(request.POST.get('duration'))
           startdate = request.POST.get('startdate')
           enddate = request.POST.get('enddate')
           awarddate = request.POST.get('awarddate')

           obj = Job.objects.create(
               jbtype = jbtype,
               title = title,
               description = description,
               budgetmin = budgetmin,
               budgetmax = budgetmax,
               isawarded = isawarded,
               duration = duration,
               startdate = startdate,
               enddate = enddate,
               awarddate = awarddate,
               )
           return redirect('list_job')
    else:
         return render(request,'forms/job.html') 


def update_job(request,id):
     
    job  = Job.objects.get(id=id)   

    if request.method == 'POST':
           job.jbtype = int(request.POST.get('jbtype'))
           job.title = request.POST.get('title')
           job.description = request.POST.get('description')
           job.budgetmin = double(request.POST.get('budgetmin'))
           job.budgetmax = double(request.POST.get('budgetmax'))
           job.isawarded = int(request.POST.get('isawarded'))
           job.duration =  int(request.POST.get('duration'))
           job.startdate = request.POST.get('startdate')
           job.enddate = request.POST.get('enddate')
           job.awarddate = request.POST.get('awarddate') 
           job.save()

           return redirect('list_job')

    return render(request,'forms/job.html',{'job': job})



def delete_job(request,id):
     
    job = Job.objects.get(id=id)
     
    if request.method == 'POST':
        job.delete()
        return redirect('list_job')
      

    return render(request,'delete.html',{'job': job}) 

#CRUD for Admin ------------------------------------------------------------------------------------------------
def ListAdmin(request):
    admin = Admin.objects.all()
    return render(request,'admin.html',{'admins':admin}) 

def CreateAdmin(request):
    if request.method == 'POST':
           username      = request.POST.get('username')
           plainpassword = request.POST.get('password')
           admintype     = int(request.POST.get('admintype'))
           status        =  int(request.POST.get('status'))
           secret       =  secretGenerator()
           password     = hashPassword(plainpassword + secret)

           


           obj = Admin.objects.create(
               username = username,
               password = password,
               secret= secret,
               admintype = admintype,
               status = status,
               )
           return redirect('ListAdmin')
    else:
         return render(request,'forms/user.html') 

def UpdateAdmin(request,id):
    admin  = Admin.objects.get(id=id)
    if request.method == 'POST':
           username      = request.POST.get('username')
           plainpassword = request.POST.get('password')
           admintype     = int(request.POST.get('admintype'))
           status        =  int(request.POST.get('status'))
           secret        = admin.secret
           password      = hashPassword(plainpassword + secret)

           admin.save()

           return redirect('ListAdmin')


    return render(request,'forms/admin.html',{'admin':admin})  

def DeleteAdmin(request,id):
    
    admin = Admin.objects.get(id=id)
     
    if request.method == 'POST':
        admin.delete()
        return redirect('ListAdmin')
      

    return render(request,'admin.html',{'admin': admin}) 

#login,logout,auth----------------------------------------------------------------------------------------------
def login(request):
     return render(request,'login/index.html')


def dashboard(request):
    user = User.objects.count()
    admin = Admin.objects.count()
    context = {
     "user":user,
     "admin":admin,
    }
    return render(request,'dashboard/index.html',context) 


def logout(request):
     AuthLogOut(request)
     msg = "You Have successfully log out"
     messages.success(request,msg,extra_tags="success")
     return redirect('login')

def auth(request):
    if request.method == 'POST':
           username      = request.POST.get('username')
           plainpassword = request.POST.get('password')
    try :   
            user = Admin.objects.get(username=username)

            secret = user.secret
           
            passwordConfirm = hashPassword(plainpassword+secret)


            if passwordConfirm == user.password :
              return redirect('dashboard')
              pass
        
            else:
               errormsg = "Invalid Username or Password"
               messages.error(request,errormsg)
               return redirect('login')
               pass
    except ObjectDoesNotExist:

               errormsg = "Invalid Username or Password"
               messages.error(request,errormsg)
               return redirect('login')
               pass

    else:
         return redirect('login')
def secretGenerator():
    letters = string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(10))


def hashPassword(word):
    password = hashlib.sha256(word.encode()).hexdigest()
    return password






  



