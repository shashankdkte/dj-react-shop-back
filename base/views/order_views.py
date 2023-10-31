from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response

from base.models import Product, Order, OrderItem,ShippingAddress
from base.serializers import ProductSerializer,OrderSerializer
from rest_framework import status
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
  user = request.user
  data = request.data
  print(data)

  orderItems = data['orderItems']

  if orderItems and len(orderItems) == 0:
    return Response({'detail':'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
  else:

    # 1 Create Order
    order = Order.objects.create(
      user = user,
      payment_method = data['paymentMethod'],
      tax_price = data['taxPrice'],
      shipping_price = data['shippingPrice'],
      total_price = data['totalPrice']
    )

    # 2 Create Shipping Address
    shipping  = ShippingAddress.objects.create(
      order = order,
      address = data['shippingAddress']['address'],
      city=data['shippingAddress']['city'],
      postal_code=data['shippingAddress']['postalCode'],
      country=data['shippingAddress']['country'],

    )

    # 3 Create Order items and Set Order to OrderItem relationship

    for i in orderItems:
      product = Product.objects.get(_id = i['product'])

      item = OrderItem.objects.create(
        product = product,
        order = order,
        name=product.name,
        quantity = i['qty'],
        price = i['price'],
        image = product.image.url
      )


      # 4 Update Stock

      product.count_in_stock -= item.quantity
      product.save()

    serializer = OrderSerializer(order,many=False)
    return Response(serializer.data)
  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
  
   user = request.user
   try:
      order = Order.objects.get(_id=pk)
      if user.is_staff or order.user == user:
         serializer = OrderSerializer(order,many=False)
         return Response(serializer.data)
      else:
          Response({'detail':'Not authorized to view this order '},status=status.HTTP_400_BAD_REQUEST)
   except: 
     Response({'detail', 'Order does not exist'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request,pk):
   order = Order.objects.get(_id=pk)

   order.is_paid = True
   order.paid_at = datetime.now()
   order.save()

   return Response('Order was paid')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderToDelivered(request, pk):
    order = Order.objects.get(_id=pk)

    order.is_delivered = True
    order.delivered_at = datetime.now()
    order.save()

    return Response('Order was delivered')