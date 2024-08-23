from django.shortcuts import render

from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "main/home.html", context)


def contacts(request):
    return render(request, "main/contacts.html")
