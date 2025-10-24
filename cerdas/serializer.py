from rest_framework import serializers
from .models import Cerda, ControlCelo

class CerdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cerda
        fields = "__all__"

class CeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlCelo
        fields = "__all__"