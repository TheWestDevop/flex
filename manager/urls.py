from django.urls import path
from manager.views import *

urlpatterns = [
    #path('dashboard/',dashboard,name="dashboard"),
    #path('login/',login,name="login"),
    #path('auth/',auth,name="auth"),
    #path('logout',logout,name="logout"),
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
]