from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from . import models
from .models import *

# Create your views here.

def connexion(request):
    return render(request, 'pages/login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'pages/index.html')

def islogin(request,):
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = postdata['name']

    username = postdata['username']
    password = postdata['password']
    isSuccess=False

    user = authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        print("user is login")
        isSuccess = True
        login(request, user)
        datas = {
        'success':True,
        'username':username,
        'message':'Votre connection a reussi avec succes',
    }
        return JsonResponse(datas,safe=False) # page si connect
        
    else:
        data = {
        'success':False,
        'message':'Vos identifiants ne sont pas correcte',
        }
        return JsonResponse(data,safe=False)
    
    
    
    return JsonResponse(datas, safe=False)

@login_required(login_url='login')
def profil(request):
    return render(request, 'pages/profil.html')

@login_required(login_url='login')
def quizz(request):
    return render(request, 'pages/quizz.html')

@login_required(login_url='login')
def epreuve(request):
    return render(request, 'pages/epreuve.html')

@login_required(login_url='login')
def lesson(request):
    return render(request, 'pages/lesson.html')

@login_required(login_url='login')
def pdf(request):
    return render(request, 'pages/pdf.html')

def deconnexion(request):
    logout(request)

    return redirect('login')