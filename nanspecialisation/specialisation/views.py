from django.shortcuts import render

# Create your views here.


def islogin(request):
    return render(request, 'pages/login.html')

def index(request):
    return render(request, 'pages/index.html')

def coding(request):
    return render(request, 'pages/coding.html')

def epreuve(request):
    return render(request, 'pages/epreuve.html')

def lesson(request):
    return render(request, 'pages/lesson.html')

def pdf(request):
    return render(request, 'pages/pdf.html')

def profil(request):
    return render(request, 'pages/profil.html')

def quizz(request):
    return render(request, 'pages/quizz.html')