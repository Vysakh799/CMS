from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def st_login(request):
    return render(request,'student/student_login.html')

def staff_login(request):
    return render(request,"staff/staff_login.html")

def admin_login(request):
    return render(request,'admin/admin_login.html')