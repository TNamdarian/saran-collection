from django.shortcuts import render


def sizing(request):
    """
    A view to return the sizing page
    """
    return render(request, 'sizing/sizing.html')