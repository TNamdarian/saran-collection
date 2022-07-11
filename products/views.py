from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Category
from django.db.models import Q
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DeleteView,
)


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        if 'q' in request. GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search ceriteria!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    product = get_object_or_404(Product, pk=product_id)

    print(product.category)

    context = {
        'product': product,
        'category' : product.category
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'You need to have the correct '
                       'permissions to manage product details')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
        
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


class DeleteProductView(LoginRequiredMixin, DeleteView, UserPassesTestMixin,
                        SuccessMessageMixin):
    """
    This renders the page to delete a product. This is to bring in defensive
    coding to make sure user wants to delete a product. On deletion there
    is feedback with a success message with SuccessMessageMixin. Use of
    LoginRequiredMixin to access this page, a user needs to be logged in. Use
    of UserPassesTestMixin to limit access to logged-in users that pass a test
    namely, they should have created the product or they are an admin user. Use
    of DeleteView which is built-in Django to assist with deleting.
    """
    model = Product
    template_name = "products/delete_product.html"
    success_message = "The Product was successfully deleted."
    success_url = reverse_lazy('products')

    # User permissions: https://bit.ly/3mSsegO
    def test_func(self):
        """
        This is to set the paramaters for UserPassesTestMixin so that only
        users who created the product or if they are an admin user can delete
        a product.
        """
        if self.request.user.is_superuser:
            return True
        return False

    # Success message in DeleteView: https://bit.ly/3oRYlzG
    def delete(self, request, *args, **kwargs):
        """
        This renders a feedback success message related to SuccessMessageMixin
        once the product is successfully deleted.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteProductView, self).delete(request, *args, **kwargs)