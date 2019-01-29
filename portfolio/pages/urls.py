"""from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]"""

from django.views.generic import TemplateView
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls import url


urlpatterns = [
    url('^$', TemplateView.as_view(template_name='index.html')),
]