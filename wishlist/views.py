from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import WishList


def view_wishlist(request):
    """ A view to return wishlist page """

    return render(request, 'wishlist/wishlist.html')
