from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name='account_app/login.html'
    success_url=reverse_lazy('naval_app/buque_list.html')
