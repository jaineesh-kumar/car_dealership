"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import HomeView, AboutView, ContactView, PrivacyView, TermsView

admin.site.site_header = "Marlow Motors Administration"
admin.site.site_title = "Marlow Motors Admin Portal"
admin.site.index_title = "Dealership Management System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('inventory/', include('apps.inventory.urls')),
    path('leads/', include('apps.leads.urls')),
    path('style-guide/', TemplateView.as_view(template_name='style_guide.html'), name='style_guide'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

