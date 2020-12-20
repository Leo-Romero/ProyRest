from django.urls import path
from apps.appweb.api.api import proveed_api_view, proveed_detail_api_view

urlpatterns = [
   # path('proveedor/', ProveedorAPIView.as_view(), name='proveed_api')
    path('proveedor/', proveed_api_view, name='proveed_api'),
    path('proveedor/<int:pk>/', proveed_detail_api_view, name='proveed_detail_api_view'),
]