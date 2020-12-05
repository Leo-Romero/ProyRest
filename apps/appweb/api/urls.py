from django.urls import path
from apps.appweb.api.api import ProveedorAPIView

urlpatterns = [
    path('proveedor/', ProveedorAPIView.as_view(), name='proveed_api')
]