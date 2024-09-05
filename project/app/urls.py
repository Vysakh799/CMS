from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('contact',views.contact),

    #Student
    path('st_login',views.st_login),
    path('studentnewpassword',views.studentnewpassword),
    path('st_logout',views.st_logout),
    path('stexamresultview',views.stexamresultview),
    path('std_frgtmail',views.std_frgtmail),
    path('studforgotpassword',views.studforgotpassword),

    #Staff
    path('staff',views.staff_login),
    path('staffindex',views.staffindex),
    path('addstudents',views.addstudents),
    path('staff_viewstudents',views.staff_viewstudents),
    path('admsubjects',views.admsubjects),
    path('viewsubjects',views.viewsubjects),
    path('examviewresult',views.examviewresult),
    path('examaddresult',views.examaddresult),
    path('staffforgetpswmail',views.staffforgetpswmail),
    path('staffnewpassword',views.staffnewpassword),
    path('staff_logout',views.staff_logout),
    
    #Admin
    path('admin_login',views.admin_login),
    path('admin_index',views.admin_index),
    path('admstaff',views.admstaff),
    path('addstaff',views.addstaff),
    path('addbranch',views.addbranch),
    path('admbranch',views.admbranch),
    path('deactivebranch/<pk>',views.deactivebranch),
    path('activebranch/<pk>',views.activebranch),
    path('viewstudents',views.viewstudents),
    path('deletestudent/<pk>',views.deletestudent),
    path('admin_viewmessege',views.admin_viewmessege),
    path('deactivestaff/<pk>',views.deactivestaff),
    path('activestaff/<pk>',views.activestaff),
    path('adm_logout',views.adm_logout),

]