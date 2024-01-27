from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def HomePage(request):
    return render(request,'home.html')

def whiteBoard(request):
    return render(request,"board.html")