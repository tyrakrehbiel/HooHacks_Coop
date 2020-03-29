from django.urls import path
from . import views

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.notes_list, name='notes_list'),
    path('notes/<int:pk>/', views.delete_note, name='delete_note'),

    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),

    path('profile/', views.profile, name='profile'),
    path('profile/upload/', views.upload_note, name='upload_note'),
    # path('profile/myNotes/', views.),
    path('profile/settings/', views.settings, name='settings'),
    
    path('feed/', views.feed, name='feed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
