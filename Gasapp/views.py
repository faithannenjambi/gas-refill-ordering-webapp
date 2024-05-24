
from django.shortcuts import render,redirect
from .models import Order, Contact

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    if request.method == "POST":
        name = request.POST['full-name']
        email = request.POST['email']
        message = request.POST['message']

        new_contact = Contact(
            name = name,
            email = email,
            message = message,
            )
        new_contact.save()

        return redirect('message')
    
    return render(request,'about.html')

def order(request):
    if request.method == "POST":
        cylinder_size = request.POST["cylinder-size"]
        phone_number = request.POST['phone-number']
        quantity = request.POST['quantity']
        full_name = request.POST['full-name']
        address = request.POST['address']
        total_amount = request.POST['total-amount']

        new_order = Order(
            cylinder_size = cylinder_size,
            full_name = full_name,
            address = address,
            phone_number = phone_number,
            quantity = quantity,
            total_amount = total_amount
         )
        new_order.save()

        return redirect('order-successful')

        
    return render(request,'order.html')


def order_successful(request):
    return render(request, 'order-successful.html')

def message(request):
    return render(request, 'message.html')