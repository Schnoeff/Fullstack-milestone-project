from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from packages.models import Package
from bag.contexts import bag_contents

import stripe
import json
# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Oops,something went wrong')
    return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'county': request.POST['county'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                package = Package.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        package=package,
                        quantity=item_data,
                    )
                    order_line_item.save()
                else:
                    for quantity in item_data():
                        order_line_item = OrderLineItem(
                            order=order,
                            package=package,
                            quantity=quantity,
                        )
                        order_line_item.save()

        request.session['save_info'] = 'save-info' in request.POST
        return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "You don't have any items in your bag yet!")
            return redirect(reverse('packages'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        print("TYRING STUFF", intent.client_secret)

        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret_key': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order has been placed!! \
        Your order number is {order_number}. A confirmation \
        email will be sent to at {order.email} and we will give you a call \
        to arrange cleaning times.')

    if 'bag' in request.session:
        del request.session['bag']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }

        return render(request, template, context)
