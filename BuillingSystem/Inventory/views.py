from rest_framework .views import APIView
from rest_framework.response import Response
from .models import * 
from .Serializers import *

class ProductsView(APIView):

    # def get(self, request):

    #     all_products = Products.objects.all()

    #     products_datas =[]

    #     for products in all_products:

    #         single_product = {
    #             "id": products.id,
    #             "product_name": products.products_name,
    #             "code": products.code,
    #             "price": products.price
    #         }

    #         products_datas.append(single_product)

    

    #     return Response(products_datas)

    def get(self, request):

        all_products = Products.objects.all()

        serialized_products = Products_Serializers(all_products, many= True).data

        print(serialized_products)

    

        return Response(serialized_products)




    def post(self, request):

        new_product = Products(products_name = request.data["product_name"], code= request.data['code'], price = request.data['price'])

        new_product.save()

        return Response("Data Saved")
    
    
    


class ProductViewById(APIView):
        
    # def get(self, request, id):

    #     product = Products.objects.get(id = id)


    #     single_product = {
    #         "id": product.id,
    #         "product_name": product.products_name,
    #         "code": product.code,
    #         "price": product.price
    #         }

    #     return Response(single_product)
    
    def patch(self, request, id):

        product = Products.objects.filter(id = id)

        product.update(products_name = request.data["product_name"], code= request.data['code'], price = request.data['price'])
        
        return Response("updated")
    
    def delete(self, request, id):

        product = Products.objects.filter(id = id)

        product.delete()

        return Response("Deleted")
    
#Serializer 

    

    def get(self, request, id):

        product = Products.objects.get(id = id)


        single_productss = Products_Serializers2(product).data

        return Response(single_productss)