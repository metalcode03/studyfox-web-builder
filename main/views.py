from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def preference(request):
    return render(request, 'main/preference.html')