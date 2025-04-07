import json
from django.core.management.base import BaseCommand
from main.models import Client, Car, Sale  

class Command(BaseCommand):
    help = 'Загрузить данные из JSON в базу данных'

    def handle(self, *args, **options):
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

            # Заполнение таблицы Clients
            for client_data in data['clients']:
                Client.objects.create(**client_data)

            # Заполнение таблицы Cars
            for car_data in data['cars']:
                Car.objects.create(**car_data)

            # Заполнение таблицы Sales
            for sale_data in data['sales']:
                client = Client.objects.get(id=sale_data['client_id'])
                car = Car.objects.get(id=sale_data['car_id'])
                Sale.objects.create(client=client, car=car, created_at=sale_data['created_at'])

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))