from django.views.generic import ListView, DetailView
from .models import Car, Brand

class InventoryListView(ListView):
    model = Car
    template_name = 'inventory/list.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        qs = Car.objects.filter(status='published').order_by('-created_at')
        
        brand = self.request.GET.get('brand')
        fuel = self.request.GET.get('fuel')
        if brand:
            qs = qs.filter(brand__slug=brand)
        if fuel:
            qs = qs.filter(fuel=fuel)
            
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context

class CarDetailView(DetailView):
    model = Car
    template_name = 'inventory/detail.html'
    context_object_name = 'car'

    def get_queryset(self):
        return Car.objects.filter(status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['similar_cars'] = Car.objects.filter(
            brand=self.object.brand, status='published'
        ).exclude(id=self.object.id)[:4]
        return context
