from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

def home(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)
