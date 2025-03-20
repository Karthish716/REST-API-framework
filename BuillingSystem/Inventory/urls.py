from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/<int:id>/', ProductViewById.as_view()),

]