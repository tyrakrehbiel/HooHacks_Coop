from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'coop/index.html'), name='coop-home'),
    #path('', include('coop.urls')),
    # path('coop/', include('coop.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
