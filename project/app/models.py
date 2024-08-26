from django.db import models
# Create your models here.
 
class admins(models.Model):
    username=models.TextField()
    password=models.TextField()
    Cad1=models.FileField(null=True)
    Cad2=models.FileField(null=True)
    Cad3=models.FileField(null=True)

