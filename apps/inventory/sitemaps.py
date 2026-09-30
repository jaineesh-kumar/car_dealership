from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Car

class CarSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Car.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.created_at

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ['home', 'about', 'contact', 'inventory', 'sell_trade', 'privacy', 'terms']

    def location(self, item):
        return reverse(item)
