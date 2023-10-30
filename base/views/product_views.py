from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from base.models import Product
from base.serializers import ProductSerializer
# Create your views here.

from rest_framework import status





@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/products/',
    '/api/products/create/',
    '/api/products/upload/',
    '/api/products/<id>/reviews/',
    '/api/products/top/',
    '/api/products/<id>/',
    '/api/products/delete/<id>/',
    '/api/products/<update>/<id>/',

  ]
  return Response(routes)

@api_view(['GET'])
def get_products(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products,many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_single_product(request,pk):
  product = Product.objects.get(_id=pk)
  print(product)
  serializer = ProductSerializer(product,many=False)
  return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Producted Deleted')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
   user = request.user

   product = Product.objects.create(
      user=user,
      name='Sample Name',
      price=0,
      brand='Sample Brand',
      count_in_stock=0,
      category='Sample Category',
      description='',
      rating=2,
   )
   serializer = ProductSerializer(product, many=False)
   return Response(serializer.data)