from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . forms import SignUpForm
from . models import User


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('admin')

signup = SignUpView.as_view()

