from django.core.management.base import BaseCommand
from core.models import Pharmacy, Product
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample pharmacies and products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Clear existing data
        Pharmacy.objects.all().delete()
        Product.objects.all().delete()

        pharmacies = [
            {'name': 'HealthPlus Central', 'city': 'New York', 'address': '123 Broadway', 'verified': True},
            {'name': 'City Care Pharmacy', 'city': 'Chicago', 'address': '456 Michigan Ave', 'verified': True},
            {'name': 'Green Cross', 'city': 'Seattle', 'address': '789 Pike St', 'verified': True},
            {'name': 'MediLife', 'city': 'Austin', 'address': '321 Congress Ave', 'verified': False},
            {'name': 'QuickMeds', 'city': 'Miami', 'address': '654 Ocean Dr', 'verified': True},
            {'name': 'Wellness Hub', 'city': 'Denver', 'address': '987 Colfax Ave', 'verified': True},
        ]

        created_pharmacies = []
        for p_data in pharmacies:
            pharmacy = Pharmacy.objects.create(
                name=p_data['name'],
                address=p_data['address'],
                city=p_data['city'],
                latitude=40.7128 + random.uniform(-1, 1), # Random coords for demo
                longitude=-74.0060 + random.uniform(-1, 1),
                is_verified=p_data['verified']
            )
            created_pharmacies.append(pharmacy)
            self.stdout.write(f'Created pharmacy: {pharmacy.name}')

        products_list = [
            {'name': 'Aspirin 500mg', 'category': 'Pain Relief', 'price': 5.99},
            {'name': 'Amoxicillin 250mg', 'category': 'Antibiotics', 'price': 12.50},
            {'name': 'Vitamin C 1000mg', 'category': 'Supplements', 'price': 8.99},
            {'name': 'Ibuprofen 400mg', 'category': 'Pain Relief', 'price': 6.49},
            {'name': 'Cetirizine 10mg', 'category': 'Allergy', 'price': 15.00},
            {'name': 'Paracetamol 500mg', 'category': 'Pain Relief', 'price': 3.99},
            {'name': 'Omeprazole 20mg', 'category': 'Digestive Health', 'price': 18.25},
            {'name': 'Multivitamin Complex', 'category': 'Supplements', 'price': 22.99},
            {'name': 'Bandages (Pack of 20)', 'category': 'First Aid', 'price': 4.50},
            {'name': 'Antiseptic Cream', 'category': 'First Aid', 'price': 7.25},
            {'name': 'Cough Syrup', 'category': 'Cold & Flu', 'price': 9.99},
            {'name': 'Throat Lozenges', 'category': 'Cold & Flu', 'price': 5.49},
        ]

        for product_data in products_list:
            # Assign random pharmacy
            pharmacy = random.choice(created_pharmacies)
            Product.objects.create(
                pharmacy=pharmacy,
                name=product_data['name'],
                description=f"High quality {product_data['name']} from {pharmacy.name}.",
                category=product_data['category'],
                price=product_data['price'],
                stock_quantity=random.randint(0, 50), # Some might be 0 (out of stock)
                is_available=True
            )
            self.stdout.write(f'Created product: {product_data["name"]}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
