from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CerdaSerializer, CeloSerializer
from .models import Cerda, ControlCelo
# Create your views here.

# Funcion para no repetir lo mismo
def notexist():
    return {"error": "Los datos no fueron encontrados"}
class CerdaView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                cerda = Cerda.objects.get(pk=pk)
                serializer = CerdaSerializer(cerda)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Cerda.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            cerda = Cerda.objects.all()
            serializer = CerdaSerializer(cerda, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = CerdaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            cerda = Cerda.objects.get(pk=pk)
        except Cerda.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = CerdaSerializer(cerda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            cerda = Cerda.objects.get(pk=pk)
        except Cerda.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        cerda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

