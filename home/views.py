from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    A view to return the home page
    """
    return render(request, 'pages/index.html')