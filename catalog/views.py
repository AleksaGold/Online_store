from django.shortcuts import render


def index(request):
    return render(request, "main/home.html")


def contacts(request):
    return render(request, "main/contacts.html")
