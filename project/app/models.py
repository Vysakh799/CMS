from django.db import models
from django.utils import timezone
# Create your models here.
 
class admins(models.Model):
    username=models.TextField()
    password=models.TextField()
    Cad1=models.FileField(null=True)
    Cad2=models.FileField(null=True)
    Cad3=models.FileField(null=True)

class Branches(models. Model):
    aname=models.ForeignKey(admins,on_delete=models.CASCADE)
    bname=models.TextField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.bname

class Staff(models.Model):
    aname=models.ForeignKey(admins,on_delete=models.CASCADE)
    staffname=models.TextField()
    staffemail=models.TextField()
    staffphno=models.TextField()
    staffaddress=models.TextField()
    staffbranch=models.ForeignKey(Branches,on_delete=models.CASCADE)
    staffpassword=models.TextField()
    status=models.BooleanField(default=True)


    def __str__(self):
        return self.staffname

class Sem(models.Model):
    semno=models.TextField()
    def __str__(self):
        return self.semno

class Subject(models.Model):
    bname=models.ForeignKey(Branches,on_delete=models.CASCADE)
    sem=models.ForeignKey(Sem,on_delete=models.CASCADE)
    subjectname=models.TextField()

    def __str__(self):
        return self.subjectname

class Student(models.Model):
    staffname=models.ForeignKey(Staff,on_delete=models.CASCADE)
    bname=models.ForeignKey(Branches,on_delete=models.CASCADE)
    ssem=models.ForeignKey(Sem,on_delete=models.CASCADE)
    stname=models.TextField()
    stregno=models.TextField()
    stadmno=models.TextField()
    stemail=models.TextField()
    stphno=models.TextField()
    staddress=models.TextField()
    stpassword=models.TextField(null=True)
    setnewpsw=models.BooleanField(default=False)
    

    def __str__(self):
        return self.stname

class Semexam(models.Model):
    sem=models.ForeignKey(Sem,on_delete=models.CASCADE)
    subname=models.ForeignKey(Subject,on_delete=models.CASCADE)
    stud=models.ForeignKey(Student,on_delete=models.CASCADE)
    mark=models.IntegerField()
    bname=models.ForeignKey(Branches,on_delete=models.CASCADE)
    staffname=models.ForeignKey(Staff,on_delete=models.CASCADE)
    
class messeges(models.Model):
    name=models.TextField()
    time=models.TimeField()
    date=models.DateField()
    subject=models.TextField()
    messege=models.TextField()
    read=models.BooleanField(default=False)

