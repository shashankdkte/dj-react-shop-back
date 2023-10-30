from django.urls import path
from base.views import product_views as views


urlpatterns = [
    # path("routes", views.getRoutes, name="routes"),
    path("",views.get_products,name="products"),
    path("create/",views.createProduct,name="product_create"),
    path("<str:pk>/",views.get_single_product,name="product_value"),
    path("delete/<str:pk>/",views.deleteProduct,name="product_delete"),
]
