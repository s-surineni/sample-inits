from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic import TemplateView, CreateView

from multiauth.forms import StudentSignUpForm
from multiauth.models import User

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    return HttpResponse('Hello')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def from_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect('students:quiz_list')
        return redirect('home')

def teacher_signup(request):
    return HttpResponse('Hello')
