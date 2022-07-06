from django.shortcuts import render

# Create your views here.
def returns(request):
    """
    A view to return the returns page
    """
    return render(request, 'returns/returns.html')