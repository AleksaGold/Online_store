from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="update_product"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"),
]
