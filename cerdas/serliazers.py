from rest_framework import serializers
from .models import Cerda, ControlCelo


class CerdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cerda
        fields = [
            'id',
            'codigo',
            'fecha_nacimiento',
            'estado',
            'activa',
            'fecha_creacion',
            'fecha_actualizacion',
        ]
        read_only_fields = (
            'fecha_creacion',
            'fecha_actualizacion',
        )


class ControlCeloSerializer(serializers.ModelSerializer):
    cerda_codigo = serializers.CharField(
        source='cerda.codigo',
        read_only=True
    )

    class Meta:
        model = ControlCelo
        fields = [
            'id',
            'cerda',
            'cerda_codigo',
            'fecha_celo',
            'en_celo',
            'observaciones',
            'fecha_servicio_recomendada',
            'fecha_proximo_celo',
            'fecha_creacion',
            'fecha_actualizacion',
        ]
        read_only_fields = (
            'fecha_servicio_recomendada',
            'fecha_proximo_celo',
            'fecha_creacion',
            'fecha_actualizacion',
        )

    def validate(self, data):
        """
        Evitar más de un celo activo por cerda
        (doble seguridad además del constraint)
        """
        cerda = data.get('cerda')
        en_celo = data.get('en_celo', True)

        if en_celo:
            qs = ControlCelo.objects.filter(cerda=cerda, en_celo=True)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    "Esta cerda ya tiene un celo activo."
                )

        return data

