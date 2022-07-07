from django.shortcuts import render

# Create your views here.
def sizing(request):
    """
    A view to return the sizing page
    """
    return render(request, 'sizing/sizing.html')