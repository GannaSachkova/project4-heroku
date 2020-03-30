from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """
    A view to ensure that payment information is being handled 
    by stripe correctly, so that the user will be able to purchase 
    items. The view renders the html page
    and pass in the forms and contents of the cart. 
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # print(payment_form.cleaned_data['stripe_id'])

        # payment_form.data.stripe_id=[stripe.api_key]
        payment_form.data._mutable = True
        payment_form.data['stripe_id'] = settings.STRIPE_SECRET
        #import pdb;  pdb.set_trace()
        # if the order form and the payment form is valid, filled out correctly, then the order form will be saved as order.
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cr_number = str(payment_form.cleaned_data['credit_card_number'])
            exp_date = int(payment_form.cleaned_data['expiry_month'])
            exp_year = int(payment_form.cleaned_data['expiry_year'])
            cvc = str(payment_form.cleaned_data['cvv'])
            # get the information from the cart from the current session, about what is being purchased.
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity[0] * product.price


                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity[0]
                )
                
                order_line_item.save()

            # a try except that will create a customer charge, using Stripe's in-built API.
            try:
                token = stripe.Token.create(
                    card={
                          "number": cr_number,
                          "exp_month": exp_date,
                          "exp_year": exp_year,
                          "cvc": cvc
                    },
                )
                customer = stripe.Charge.create(	
                    amount = int(total * 100),	
                    currency = "eur",	
                    source = token,
                    description = "desc"                   
                )

            # If the card is being declined.    
            except stripe.error.CardError as e:
                messages.error(request, "Your card was declined!")
            # if the customer have paid, request the cart from the current session.
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            # if the user have not paid.
            else:
                messages.error(request, "Unable to take payment")
        # if any payment form errors occurs.
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    # return a payment form and an order form as blank
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    # return the checkout html with an order form, a payment form, and a publishable key for Stripe, 
    # available on the HTML page when the user clicks on checkout.
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
