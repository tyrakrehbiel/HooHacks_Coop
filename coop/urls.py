from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('notes/', views.notes_list, name='notes_list'),
    path('notes/upload_note/', views.upload_note, name='upload_note'),
    path('notes/<int:pk>/', views.delete_note, name='delete_note')
]
