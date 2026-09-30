import random
import urllib.request
from decimal import Decimal
from tempfile import NamedTemporaryFile
from django.core.management.base import BaseCommand
from django.core.files import File
from apps.inventory.models import Brand, Car, CarImage, CarFeature

class Command(BaseCommand):
    help = 'Seeds the database with sample cars and images.'

    def handle(self, *args, **options):
        self.stdout.write("Deleting existing data...")
        Car.objects.all().delete()
        Brand.objects.all().delete()

        brands = ['Audi', 'BMW', 'Mercedes-Benz', 'Honda', 'Toyota', 'Ford', 'Tesla']
        brand_objs = {}
        for b in brands:
            brand_objs[b] = Brand.objects.create(name=b)

        models_data = [
            ('Audi', 'A4', 'Sedan', 'petrol', 'automatic', 35000.00),
            ('Audi', 'Q7', 'SUV', 'diesel', 'automatic', 65000.00),
            ('BMW', 'X5', 'SUV', 'diesel', 'automatic', 55000.00),
            ('BMW', '3 Series', 'Sedan', 'petrol', 'automatic', 42000.00),
            ('Mercedes-Benz', 'C-Class', 'Sedan', 'petrol', 'automatic', 48000.00),
            ('Mercedes-Benz', 'GLE', 'SUV', 'diesel', 'automatic', 70000.00),
            ('Honda', 'Civic', 'Sedan', 'petrol', 'manual', 22000.00),
            ('Honda', 'CR-V', 'SUV', 'petrol', 'automatic', 28000.00),
            ('Toyota', 'Camry', 'Sedan', 'hybrid', 'automatic', 30000.00),
            ('Toyota', 'RAV4', 'SUV', 'hybrid', 'automatic', 32000.00),
            ('Ford', 'Mustang', 'Coupe', 'petrol', 'manual', 45000.00),
            ('Ford', 'Explorer', 'SUV', 'petrol', 'automatic', 38000.00),
            ('Tesla', 'Model 3', 'Sedan', 'electric', 'automatic', 40000.00),
            ('Tesla', 'Model Y', 'SUV', 'electric', 'automatic', 49000.00),
            ('Audi', 'A6', 'Sedan', 'petrol', 'automatic', 45000.00),
            ('BMW', '5 Series', 'Sedan', 'diesel', 'automatic', 52000.00),
            ('Mercedes-Benz', 'E-Class', 'Sedan', 'petrol', 'automatic', 55000.00),
            ('Honda', 'Accord', 'Sedan', 'petrol', 'automatic', 26000.00),
            ('Toyota', 'Highlander', 'SUV', 'hybrid', 'automatic', 35000.00),
            ('Ford', 'F-150', 'Truck', 'petrol', 'automatic', 42000.00),
        ]

        image_urls = [
            "https://images.unsplash.com/photo-1614200187524-dc4b892acf16?w=800&q=80"
        ]

        self.stdout.write("Creating 20 cars...")
        for i, data in enumerate(models_data):
            brand_name, model_name, variant, fuel, transmission, price = data
            year = random.randint(2018, 2023)
            km = random.randint(5000, 80000)
            
            car = Car.objects.create(
                title=f"{year} {brand_name} {model_name} {variant}".strip(),
                brand=brand_objs[brand_name],
                model=model_name,
                variant=variant,
                year=year,
                price=Decimal(price),
                km_driven=km,
                fuel=fuel,
                transmission=transmission,
                owners=random.randint(1, 3),
                colour=random.choice(['Black', 'White', 'Silver', 'Grey', 'Blue', 'Red']),
                registration_state='NY',
                description="This is a beautiful demo car. In real life this would be a full description of the vehicle, its history, and its features.",
                is_featured=(i % 5 == 0),
                is_sold=False,
                status='published'
            )

            CarFeature.objects.create(car=car, name="Bluetooth")
            CarFeature.objects.create(car=car, name="Backup Camera")
            CarFeature.objects.create(car=car, name="Alloy Wheels")

            for j in range(2):
                img_url = random.choice(image_urls)
                img_temp = NamedTemporaryFile(delete=True)
                req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response:
                    img_temp.write(response.read())
                img_temp.flush()
                
                car_img = CarImage(car=car, order=j, is_cover=(j==0))
                car_img.image.save(f"car_{car.id}_{j}.jpg", File(img_temp))
                car_img.save()
            
            self.stdout.write(f"Created {car.title}")

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
