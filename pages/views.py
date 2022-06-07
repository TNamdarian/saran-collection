from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    A view to return the index page
    """
    return render(request, 'pages/index.html')


def about(request):
    """
    A view to return the about page
    """
    return render(request, 'pages/about.html')