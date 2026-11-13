from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    return HttpResponse("Welcome to Menu Page! - Updated in development")