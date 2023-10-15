from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("products/",views.get_products,name="products"),
    path("products/<str:pk>",views.get_single_product,name="product_value"),
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/',views.getUserProfile,name="users-profile"),
    path('users/',views.getUsers,name="users"),
    path('users/<str:pk>/',views.getUserById,name="user")

]

