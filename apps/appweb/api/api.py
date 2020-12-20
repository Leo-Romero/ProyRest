from rest_framework import status
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
    # listar
    if request.method == 'GET':
        # queryset
        proveed = Proveedor.objects.all()
        proveed_serializer = ProveedorSerializer(proveed, many=True)    # porque son varios
        return Response(proveed_serializer.data, status = status.HTTP_200_OK)
    
    # Agregar
    elif request.method == 'POST':
        proveed_serializer = ProveedorSerializer(data = request.data)

        # validar
        if proveed_serializer.is_valid():
            proveed_serializer.save()
            return Response(proveed_serializer.data, status = status.HTTP_201_CREATED)
        return Response(proveed_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proveed_detail_api_view(request, pk=None):
    # queryset
    proveed = Proveedor.objects.filter(id = pk).first()

    # validar
    if proveed:

        # listar
        if request.method == 'GET':
            proveed_serializer = ProveedorSerializer(proveed)
            return Response(proveed_serializer.data, status = status.HTTP_200_OK)
        
        # Modificar
        elif request.method == 'PUT':                   # en rest en vez de POST se usa PUT
            # al pasar la instancia "proveed" rest sabe que es para actualizar con la "data"
            proveed_serializer = ProveedorSerializer(proveed, data = request.data)
            if proveed_serializer.is_valid():
                proveed_serializer.save()
                return Response(proveed_serializer.data, status = status.HTTP_200_OK)
            return Response(proveed_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Borrar
        elif request.method == 'DELETE':
            proveed.delete()
            return Response({'message': 'Usuario eliminado.'}, status = status.HTTP_200_OK)
    return Response({'message': 'Usuario no encontrado.'}, status = status.HTTP_400_BAD_REQUEST)
