from rest_framework import serializers
from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    ...

    # доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     book = Order.objects.filter(id = instance.id).all()
    #     book_count = book.count()   
    #     representation['orders_count'] = [book_count]
    #     return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


    # доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        books_data =  BookSerializer(instance.books.all(), many=True).data
        for book in books_data:
            book.pop('id', None) 
            book.pop('orders_count', None) 
        representation['books'] = books_data
       
        return representation
