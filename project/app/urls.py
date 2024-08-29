from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),


    #Student
    path('st_login',views.st_login),

    #Staff
    path('staff',views.staff_login),
    path('staffindex',views.staffindex),
    path('addstudents',views.addstudents),
    path('staff_viewstudents',views.staff_viewstudents),
    path('admsubjects',views.admsubjects),
    path('viewsubjects',views.viewsubjects),
    path('examviewresult',views.examviewresult),
    path('examaddresult',views.examaddresult),
    
    #Admin
    path('admin_login',views.admin_login),
    path('admin_index',views.admin_index),
    path('admstaff',views.admstaff),
    path('addstaff',views.addstaff),
    path('addbranch',views.addbranch),
    path('admbranch',views.admbranch),
    path('deletebranch/<pk>',views.deletebranch),
    path('viewstudents',views.viewstudents),
    path('deletestudent/<pk>',views.deletestudent),

]