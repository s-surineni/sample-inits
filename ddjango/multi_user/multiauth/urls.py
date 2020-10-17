from django.urls import include, path

from multiauth import views


urlpatterns = [
    path('', views.home, name='home'),

]
