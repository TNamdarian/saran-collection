from django.shortcuts import render


def shipping(request):
    """
    A view to return the shipping page
    """
    return render(request, 'shipping/shipping.html')