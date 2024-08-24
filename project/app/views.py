from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def st_login(request):
    return render(request,'student_login.html')