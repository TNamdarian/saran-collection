from django.shortcuts import render

# Create your views here.
def shipping(request):
    """
    A view to return the shipping page
    """
    return render(request, 'shipping/shipping.html')