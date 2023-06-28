from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from bag.contexts import bag_contents
from .forms import OrderForm
from events.models import Events
from .models import Order, OrderItem
import stripe
import csv

# Create your views here.


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    intent = None
    if request.method == "POST":
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    event = Events.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        event=event,
                        quantity=item_data,
                    )
                    order_item.save()

                except Events.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form ')
    else:

        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'There is nothing in your bag')
            return redirect(reverse('event_list'))

        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request)
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret if intent else None,
    }

    return render(request, template, context)


def download_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # Create a response object with CSV mimetype
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename=order_{order.order_number}.csv'

    # Create a CSV writer object and write the header row
    writer = csv.writer(response)
    writer.writerow(['Name', 'Quantity', 'Price', 'Total',
                    'Date', 'Time', 'Location', 'Image'])

    # Write each line item as a row in the CSV
    for line_item in order.lineitems.all():
        writer.writerow([
            line_item.event.name,
            line_item.quantity,
            line_item.event.price,
            line_item.lineitem_total,
            line_item.event.date,
            line_item.event.time,
            line_item.event.location,
            request.build_absolute_uri(
                line_item.event.image.url) if line_item.event.image
            else '',
        ])

    # Return the response with the CSV file
    return response


def checkout_success(request, order_number):

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order Succesfull')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'download_url': reverse('download_order', args=[order_number])
    }
    return render(request, template, context)
