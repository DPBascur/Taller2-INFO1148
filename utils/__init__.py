"""
Módulo de utilidades
Contiene generadores de datos y funciones auxiliares
"""

from .generadores import (
    generar_aleatorio,
    generar_ordenado,
    generar_inverso,
    generar_parcialmente_ordenado
)

__all__ = [
    'generar_aleatorio',
    'generar_ordenado',
    'generar_inverso',
    'generar_parcialmente_ordenado'
]
