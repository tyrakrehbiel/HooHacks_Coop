from django.urls import path
from . import views

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
     path('about/', views.about, name='about'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)