from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login

def about(request):
    #return HttpResponse('hi there! Im Hello World!')
    return render(request , 'about.html')
def home(request):
    #return HttpResponse('Menu')
    return render(request , 'Home.html')
def login(request):
    return render(request , "login.html")
def register(request):
    return render(request , "register.html")
def rooms(request):
    return render(request , "rooms.html")
def notfound(request, exception):
    return render(request,'404.html')
