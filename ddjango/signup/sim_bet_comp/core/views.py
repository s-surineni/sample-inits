from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.http import HttpResponse
from django.shortcuts import redirect, render


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    # return render(request, 'core/signup.html', {'form': form})
    return render(request, 'core/signup2.html', {'form': form})


def home(request):
    welcome = 'Welcome {}'.format(request.user)
    return HttpResponse(welcome)
