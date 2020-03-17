from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Stock

# class created following instructions by Antonio Mele
# in the book Django By Example
class Cart(object):
    def __init__(self, request):
        # initialize the cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = []
        self.cart = cart

  

    def remove(self, product_id, size):
        # remove the product from the cart
        for item in self.cart:
            if item['product_id'] == product_id and str(item['size']) == size:
                self.cart.remove(item)
        self.save()
