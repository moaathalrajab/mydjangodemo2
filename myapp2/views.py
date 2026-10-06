from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, welcome to my django app!</h1>")
# new comment

