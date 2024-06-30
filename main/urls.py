from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ProductDetailView, ContactListView, OrderCreateView, ProductUpdateView, \
    ProductDeleteView, VersionListView, VersionDetailView, VersionCreateView, VersionUpdateView, VersionDeleteView, \
    ProductCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('create_order/', OrderCreateView.as_view(), name='create_order'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("versions/", VersionListView.as_view(), name="versions"),
    path("versions/<int:pk>/", VersionDetailView.as_view(), name="version_detail"),
    path("create_version/", VersionCreateView.as_view(), name="version_create"),
    path("version/<int:pk>/update/", VersionUpdateView.as_view(), name="version_update"),
    path("version/<int:pk>/delete/", VersionDeleteView.as_view(), name="version_delete"),
]
