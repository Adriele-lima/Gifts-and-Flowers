from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import Product
from profiles.models import User


def view_wishlist(request):
    """ A view to return wishlist page """

    if request.user.is_authenticated:
        wishlist = Product.objects.filter(user_wishlist=request.user)

        context = {
            'wishlist': wishlist
        }
    else:
        messages.error(request, 'Sorry, only authenticated users can do that.')
        return redirect('account_signup')

    return render(request, 'wishlist/wishlist.html', context)
