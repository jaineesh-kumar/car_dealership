from django.urls import path
from . import views

urlpatterns = [
    path('sell/', views.sell_trade_view, name='sell_trade'),
    path('enquiry/<int:car_id>/', views.submit_enquiry, name='submit_enquiry'),
]
