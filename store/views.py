from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
import json

from .models import Order_details
from .models import Order
from .models import Admin
from .models import Categories
from .models import Product
from .models import Customer

@api_view(['post'])
def createcus(request):
    data = json.loads(request.body)

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone = data['phone']
    address = data['address']
    city = data['city']
    state = data['state']
    postal_code = data['postal_code']

    singup = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, postal_code=postal_code)

    singup.save()

    return Response({'status' : 'OK'})



@api_view(['get'])
def logcus(request):
    usersList = Customer.objects.all()
    usersList2 = json.loads(request.body)
    email = usersList2['email']
    chek = Customer.objects.get(email=email)
    data = []
    for user in usersList:
        userData = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'city': user.city,
            'postal_code': user.postal_code,
        }
        data.append(userData)

    return JsonResponse({'data': data})

@api_view(['get'])
def allcus(request):
    usersList = Customer.objects.all()
 
    data = []
    for user in usersList:
        userData = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'city': user.city,
            'postal_code': user.postal_code,
        }
        data.append(userData)

    return JsonResponse({'data': data})


@api_view(['DELETE'])
def deletecus(request):
    data = json.loads(request.body)
    email = data['email']

    Customer.objects.filter(email=email).delete()

    return JsonResponse({'status': 'ok'})

@api_view(['PUT'])
def updatacus(request):
    data = json.loads(request.body)
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']

    user = Customer.objects.get(email=email)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    return JsonResponse({'status': 'ok'})



@api_view(['get'])
def logadmin(request):
    usersList = Admin.objects.all()
    usersList2 = json.loads(request.body)
    username = usersList2['username']
    password = usersList2['password']
    chek = Admin.objects.get(username=username, password = password)
    data = []
    for user in usersList:
        userData = {
            'first_name': user.first_name,
            'username': user.username,
            'password': user.password,
            'email': user.email,
         
        }
        data.append(userData)

    return JsonResponse({'data': data})


@api_view(['post'])
def createpro(request):
    data = json.loads(request.body)

    product_name = data['product_name']
    description = data['description']
    price = data['price']
    image = data['image']
    
   

    singup = Product(product_name=product_name, description=description, price=price, image=image)

    singup.save()

    return Response({'status' : 'OK'})


@api_view(['get'])
def allpro(request):
    usersList = Product.objects.all()
 
    data = []
    for user in usersList:
        userData = {
            'product_name': user.product_name,
            'description': user.description,
            'price': user.price,
            
            
        }
        data.append(userData)

    return JsonResponse({'data': data})

@api_view(['DELETE'])
def deletepro(request):
    data = json.loads(request.body)
    product_name = data['product_name']

    Product.objects.filter(product_name=product_name).delete()

    return JsonResponse({'status': 'ok'})

@api_view(['PUT'])
def updatapro(request):
    data = json.loads(request.body)
    product_name = data['product_name']
    description = data['description']
    price = data['price']

    user = Product.objects.get(product_name=product_name)
    user.product_name = product_name
    user.description = description
    user.price = price

    user.save()

    return JsonResponse({'status': 'ok'})



@api_view(['post'])
def createcate(request):
    data = json.loads(request.body)

    category_name = data['category_name']
    category_description = data['category_description']
    category_image = data['category_image']
   
   

    singup = Categories(category_name=category_name, category_description=category_description, category_image=category_image)

    singup.save()

    return Response({'status' : 'OK'})

@api_view(['get'])
def allcate(request):
    usersList = Categories.objects.all()
 
    data = []
    for user in usersList:
        userData = {
            'category_name': user.category_name,
            'category_description': user.category_description,
  
        }
        data.append(userData)

    return JsonResponse({'data': data})


@api_view(['DELETE'])
def deletecate(request):
    data = json.loads(request.body)
    category_name = data['category_name']

    Categories.objects.filter(category_name=category_name).delete()

    return JsonResponse({'status': 'ok'})


@api_view(['PUT'])
def updatacate(request):
    data = json.loads(request.body)
    category_name = data['category_name']
    category_description = data['category_description']
    

    user = Categories.objects.get(category_name=category_name)
    user.category_name = category_name
    user.category_description = category_description
    

    user.save()

    return JsonResponse({'status': 'ok'})



@api_view(['post'])
def createorder(request):
    data = json.loads(request.body)


   # payment_type = data['payment_type']
    customer_id = data['customer_id']
   
   

    singup = Order(customer_id=customer_id)

    singup.save()

    return Response({'status' : 'OK'})




@api_view(['get'])
def brow(request):
    usersList = Categories.objects.all()
    usersList2 = Product.objects.all()

 
    data = []
    for user in usersList :
    
        userData = {
            'category_name': user.category_name,
        }
    for user in usersList2:
        userData2 = {
            
            'product_name': user.product_name,
            'description': user.description,
            'price': user.price,
        }

        data.append([userData,userData2])
        
    return JsonResponse({'data': data})


@api_view(['post'])
def addcart(request):
    usersList = Customer.objects.all()
    usersList3 = Product.objects.all()
    usersList2 = json.loads(request.body)
    usersList4 = json.loads(request.body)
    add = json.loads(request.body)
    email = usersList2['email']
    chek = Customer.objects.get(email=email)
    data = []
    for user in usersList:
        userData = {
           
            'first_name': user.first_name,
            'phone': user.phone,
        }
    for user in usersList3:
        userData2 = {
           
            'product_name': user.product_name,
            'description': user.description,
            'price': user.price,

        }
        data.append([userData,userData2])
    order_id = add["order_id"]
    quantity = add['quantity']
    item_note = add['item_note']
    item_price = add['item_price']
    item_discount = add['item_discount']
    item_total = int(quantity) * int(item_price) - int(item_discount)

    singup = Order_details(quantity=quantity, item_note=item_note ,item_price=item_price,item_discount=item_discount, item_total=item_total, order_id=order_id)

    singup.save()
    total_amount = int(quantity) * int(item_price) - int(item_discount)
    addorder = Order(total_amount = total_amount)
    addorder.save()
    return JsonResponse({'data': data})


@api_view(['DELETE'])
def deleteorder(request):
    data = json.loads(request.body)
    id = data['id']
    
    Order.objects.filter(id=id).delete()
    Order_details.objects.filter(id=id).delete()


    return JsonResponse({'status': 'ok'})
    


@api_view(['get'])
def allorder(request):
    usersList = Order.objects.all()
    usersList2 = Order_details.objects.all()

 
    data = []
    for user in usersList :
    
        userData = {
            'order_date': user.order_date,
            'total_amount': user.total_amount,
            'payment_status': user.payment_status,
            




        }
    for user in usersList2:
        userData2 = {
           
            "quantity" : user.quantity,
            "item_note" : user.item_note,
            "item_price" : user.item_price,
            "item_discount" : user.item_discount,
            "item_total" : user.item_total,


            
        }

        data.append([userData,userData2])
        
    return JsonResponse({'data': data})
    
    


   