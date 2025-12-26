# admin.py
from django.contrib import admin
from .models import Cerda, ControlCelo


@admin.register(Cerda)
class CerdaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'estado',
        'activa',
        'fecha_nacimiento',
        'fecha_creacion',
    )
    list_filter = ('estado', 'activa')
    search_fields = ('codigo',)
    ordering = ('codigo',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')


@admin.register(ControlCelo)
class ControlCeloAdmin(admin.ModelAdmin):
    list_display = (
        'cerda',
        'fecha_celo',
        'en_celo',
        'fecha_servicio_recomendada',
        'fecha_proximo_celo',
    )
    list_filter = ('en_celo', 'fecha_celo')
    search_fields = ('cerda__codigo',)
    ordering = ('-fecha_celo',)
    readonly_fields = (
        'fecha_servicio_recomendada',
        'fecha_proximo_celo',
        'fecha_creacion',
        'fecha_actualizacion',
    )

    autocomplete_fields = ('cerda',)
