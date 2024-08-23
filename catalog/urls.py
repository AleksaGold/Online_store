from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", products_list, name="products_list"),
    path("contacts/", contacts, name="contacts"),
]
