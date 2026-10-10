from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def main(request):
    emp = DeliveryEmployee.objects.all()
    return render(request, 'index.html', {'emp' : emp})

def orderPage(request):
    emp = DeliveryEmployee.objects.all()

    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        address = request.POST['address']
        priority = request.POST['priority']
        assigned_to = request.POST['assigned_to']
        status = request.POST['status']

        employee = DeliveryEmployee.objects.get(
            name=assigned_to
        )

        order = Order(order = employee, customer_name = customer_name, address = address, priority = priority, assigned_to = assigned_to,status = status )

        order.save()

        return redirect('orderPage')

    return render(request, 'orderPage.html', {'emp' : emp})
