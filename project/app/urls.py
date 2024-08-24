from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('st_login',views.st_login),
]