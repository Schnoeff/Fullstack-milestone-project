from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You don't have any items in your bag yet!")
        return redirect(reverse('packages'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HJMCYHEgiPOT6f6HGio8jgwY5PIJwUOWj5Yf8au53lJljowOz5RRo4pHnDOUCmvGji8Zivm8tBwKOtwm8C2v7MQ00hZaMvt3F',
        'client_secret': 'client_secret',
    }

    return render(request, template, context)
