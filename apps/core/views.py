from django.views.generic import TemplateView
from apps.inventory.models import Car

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_cars'] = Car.objects.filter(status='published', is_featured=True)[:4]
        return context
