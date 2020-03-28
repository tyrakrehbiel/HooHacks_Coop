from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
]