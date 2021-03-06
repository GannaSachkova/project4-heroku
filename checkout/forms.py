from  django import forms
from .models import Order

class MakePaymentForm(forms.Form):

    """
    Payment form with payment details that the user have to insert to be able to checkout.
    """

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2038)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):

    """
    Order form to collect the shipping information for the order.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'town', 'street_address1', 'street_address2', 'county')
