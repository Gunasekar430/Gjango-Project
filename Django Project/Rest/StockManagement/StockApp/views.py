from django.shortcuts import render, redirect, get_object_or_404

from .models import *


# =========================
# PRODUCT LIST
# =========================

def index(request):

    search = request.GET.get('search', '')

    if search:

        products = Product.objects.filter(
            name__icontains=search
        )

    else:

        products = Product.objects.all()

    low_stock = Product.objects.filter(
        quantity__lte=models.F('minimum_stock')
    )

    return render(
        request,
        'index.html',
        {
            'products': products,
            'low_stock': low_stock,
            'search': search
        }
    )


# =========================
# ADD PRODUCT
# =========================

def add_product(request):

    if request.method == 'POST':

        name = request.POST['name']

        category = request.POST['category']

        quantity = int(request.POST['quantity'])

        minimum_stock = int(request.POST['minimum_stock'])

        price = request.POST['price']

        Product.objects.create(

            name=name,

            category=category,

            quantity=quantity,

            minimum_stock=minimum_stock,

            price=price
        )

        return redirect('index')

    return render(request, 'add.html')


# =========================
# DELETE PRODUCT
# =========================

def delete_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    product.delete()

    return redirect('index')


# =========================
# STOCK OUT
# =========================

def stock_out(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == 'POST':

        quantity = int(
            request.POST['quantity']
        )

        # Business Rule
        # Cannot issue more than available stock

        if quantity <= 0:

            return render(
                request,
                'stockout.html',
                {
                    'product': product,
                    'error': 'Quantity must be greater than 0'
                }
            )

        if quantity > product.quantity:

            return render(
                request,
                'stockout.html',
                {
                    'product': product,
                    'error': 'Cannot issue more than available stock'
                }
            )

        product.quantity -= quantity

        product.save()

        return redirect('index')

    return render(
        request,
        'stockout.html',
        {
            'product': product
        }
    )


# =========================
# CREATE RESTOCK REQUEST
# =========================

def create_restock(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if product.quantity > product.minimum_stock:

        return redirect('index')

    if request.method == 'POST':

        requested_quantity = int(
            request.POST['requested_quantity']
        )

        if requested_quantity <= 0:

            return render(
                request,
                'restock.html',
                {
                    'product': product,
                    'error': 'Quantity must be greater than 0'
                }
            )

        RestockRequest.objects.create(

            product=product,

            requested_quantity=requested_quantity,

            status='Pending'
        )

        return redirect('restock_list')

    return render(
        request,
        'restock.html',
        {
            'product': product
        }
    )


# =========================
# RESTOCK LIST
# =========================

def restock_list(request):

    requests = RestockRequest.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'restock.html',
        {
            'requests': requests
        }
    )


# =========================
# APPROVE RESTOCK
# =========================

def approve_restock(request, id):

    restock = get_object_or_404(
        RestockRequest,
        id=id
    )

    # Only pending request can be approved

    if restock.status != 'Pending':

        return redirect('restock_list')

    product = restock.product

    # Increase stock

    product.quantity += restock.requested_quantity

    product.save()

    # Update request status

    restock.status = 'Approved'

    restock.save()

    return redirect('restock_list')


# =========================
# REJECT RESTOCK
# =========================

def reject_restock(request, id):

    restock = get_object_or_404(
        RestockRequest,
        id=id
    )

    if restock.status == 'Pending':

        restock.status = 'Rejected'

        restock.save()

    return redirect('restock_list')