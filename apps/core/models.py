from django.db import models

class SiteSettings(models.Model):
    dealership_name = models.CharField(max_length=255, default="Marlow Motors")
    phone = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    hours = models.TextField(blank=True)
    social_links = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.dealership_name
