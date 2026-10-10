from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def main(request):
    product = Products.objects.all()
    return render(request, 'index.html', {'product' : product})

def purchase(request, id):
    product = Products.objects.get( id = id )

    if request.method == 'POST':
        a = request.POST['newValue']

        product.quantity = a 

        product.save()

        return redirect('main')
    return render(request, 'purchase.html', { 'product' : product })

def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('main')

def add(request):

    if request.method == 'POST':

        name = request.POST['name']
        category = request.POST['category']
        quantity = request.POST['quantity']
        minimum_stock = request.POST['minimum_stock']
        price = request.POST['price']

        product = Products( name = name, category = category, quantity = quantity, minimum_stock = minimum_stock, price = price  )

        product.save()

        return redirect('main')
    return render(request, 'add.html')

def restock(request,id):
    product = Products.objects.get(id=id)

    if request.method == 'POST':
        Restock = request.POST['restock']
        product.quantity += int(Restock)

        product.save()

        return redirect('main')
    return render(request, 'restock.html', {'product' : product})