from django.shortcuts import render,redirect
from .models import *
import bcrypt
# Create your views here.

def index(request):
    # print(request.session['adm'])
    return render(request,'index.html')

def st_login(request):
    return render(request,'student/student_login.html')

def staff_login(request):
    return render(request,"staff/staff_login.html")

def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        psw=password.encode('utf-8')
        salt=bcrypt.gensalt()               #Password Hashing
        psw_hashed=bcrypt.hashpw(psw,salt)
        adm=admins.objects.get(username=username)
        if bcrypt.checkpw(psw,adm.password.encode('utf-8')):
                request.session['adm']=adm.username
                    # messages.success(request, "Login successfully completed!") 
                return redirect(admin_index)
    return render(request,'admin/admin_login.html')

def admin_index(request):
    if 'adm' in request.session:
        adm=admins.objects.get(username=request.session['adm'])
        return render(request,'admin/admin_index.html',{'adm':adm})
    else:
         return redirect(index)

def admstaff(request):
    if 'adm' in request.session:
        return render(request,'admin/admstaff.html')
    else:
        return render(index)
    
def addstaff(request):
    if 'adm' in request.session:
        return render(request,'admin/addstaff.html')
    else:
        return redirect(index)

def addbranch(request):
    if 'adm' in request.session:
        return render(request,'addbranch.html')
    else:
        return redirect(index)
    