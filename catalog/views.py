from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "main/home.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "main/product_detail.html", context)


def contacts(request):
    return render(request, "main/contacts.html")
