from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomePage(View):
    def get(request):
        return render('first.html')