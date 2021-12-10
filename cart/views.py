from django.shortcuts import render
from .utils import cookieCart, cartData, guestOrder
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import datetime

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        itemss = order.orderitem_set.all()
        cartItems = order.get_cart_items
       
    else:
        itemss = []
        order = {'get_cart_total' :0 , 'get_cart_items' :0, 'shipping':False}
   
    context = {'itemss' : itemss , 'order' : order}
    return render(request,  "cart/index.html", context)


def checkout(request):
    data = cartData(request)
	
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    value = data['valeur']



    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	

    if action =="add" and int(value) >1:
        orderItem.quantity = (orderItem.quantity + int(value)) 
    elif action == 'add':
    	orderItem.quantity = (orderItem.quantity  + 1)
        
    elif action == 'remove':
        	orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()


    if orderItem.quantity <= 0:
    	orderItem.delete()
    return JsonResponse('Item was added', safe=False)
    

def processOrder(request):
    
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated: 
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:    
        customer, order = guestOrder(request, data)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.complete = True
    order.save()    
    if order.shipping == True:
        ShoppingAddress .objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)
    return JsonResponse('Payment submitted..', safe=False) 
	   