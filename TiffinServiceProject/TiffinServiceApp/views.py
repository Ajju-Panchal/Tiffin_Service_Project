from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'index.html')