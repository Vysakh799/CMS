from django.db import models
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


class Staff(models.Model):
    aname=models.ForeignKey(admins,on_delete=models.CASCADE)
    staffname=models.TextField()
    staffemail=models.TextField()
    staffphno=models.TextField()
    staffaddress=models.TextField()
    staffbranch=models.ForeignKey(Branches,on_delete=models.CASCADE)
    staffpassword=models.TextField()

class Sem(models.Model):
    semno=models.TextField()

class Subject(models.Model):
    bname=models.ForeignKey(Branches,on_delete=models.CASCADE)
    sem=models.ForeignKey(Sem,on_delete=models.CASCADE)
    subjectname=models.TextField()

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

class Semexam(models.Model):
    sem=models.ForeignKey(Sem,on_delete=models.CASCADE)
    subname=models.ForeignKey(Subject,on_delete=models.CASCADE)
    stname=models.ForeignKey(Student,on_delete=models.CASCADE)
    mark=models.IntegerField()
    bname=models.ForeignKey(Branches,on_delete=models.CASCADE)
    


