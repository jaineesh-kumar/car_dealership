from django.contrib import admin
from .models import Enquiry, SellRequest

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'car', 'status', 'created_at')
    list_filter = ('type', 'status', 'created_at')
    search_fields = ('name', 'phone', 'email')

@admin.register(SellRequest)
class SellRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'year', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'brand', 'model')
