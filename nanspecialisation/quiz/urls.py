from django.urls import path

from . import views

urlpatterns = [
    path('', views.connexion, name='login'),
    
    path('post', views.islogin, name='login_request'),
    path('home', views.home, name='home'),
    path('profil', views.profil, name='profil'),
    path('quizz', views.quizz, name='quizz'),
    path('epreuve', views.epreuve, name='epreuve'),
    path('lesson', views.lesson, name='lesson'),
    path('pdf', views.pdf, name = 'pdf'),
    
    path('deconnexion', views.deconnexion, name='deconnexion'),
]
