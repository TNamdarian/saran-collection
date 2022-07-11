from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


def index(request):
    """
    A view to return the home page
    """
    products = Product.objects.order_by('-rating')[:6]

    context = {
        'products': products,
    }

    return render(request, 'pages/index.html', context)