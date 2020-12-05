from rest_framework.response import Response
from rest_framework.views import APIView
from apps.appweb.models import Proveedor
from apps.appweb.api.serializers import ProveedorSerializer

class ProveedorAPIView(APIView):
    def get(self, request):
        proveed = Proveedor.objects.all()
        proveed_serializer = ProveedorSerializer(proveed, many=True)    # porque son varios
        return Response(proveed_serializer.data)
