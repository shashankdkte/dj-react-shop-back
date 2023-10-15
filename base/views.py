from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer,UserSerializerWithToken,UserSerializer
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
      data = super().validate(attrs)
      serializer = UserSerializerWithToken(self.user).data
      for k,v in serializer.items():
        data[k] = v
      return data

class MyTokenObtainPairView(TokenObtainPairView):
   serializer_class = MyTokenObtainPairSerializer



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

@api_view(['POST'])
def registerUser(request):
  data = request.data
  try:
    user = User.objects.create(
      first_name = data['name'],
      username=data['email'],
      email = data['email'],
      password = data['password']
    )
    serializer = UserSerializerWithToken(user,many=False)
    return Response(serializer.data)
  except:
    message = {'detail':'User with this email already exist'}
    return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
  user = request.user
  serializer =UserSerializer(user,many=False)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
  users = User.objects.all()
  serializer =UserSerializer(users,many=True)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request,pk):
  user = User.objects.get(id=pk)
  serializer =UserSerializer(user,many=False)
  return Response(serializer.data)

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