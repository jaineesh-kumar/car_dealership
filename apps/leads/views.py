from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Enquiry, SellRequest
from apps.inventory.models import Car

def sell_trade_view(request):
    if request.method == 'POST':
        # Honeypot check
        if request.POST.get('website_url'):
            return redirect('home')
            
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        km = request.POST.get('km')
        SellRequest.objects.create(
            name=name, phone=phone, brand=brand, model=model, year=year, km=km
        )
        messages.success(request, "Your sell request has been submitted successfully. We will contact you soon.")
        return redirect('sell_trade')
    return render(request, 'leads/sell.html')

def submit_enquiry(request, car_id):
    if request.method == 'POST':
        # Honeypot check
        if request.POST.get('website_url'):
            return redirect('home')
            
        car = get_object_or_404(Car, id=car_id)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        enquiry_type = request.POST.get('type', 'enquiry')
        
        Enquiry.objects.create(
            car=car, name=name, phone=phone, email=email, message=message, type=enquiry_type
        )
        messages.success(request, f"Your {enquiry_type.replace('_', ' ')} request has been sent.")
        return redirect('car_detail', slug=car.slug)
    return redirect('home')
