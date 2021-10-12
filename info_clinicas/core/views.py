from django.shortcuts import render


def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'core.html')
