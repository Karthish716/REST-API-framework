from rest_framework .views import APIView
from rest_framework.response import Response
from .models import * 

class ProductsView(APIView):

    def post(self, request):

        new_product = Products(products_name = request.data["product_name"], code= request.data['code'], price = request.data['price'])

        new_product.save()

        return Response("Data Saved")