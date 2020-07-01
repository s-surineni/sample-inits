from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('simple/', views.simple_upload, name='simple_upload'),
    url(r'^form/$', views.model_form_upload, name='model_form_upload'),
]
