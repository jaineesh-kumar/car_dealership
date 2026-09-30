from django.contrib import admin
from .models import Brand, Car, CarImage, CarFeature

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 6

class CarFeatureInline(admin.TabularInline):
    model = CarFeature
    extra = 3

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'year', 'price', 'is_featured', 'is_sold', 'status')
    list_filter = ('status', 'is_sold', 'brand', 'year', 'fuel', 'transmission')
    search_fields = ('title', 'model', 'variant')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CarImageInline, CarFeatureInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'brand', 'model', 'variant', 'year')
        }),
        ('Pricing & Status', {
            'fields': ('price', 'status', 'is_featured', 'is_sold')
        }),
        ('Specifications', {
            'fields': ('km_driven', 'fuel', 'transmission', 'owners', 'colour', 'registration_state')
        }),
        ('Detailed Description', {
            'fields': ('description',),
        }),
    )
