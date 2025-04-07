from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Review
from .serializers import ProductListSerializer, ProductDetailsSerializer
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""

    products = Product.objects.all()
    serialaser = ProductListSerializer(products, many=True)
    return Response(serialaser.data)




class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""

        try:
            product = Product.objects.get(id=product_id)
            serialaser = ProductListSerializer(product)
            return Response(serialaser.data)
        except Product.DoesNotExist:
            return Response({"detail": "Товар не найден."}, status=status.HTTP_404_NOT_FOUND)
        

        


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """Обработайте значение параметра mark и реализуйте получение 
        отзывов по конкретному товару с определённой оценкой. 
        Реализуйте сериализацию полученных данных и отдайте 
        отсериализованные данные в Response."""
        
        mark = request.query_params.get('mark', None)  

        try:
            product = Product.objects.get(id=product_id)

            if mark is not None:
                reviews = Review.objects.filter(product=product, mark=mark)
            else:
                reviews = Review.objects.filter(product=product)

            serializer_product = ProductDetailsSerializer(product)
            serializer_reviews = ReviewSerializer(reviews, many=True)

            return Response({
                "product": serializer_product.data,
                "reviews": serializer_reviews.data
            })
        
        except Product.DoesNotExist:
            return Response({"detail": "Товар не найден."}, status=status.HTTP_404_NOT_FOUND)
