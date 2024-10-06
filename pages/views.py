from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import messages
from .models import *


def home(request, *args, **kwargs):
    return render(request,"home.html")

def privacy(request, *args, **kwargs):
    return render(request,"privacy.html")

def donations(request, *args, **kwargs):
    return render(request,"donations.html")

def cancellation(request, *args, **kwargs):
    return render(request,"cancellation.html")