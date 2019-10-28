from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from .emails import send_welcome_email
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

            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            recipient=User(username=username,email=email)
            try:
                send_welcome_email(username,email)
                messages.success(request, f'Account has been created successfully!')
            except:
                print('error')
            return redirect('/login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)




def search_business(request):
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET["business"]
        searched_business = Business.search_by_id(search_term)
        message = f'search_term'
        context = {
            "business":searched_business,
            "message":message,

        }
        return render(request, 'search.html', context)
    else:
        message = "You haven't searched for any user"
        context = {
            "message":message,
        }
        return render(request, 'search.html', context)
