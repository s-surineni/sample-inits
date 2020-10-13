from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    return HttpResponse('Hello')


def student_signup(request):
    return HttpResponse('Hello')


def teacher_signup(request):
    return HttpResponse('Hello')
