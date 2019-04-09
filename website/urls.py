from django.urls import path
from manager.views import create_user,list_user,update_user,delete_user

urlpatterns = [
    path('',list_user,name="list_user"),
    path('new/',create_user,name="create_user"),
    path('update/<int:id>/',update_user,name="update_user"),
    path('delete/<int:id>/',delete_user,name="delete_user"),
]

    