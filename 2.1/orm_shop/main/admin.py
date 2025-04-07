from django.contrib import admin
from django.contrib import admin
from .models import Client, Car, Sale

# Регистрация модели Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'middle_name', 'last_name', 'phone_number')  # Поля, отображаемые в списке
    search_fields = ('name', 'last_name', 'phone_number')  # Поля для поиска

# Регистрация модели Car
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'color', 'mileage', 'price')  # Поля, отображаемые в списке
    search_fields = ('model', 'color', 'year')  # Поля для поиска



# Регистрация модели Sale
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('client', 'car', 'created_at')  # Поля, отображаемые в списке
    list_filter = ('created_at',)  # Фильтр по дате продажи
    search_fields = ('client__name', 'client__last_name', 'car__model')  