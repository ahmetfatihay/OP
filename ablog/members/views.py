from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, PasswordChangingForm

class PasswordChangeView(PasswordChangeView):
    from_class = PasswordChangingForm
    #from_class = PasswordChangeForm
    success_url = reverse_lazy('password_success') 

def password_success(request):
    return render(request, 'registration/password_success.html',{})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
