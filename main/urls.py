from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('participants/', views.Participants.as_view(), name='participants'),
    path('journal/', views.Journal.as_view(), name='journal'),
    path('resources/', views.Resources.as_view(), name='resources'),
]
