from django.shortcuts import render,redirect
from .models import *
import bcrypt
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

# Create your views here.


def index(request):
    try:
        std=request.session['std']
    except:
        std=False
    return render(request,'index.html',{'std':std})

def contact(request):
    if request.method=='POST':
        name=request.POST['Name']
        subject=request.POST['Subject']
        messege=request.POST['messege']
        c_date=datetime.now().date()
        c_time=datetime.now().time()
        data=messeges.objects.create(name=name,subject=subject,messege=messege,date=c_date,time=c_time)
        data.save()
        print(messege)
    return render(request,'contact.html')



#Student


def st_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        psw=password.encode('utf-8')
        print(password,username)
        try:
            student=Student.objects.get(stregno=username)
            if bcrypt.checkpw(psw,student.stpassword.encode('utf-8')):
                    request.session['std']=student.stname
                    print("logged in ")
                    if student.setnewpsw==True:
                        return redirect(index)
                    else:
                        return redirect(studentnewpassword)
            else:
                    print('error')
                    messages.add_message(request,messages.INFO, "Incorrect Password" ,extra_tags="danger")
        except:
            messages.add_message(request,messages.INFO, "Incorrect Username or Password" ,extra_tags="danger")

    return render(request,'student/student_login.html')

def st_logout(request):
    if 'std' in request.session:
        del request.session['std']
        return redirect(index)
    else:
        return render(index)
    

def studentnewpassword(request):
    if 'std' in request.session:
        if request.method=='POST':
            password=request.POST['password']
            cnfpassword=request.POST['cnfpassword']
            # student=Student.objects.get(stname=request.session['std'])
            if password==cnfpassword:
                psw=password.encode('utf-8')
                salt=bcrypt.gensalt()               #Password Hashing
                psw_hashed=bcrypt.hashpw(psw,salt)  
                Student.objects.filter(stname=request.session['std']).update(stpassword=psw_hashed.decode('utf-8'),setnewpsw=True)
                return redirect(index)
            else:
                messages.add_message(request,messages.INFO, "Password dosent match" ,extra_tags="danger")
                
        return render(request,'student/studentnewpassword.html')
    else:
        return redirect(index)
def stexamresultview(request):
    if 'std' in request.session:
        try:
            std=request.session['std']
        except:
            std=False
        sems=Sem.objects.all()
        if request.method=='POST':
            sem=request.POST['sem']
            examresult=Semexam.objects.filter(stud=Student.objects.get(stname=request.session['std']),sem=sem)

        else:
            semexam=Semexam.objects.filter(stud=Student.objects.get(stname=request.session['std']))
            sem=[]
            for i in semexam:
                sem.append(i.sem.semno)
            bigsem=max(sem)
            # print(bigsem)
            ssem=Sem.objects.get(semno=bigsem)
            examresult=Semexam.objects.filter(stud=Student.objects.get(stname=request.session['std']),sem=ssem)
    return render(request,'student/stexamresultview.html',{'std':std,'examresult':examresult,'sems':sems})
def stud_forgotpassword(request):
    return render(request,'')


#Admin


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
        return render(request,'admin/admin_index.html',{'adm':adm,'msg_count':countmsg(request)})
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

def countmsg(request):
    u_msgs=messeges.objects.filter(read=False)
    msg_len=len(u_msgs)
    return msg_len
def admin_viewmessege(request):
    if 'adm' in request.session:
        messege=messeges.objects.all()
        messeges.objects.update(read=True)
        print(messege)
    return render(request,'admin/admin_viewmesseges.html',{'messeges':messege})



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
            psw=stadmno.encode('utf-8')
            salt=bcrypt.gensalt()               #Password Hashing
            psw_hashed=bcrypt.hashpw(psw,salt)
            data=Student.objects.create(staffname=Staff.objects.get(staffname=request.session['stf']),stname=stname,stphno=stphno,stregno=stregno,stadmno=stadmno,bname=branch,ssem=sem,stemail=stemail,staddress=staddress,stpassword=psw_hashed.decode('utf-8'))
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
    if 'stf' in request.session:
        sem=Sem.objects.all()
        staff=Staff.objects.get(staffname=request.session['stf'])
        if request.method=='POST':
            ssem=request.POST['sem']
            examresult=Semexam.objects.filter(staffname=staff,sem=ssem)
            # print(examresult)
        else:
            examresult=Semexam.objects.filter(staffname=staff)
    return render(request,'staff/examviewresult.html',{'sem':sem,'examresult':examresult})

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

def staffforgetpswmail(request):
    if request.method=='POST':
        email=request.POST['email']
        try:
            data=Staff.objects.get(staffemail=email)
            # request.session['cngpsw']=data.staffname
            subject='CMS Forgot password'
            path="http://127.0.0.1:8000/staffnewpassword"
            message = f"To set new password click the link below!!\n\n {path}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list= [data.staffemail,]
            send_mail(subject,message,email_from,recipient_list)
            request.session['newpsw']=data.staffemail
            messages.success(request,"Email sent ! ")
        except:
            messages.success(request,"Email doesn't match ! ")
    return render(request,'staff/staffforgetpswmail.html')

def staffnewpassword(request):
    # if 'newpsw' in request.session:
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        cnf_password=request.POST['cnf_password']
        psw=password.encode('utf-8')
        salt=bcrypt.gensalt()               #Password Hashing
        psw_hashed=bcrypt.hashpw(psw,salt)
        if password==cnf_password:
            try:
                data=Staff.objects.filter(staffemail=email).update(staffpassword=psw_hashed.decode('utf-8'))
                print(data)
                messages.success(request,"Password Changed Sucessfully")
            except:
                messages.warning(request,"User assosiated to this mail does't exist")
        else:
                messages.warning(request, "Passwords Doesn't match!!")




    return render(request,'staff/staffnewpassword.html')