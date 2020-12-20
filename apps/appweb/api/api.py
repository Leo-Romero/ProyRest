from rest_framework.response import Response
# from rest_framework.views import APIView
from apps.appweb.models import Proveedor
from apps.appweb.api.serializers import ProveedorSerializer

from rest_framework.decorators import api_view                          # para implementar un def

# class ProveedorAPIView(APIView):
#     def get(self, request):
#         proveed = Proveedor.objects.all()
#         proveed_serializer = ProveedorSerializer(proveed, many=True)    # porque son varios
#         return Response(proveed_serializer.data)

@api_view(['GET', 'POST'])
def proveed_api_view(request):
    if request.method == 'GET':
        proveed = Proveedor.objects.all()
        proveed_serializer = ProveedorSerializer(proveed, many=True)    # porque son varios
        return Response(proveed_serializer.data)
    elif request.method == 'POST':
        proveed_serializer = ProveedorSerializer(data = request.data)
        if proveed_serializer.is_valid():
            proveed_serializer.save()
            return Response(proveed_serializer.data)
        return Response(proveed_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def proveed_detail_api_view(request, pk=None):
    if request.method == 'GET':
        proveed = Proveedor.objects.filter(id = pk).first()
        proveed_serializer = ProveedorSerializer(proveed)
        return Response(proveed_serializer.data)
    elif request.method == 'PUT':                   # en rest en vez de POST se usa PUT
        proveed = Proveedor.objects.filter(id = pk).first()
        # al pasar la instancia "proveed" rest sabe que es para actualizar con la "data"
        proveed_serializer = ProveedorSerializer(proveed, data = request.data)
        if proveed_serializer.is_valid():
            proveed_serializer.save()
            return Response(proveed_serializer.data)
        return Response(proveed_serializer.errors)
    elif request.method == 'DELETE':
        proveed = Proveedor.objects.filter(id = pk).first()
        proveed.delete()
        return Response('Eliminado')
