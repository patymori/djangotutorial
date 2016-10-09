from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>Django</h1><h3>Bem-vindo ao .NET Coders!</h3>')
    return render(request, 'index.html')
