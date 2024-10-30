from django.shortcuts import render
from django.http import JsonResponse
import json
from django.shortcuts import redirect
import datetime
from .models import *
from .utilis import cookieCart, cartData, guestOrder


def store(request):
    data = cartData(request)

    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)

    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = 1
    elif action == 'remove':
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity == 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def removeItem(request, item_id):
    if request.method == 'POST' and request.user.is_authenticated:
        customer = request.user.customer
        try:
            order = Order.objects.get(customer=customer, complete=False)
            orderItem = OrderItem.objects.get(id=item_id, order=order)
            orderItem.delete()
        except OrderItem.DoesNotExist:
            # Optionally handle the error
            pass
    return redirect('cart')


def processOrder(request):
    try:
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)

        else:
            customer, order = guestOrder(request, data)


        total = float(data.get('form', {}).get('total', 0))
        # total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data.get('shipping', {}).get('address', ''),
            city=data.get('shipping', {}).get('city', ''),
            state=data.get('shipping', {}).get('state', ''),
            zipcode=data.get('shipping', {}).get('zipcode', ''),
        )

        return JsonResponse('Payment submitted..', safe=False)

    except KeyError as e:
        print(f"KeyError: Missing field {e}")
        return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)

    except Exception as e:
        print(f"Error processing order: {e}")
        return JsonResponse({'error': str(e)}, status=500)


