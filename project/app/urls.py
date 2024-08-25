from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),


    #Student
    path('st_login',views.st_login),

    #Staff
    path('staff',views.staff_login),

    #Admin
    path('admin',views.admin_login),
]