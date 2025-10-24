# models.py
from django.db import models
from datetime import datetime, timedelta

class Cerda(models.Model):
    ESTADO_CHOICES = [
        ('preñada', 'Preñada'),
        ('lactante', 'Lactante'),
        ('vacía', 'Vacía'),
        ('servida', 'Servida'),
    ]
    
    nombre = models.CharField(max_length=100)
    numero_arete = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='vacía')
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.numero_arete})"

class ControlCelo(models.Model):
    cerda = models.ForeignKey(Cerda, on_delete=models.CASCADE, related_name='controles_celo')
    fecha_celo = models.DateField(default=datetime.now)
    fecha_28_dias = models.DateField(blank=True, null=True)
    en_celo = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)
    
    # Fechas calculadas automáticamente
    fecha_proximo_celo = models.DateField(blank=True, null=True)
    fecha_servicio_recomendada = models.DateField(blank=True, null=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_celo']
    
    def save(self, *args, **kwargs):
        # Calcular 28 días si no se puso
        if not self.fecha_28_dias:
            self.fecha_28_dias = self.fecha_celo + timedelta(days=28)
        
        # Calcular otras fechas importantes
        if self.fecha_celo and self.en_celo:
            self.fecha_proximo_celo = self.fecha_celo + timedelta(days=21)
            self.fecha_servicio_recomendada = self.fecha_celo + timedelta(days=1)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Celo de {self.cerda} - {self.fecha_celo}"