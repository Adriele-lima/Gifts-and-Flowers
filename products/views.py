from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view that render all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """ A view that renders one product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)
