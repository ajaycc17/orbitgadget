from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectHome, name='projectHome'),
    path('password-generator/', views.passGen, name='passGen'),
    path('drum-kit/', views.drumkit, name='drumkit'),
    path("wordcounter/", views.wordcounter, name="wordcounter"),
]