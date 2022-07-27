from django.urls import path
from . import views 

urlpatterns = [
    path('product', views.products, name='product'),
    path('', views.product, name='products'),
]