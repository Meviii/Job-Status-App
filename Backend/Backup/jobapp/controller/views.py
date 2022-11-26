from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the jobapp home.")

def user(request):
    return HttpResponse("This will return a list of users")