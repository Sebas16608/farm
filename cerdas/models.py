from django.db import models
from django.utils import timezone
from datetime import timedelta


class Cerda(models.Model):
    ESTADO_CHOICES = [
        ('preñada', 'Preñada'),
        ('lactante', 'Lactante'),
        ('vacia', 'Vacía'),
        ('servida', 'Servida'),
    ]

    codigo = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='vacia'
    )
    activa = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['codigo']

    def __str__(self):
        return self.codigo


class ControlCelo(models.Model):
    DIAS_CICLO = 21
    DIAS_SERVICIO = 1

    cerda = models.ForeignKey(
        Cerda,
        on_delete=models.CASCADE,
        related_name='controles_celo'
    )

    fecha_celo = models.DateField(default=timezone.now)
    en_celo = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    # Fechas calculadas
    fecha_proximo_celo = models.DateField(blank=True, null=True)
    fecha_servicio_recomendada = models.DateField(blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_celo']
        constraints = [
            models.UniqueConstraint(
                fields=['cerda'],
                condition=models.Q(en_celo=True),
                name='una_cerda_un_celo_activo'
            )
        ]

    def save(self, *args, **kwargs):
        # Solo calcular automáticamente al crear
        if not self.pk:
            self.fecha_proximo_celo = (
                self.fecha_celo + timedelta(days=self.DIAS_CICLO)
            )
            self.fecha_servicio_recomendada = (
                self.fecha_celo + timedelta(days=self.DIAS_SERVICIO)
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Celo {self.fecha_celo} - {self.cerda}"
