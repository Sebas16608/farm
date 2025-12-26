from django.shortcuts import render
from .models import Cerda, ControlCelo
from API import SuperAPIView
from .serliazers import CerdaSerializer, ControlCeloSerializer
# Create your views here.

class CerdaView(SuperAPIView):
    model = Cerda
    serializer = CerdaSerializer

class ControlCeloView(SuperAPIView):
    model = ControlCelo
    serializer = ControlCeloSerializer