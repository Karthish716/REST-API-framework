from django.urls import path
from .views import *

urlpatterns = [
    path('products/add/', ProductsView.as_view())
]