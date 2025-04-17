from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request,"website/base.html")

def about(request):
    return HttpResponse("Hello You are In about Us page ")

def contect(request):
    return HttpResponse("Hello You are In contect Us page ")