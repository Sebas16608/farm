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
        # Calcular 28 días si no se puso (para seguimiento/post-servicio)
        if not self.fecha_28_dias:
            self.fecha_28_dias = self.fecha_celo + timedelta(days=28)
        
        # Calcular otras fechas importantes
        if self.fecha_celo and self.en_celo:
            # Próximo celo en 18-24 días (ciclo normal de cerdas)
            self.fecha_proximo_celo = self.fecha_celo + timedelta(days=21)
            # Servicio recomendado: 12-24 horas después de detectado el celo
            self.fecha_servicio_recomendada = self.fecha_celo + timedelta(days=1)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Celo de {self.cerda} - {self.fecha_celo}"
    
    @property
    def rango_proximo_celo(self):
        """Devuelve el rango de fechas para el próximo celo"""
        if self.fecha_celo:
            inicio = self.fecha_celo + timedelta(days=18)
            fin = self.fecha_celo + timedelta(days=24)
            return f"{inicio} a {fin}"
        return "No calculado"