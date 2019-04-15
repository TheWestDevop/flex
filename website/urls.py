from django.urls import path
from manager.views import *

urlpatterns = [
   
    #admin path

    path('admin/',ListAdmin,name="ListAdmin"),
    path('admin/create',CreateAdmin,name="CreateAdmin"),
    path('admin/update/<int:id>/',UpdateAdmin,name="UpdateAdmin"),
    path('admin/delete/<int:id>/',DeleteAdmin,name="UpdateAdmin"),

    #user path
    path('user/',list_user,name="list_user"),
    path('user/create',create_user,name="create_user"),
    path('user/update/<int:id>/',update_user,name="update_user"),
    path('user/delete/<int:id>/',delete_user,name="delete_user"),


    #job path
    path('job/',list_job,name="list_job"),
    path('job/create',create_job,name="create_job"),
    path('job/update/<int:id>/',update_job,name="update_job"),
    path('job/delete/<int:id>/',delete_job,name="delete_job"),


    #JobType path
    path('jobtype/',list_jobtype,name="list_jobtype"),
    path('jobtype/create',create_jobtype,name="create_jobtype"),
    path('jobtype/update/<int:id>/',update_jobtype,name="update_jobtype"),
    path('jobtype/delete/<int:id>/',delete_jobtype,name="delete_jobtype"),


    #Notification
    path('notification/',list_notification,name="list_notification"),
    path('notification/create',create_notification,name="create_notification"),
    path('notification/update/<int:id>/',update_notification,name="update_notification"),
    path('notification/delete/<int:id>/',delete_notification,name="delete_notification"),


    #Transaction
    #path('transactions/',list_transaction,name="list_transaction"),

    #payment
    #path('payment/',list_payment,name="list_payment"),
    

]