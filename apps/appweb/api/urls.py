from django.urls import path
from apps.appweb.api.api import proveed_api_view #ProveedorAPIView

urlpatterns = [
   # path('proveedor/', ProveedorAPIView.as_view(), name='proveed_api')
    path('proveedor/', proveed_api_view, name='proveed_api')
]