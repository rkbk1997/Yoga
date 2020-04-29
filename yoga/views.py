from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

from .models import *

# Create your views here.
def indexpage(request):
    data=routen.objects.all()
    abdata=about.objects.all()
    fdata=feedback.objects.all()
    cdata=classes.objects.all()
    data1=contactme.objects.all()
    return render(request,'index.html',{'data':data,'abdata':abdata,'fdata':fdata,'cdata':cdata,'data1':data1})

def aboutpage(request):
    fdata=feedback.objects.all()
    abdata=about.objects.all()
    data1=contactme.objects.all()
    return render(request,'about.html',{'fdata':fdata,'abdata':abdata,'data1':data1})

def schedule(request):
    data=routen.objects.all()
    abdata=about.objects.all()
    data1=contactme.objects.all()
    return render(request,'schedule.html',{'data':data,'abdata':abdata,'data1':data1})

def trainers(request):
    data=trainerdata.objects.all()
    abdata=about.objects.all()
    data1=contactme.objects.all()
    return render(request,'trainers.html',{'data':data,'abdata':abdata,'data1':data1})

def contact(request):
    abdata=about.objects.all()
    data1=contactme.objects.all()
    return render(request,'contact.html',{'abdata':abdata,'data1':data1})

def courses(request):
    cdata=classes.objects.all()
    abdata=about.objects.all()
    data1=contactme.objects.all()
    return render(request,'courses.html',{'cdata':cdata,'abdata':abdata,'data1':data1})

def main(request):
    return render(request,'main.html',{})

def timetable(request):
    if request.method=='POST':
        course=request.POST["course"]
        mon=request.POST["mon"]
        tue=request.POST["tue"]
        wed=request.POST["wed"]
        thu=request.POST["thu"]
        fri=request.POST["fri"]
        sat=request.POST["sat"]
        sun=request.POST["sun"]
        routen.objects.create(course=course,mon=mon,tue=tue,wed=wed,thu=thu,fri=fri,sat=sat,sun=sun)
        return redirect('timetable')
    return render(request,'timetable.html',{})

def viewruetine(request):
    data=routen.objects.all()
    
    return render(request,'viewruetine.html',{'data':data})

def Login(request):
    error=False
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('main')
        else:
            error=True
    return render(request,'login.html',{"error":error})

def Logout(request):
	logout(request)
	return redirect('index')

def Edit_Delete_timetable(request,sid,option):
    data=routen.objects.filter(id=sid).first()
    if option=='Delete':
        data.delete()
        return redirect('viewruetine')
    if option =='Edit':
        if request.method=='POST':
            data.course=request.POST['course']
            data.mon=request.POST['mon']
            data.tue=request.POST['tue']
            data.wed=request.POST['wed']
            data.thu=request.POST['thu']
            data.fri=request.POST['fri']
            data.sat=request.POST['sat']
            data.sun=request.POST['sun']
            data.save()
            return redirect('viewruetine')
        return render(request,'viewruetine.html',{'data':data})

def aboutview(request):
    data=about.objects.all()
    return render(request,'aboutview.html',{'data':data})

def Edit_Delete_about(request,sid,option):
    data=about.objects.filter(id=sid).first()
    if option =='Edit':
        if request.method=='POST':
            data.des=request.POST['des']
            data.save()
            return redirect('aboutview')
        return render(request,'aboutview.html',{'data':data})