from django.shortcuts import render

def home(request):
    return render(request, 'blogapp/home.html')

def about(request):
    return render(request, 'blogapp/about.html')
# Create your views here.
