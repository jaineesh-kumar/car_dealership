from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Car(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    FUEL_CHOICES = (('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('hybrid', 'Hybrid'))
    TRANS_CHOICES = (('manual', 'Manual'), ('automatic', 'Automatic'))

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=100)
    variant = models.CharField(max_length=100, blank=True)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    km_driven = models.IntegerField()
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANS_CHOICES)
    owners = models.IntegerField(default=1)
    colour = models.CharField(max_length=50)
    registration_state = models.CharField(max_length=50)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.year} {self.brand.name} {self.model} {self.variant}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cars/')
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)
    is_cover = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.car.title}"

class CarFeature(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
