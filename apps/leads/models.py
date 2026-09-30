from django.db import models
from apps.inventory.models import Car

class Enquiry(models.Model):
    TYPE_CHOICES = (('enquiry', 'Enquiry'), ('test_drive', 'Test Drive'), ('callback', 'Callback'))
    STATUS_CHOICES = (('new', 'New'), ('contacted', 'Contacted'), ('closed', 'Closed'))

    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True, related_name='enquiries')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='enquiry')
    preferred_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return f"{self.type} from {self.name}"

class SellRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    km = models.IntegerField()
    expected_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    photos = models.ImageField(upload_to='sell_requests/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sell Request: {self.brand} {self.model} from {self.name}"
