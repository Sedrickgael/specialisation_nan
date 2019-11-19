from django.urls import path
from . import views



urlpatterns = [
    path('', views.islogin, name = 'home'),
    path('index', views.index, name = 'index'),
    path('coding', views.coding, name = 'coding'),
    path('epreuve', views.epreuve, name = 'epreuve'),
    path('lesson', views.lesson, name = 'lesson'),
    path('pdf', views.pdf, name = 'pdf'),
    path('profil', views.profil, name = 'profil'),
    path('quizz', views.quizz, name = 'quizz'),
]

