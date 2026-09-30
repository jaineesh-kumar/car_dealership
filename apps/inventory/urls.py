from django.urls import path
from . import views

urlpatterns = [
    path('', views.InventoryListView.as_view(), name='inventory'),
    path('<slug:slug>/', views.CarDetailView.as_view(), name='car_detail'),
]
