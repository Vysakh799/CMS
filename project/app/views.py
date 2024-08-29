from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    # print(request.session['adm'])
    return render(request,'index.html')

def st_login(request):

    return render(request,'student/student_login.html')



def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        psw=password.encode('utf-8')
        salt=bcrypt.gensalt()               #Password Hashing
        psw_hashed=bcrypt.hashpw(psw,salt)
        try:
            adm=admins.objects.get(username=username)
            if bcrypt.checkpw(psw,adm.password.encode('utf-8')):
                    request.session['adm']=adm.username
                        # messages.success(request, "Login successfully completed!") 
                    return redirect(admin_index)
        except:
            messages.add_message(request,messages.INFO, "Incorrect Username Or Password" ,extra_tags="danger")

    return render(request,'admin/admin_login.html')

def admin_index(request):
    if 'adm' in request.session:
        adm=admins.objects.get(username=request.session['adm'])
        return render(request,'admin/admin_index.html',{'adm':adm})
    else:
         return redirect(index)

def admstaff(request):
    if 'adm' in request.session:
        branches=Branches.objects.filter(aname=admins.objects.get(username=request.session['adm']))
        if request.method=='POST':
            branchname=request.POST['branch']
            print(branchname)
            branch=Branches.objects.get(bname=branchname)
            staffs=Staff.objects.filter(staffbranch=branch)
        else:
            staffs=Staff.objects.all()
        return render(request,'admin/admstaff.html',{'branches':branches,'staffs':staffs})
    else:
        return render(index)
    
def addstaff(request):
    if 'adm' in request.session:
        branches=Branches.objects.filter(aname=admins.objects.get(username=request.session['adm']))
        if request.method=='POST':
            staffname=request.POST['staffname']
            staffemail=request.POST['staffemail']
            staffphno=request.POST['staffphno']
            staffaddress=request.POST['staffaddress']
            staffbranch=request.POST['branch']
            bname=Branches.objects.get(bname=staffbranch)
            staffpassword=request.POST['staffpassword']
            psw=staffpassword.encode('utf-8')
            salt=bcrypt.gensalt()               #Password Hashing
            psw_hashed=bcrypt.hashpw(psw,salt)
            data=Staff.objects.create(aname=admins.objects.get(username=request.session['adm']),staffname=staffname,staffemail=staffemail,staffphno=staffphno,staffaddress=staffaddress,staffbranch=bname,staffpassword=psw_hashed.decode('utf-8'))
            data.save()
            subject='TDJ CMS'
            path="http://127.0.0.1:8000/staff"
            message = f"You have been Registered to the TDJ College CMS system\n\nUsername :{staffemail}\n\nPasssword: {staffpassword}\n\nTo login use this link \n\n{path}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list= [staffemail,]
            send_mail(subject,message,email_from,recipient_list)
            messages.success(request,"Email sent ! ")
        return render(request,'admin/addstaff.html',{'branches':branches})
    else:
        return redirect(index)


def addbranch(request):
    if 'adm' in request.session:
        adm=admins.objects.get(username=request.session['adm'])
        if request.method=='POST':
            bname=request.POST['branchname']
            data=Branches.objects.create(aname=adm,bname=bname)
            data.save()
        return redirect(admbranch)
    else:
        return redirect(index)


def admbranch(request):
    if 'adm' in request.session:
        # messages.warning(request,"Branch Deleted")
        data=Branches.objects.filter(aname=admins.objects.get(username=request.session['adm']))
        return render(request,'admin/addbranch.html',{'data':data})
    else:
        return redirect(index)
    
def deletebranch(request,pk):
    if 'adm' in request.session:
        Branches.objects.get(pk=pk).delete()
        messages.add_message(request,messages.INFO, "Branch Deleted" ,extra_tags="danger")
        return redirect(admbranch)
    else:
        return redirect(index)
    
def viewstudents(request):
    if 'adm' in request.session:
        staffs=Staff.objects.filter(aname=admins.objects.get(username=request.session['adm']))
        if request.method=='POST':
            staff=request.POST['staff']
            stf=Staff.objects.get(staffname=staff)
            data=Student.objects.filter(staffname=stf)
        else:
            data=Student.objects.all()
        return render(request,'admin/viewstudents.html',{'staffs':staffs,'data':data})
    else:
        return redirect(index)

def deletestudent(request,pk):
    if 'adm' in request.session:
        Student.objects.get(pk=pk).delete()
        messages.add_message(request,messages.INFO, "Student Deleted" ,extra_tags="danger")
        return redirect(viewstudents)
    else:
        return redirect(index)
    


#STAFF


def staff_login(request):
    if request.method=='POST':
        staffemail=request.POST['username']
        staffpassword=request.POST['password']
        psw=staffpassword.encode('utf-8')
        salt=bcrypt.gensalt()               #Password Hashing
        psw_hashed=bcrypt.hashpw(psw,salt)
        try:
            staff=Staff.objects.get(staffemail=staffemail)
            if bcrypt.checkpw(psw,staff.staffpassword.encode('utf-8')):
                    request.session['stf']=staff.staffname  
                        # messages.success(request, "Login successfully completed!") 
                    return redirect(staffindex)
        except:
            messages.add_message(request,messages.INFO, "Incorrect Username Or Password" ,extra_tags="danger")

    return render(request,"staff/staff_login.html")

def staffindex(request):
    if 'stf' in request.session:
        return render(request,'staff/staffindex.html')
    else:
        return redirect(index)

def addstudents(request):
    if 'stf' in request.session:
        sems=Sem.objects.all()
        branches=Branches.objects.all()
        if request.method=='POST':
            stname=request.POST['stname']
            stregno=request.POST['stregno']
            stadmno=request.POST['stadmno']
            bname=request.POST['branch']
            ssem=request.POST['sem']
            stphno=request.POST['stphno']
            stemail=request.POST['stemail']
            staddress=request.POST['staddress']
            branch=Branches.objects.get(bname=bname)
            sem=Sem.objects.get(semno=ssem)
            data=Student.objects.create(staffname=Staff.objects.get(staffname=request.session['stf']),stname=stname,stphno=stphno,stregno=stregno,stadmno=stadmno,bname=branch,ssem=sem,stemail=stemail,staddress=staddress)
            data.save()
            subject='TDJ College Of Engineering'
            path="http://127.0.0.1:8000/st_login"
            message = f"You have been Registered to the TDJ College Of Engineering\n\nUsername :{stregno}\n\nPasssword: {stadmno}\n\nTo login use this link \n\n{path}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list= [stemail,]
            send_mail(subject,message,email_from,recipient_list)
            messages.success(request,"Email sent ! ")
        return render(request,'staff/addstudents.html',{'sem':sems,'branches':branches})
    

def staff_viewstudents(request):
    staff=Staff.objects.get(staffname=request.session['stf'])
    students=Student.objects.filter(staffname=staff)
    return render(request,'staff/staff_viewstudents.html',{'students':students})


def admsubjects(request):
    if 'stf' in request.session:
        sems=Sem.objects.all()
        # branches=Branches.objects.all()
        staff=Staff.objects.get(staffname=request.session['stf'])
        if request.method=='POST':
            subject=request.POST['subjectname']
            sem=request.POST['sem']
            ssem=Sem.objects.get(semno=sem)
            data=Subject.objects.create(bname=staff.staffbranch,sem=ssem,subjectname=subject)
            data.save()
            messages.success(request,"Subject added")
    return render(request,'staff/admsubjects.html',{'sem':sems})

def viewsubjects(request):
    if 'stf' in request.session:
        sems=Sem.objects.all()
        # branches=Branches.objects.all()
        staff=Staff.objects.get(staffname=request.session['stf'])

        if request.method=="POST":
            sem=request.POST['sem']
            subjects=Subject.objects.filter(bname=staff.staffbranch,sem=Sem.objects.get(semno=sem))  
        else:
            subjects=Subject.objects.filter(bname=staff.staffbranch)
        return render(request,'staff/viewsubjects.html',{'sems':sems,'subjects':subjects})
    else:
        return redirect(index)

def examviewresult(request):

    return render(request,'staff/examviewresult.html')

def examaddresult(request):
    if 'stf' in request.session:
        sems=Sem.objects.all()
        staff=Staff.objects.get(staffname=request.session['stf'])
        students=Student.objects.filter(staffname=staff)
        subjects=Subject.objects.filter(bname=staff.staffbranch)
        if request.method=='POST':
            subjectname=request.POST['subjectname']
            mark=request.POST['mark']
            sem=request.POST['sem']
            regno=request.POST['stregno']
            bname=staff.staffbranch
            data=Semexam.objects.create(sem=Sem.objects.get(semno=sem),subname=Subject.objects.get(subjectname=subjectname),stud=Student.objects.get(stregno=regno),mark=mark,bname=bname,staffname=staff)
            data.save()
            messages.success(request,"Exam result added")

            # print(staff.staffbranch)
            # stname=request.POST[]
        return render(request,'staff/examaddresult.html',{'sem':sems,'regno':students,'subjects':subjects})
    else:
        return redirect(index)
