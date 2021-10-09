from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [path("signup/", views.signup), path("home", views.home, name="home")]
