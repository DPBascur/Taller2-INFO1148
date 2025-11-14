"""
Módulo de medición y análisis de algoritmos
Permite medir tiempos de ejecución y analizar complejidad
"""

import time
import numpy as np
from typing import Callable, List, Tuple, Dict


def medir_tiempo(algoritmo: Callable, arr: List, repeticiones: int = 3) -> Tuple:
    """
    Mide el tiempo de ejecución de un algoritmo
    
    Args:
        algoritmo: Función del algoritmo a medir
        arr: Arreglo de entrada
        repeticiones: Número de veces que se ejecuta para promediar
        
    Returns:
        tuple: (tiempo_promedio, desviacion_estandar, resultado, comparaciones, operaciones)
    """
    tiempos = []
    resultado = None
    comparaciones = 0
    operaciones = 0
    
    for _ in range(repeticiones):
        arr_copia = arr.copy()
        
        inicio = time.perf_counter()
        resultado, comp, ops = algoritmo(arr_copia)
        fin = time.perf_counter()
        
        tiempos.append(fin - inicio)
        comparaciones = comp
        operaciones = ops
    
    tiempo_promedio = np.mean(tiempos)
    desviacion = np.std(tiempos)
    
    return tiempo_promedio, desviacion, resultado, comparaciones, operaciones


def comparar_algoritmos(algoritmos: Dict[str, Callable], 
                       datos: List, 
                       repeticiones: int = 3) -> Dict:
    """
    Compara múltiples algoritmos con los mismos datos
    
    Args:
        algoritmos: Diccionario con nombre y función de cada algoritmo
        datos: Arreglo de entrada
        repeticiones: Número de repeticiones para cada medición
        
    Returns:
        dict: Diccionario con resultados de cada algoritmo
    """
    resultados = {}
    
    for nombre, algoritmo in algoritmos.items():
        tiempo, desviacion, _, comparaciones, operaciones = medir_tiempo(
            algoritmo, datos, repeticiones
        )
        
        resultados[nombre] = {
            'tiempo': tiempo,
            'desviacion': desviacion,
            'comparaciones': comparaciones,
            'operaciones': operaciones,
            'tamano': len(datos)
        }
    
    return resultados


def analizar_complejidad(algoritmo: Callable, 
                        tamanos: List[int],
                        tipo_datos: str = 'aleatorio',
                        generador: Callable = None) -> List[Dict]:
    """
    Analiza la complejidad de un algoritmo con diferentes tamaños de entrada
    
    Args:
        algoritmo: Función del algoritmo a analizar
        tamanos: Lista de tamaños de entrada a probar
        tipo_datos: Tipo de datos a generar ('aleatorio', 'ordenado', 'inverso')
        generador: Función generadora de datos
        
    Returns:
        list: Lista de diccionarios con resultados para cada tamaño
    """
    from utils.generadores import (
        generar_aleatorio, 
        generar_ordenado, 
        generar_inverso
    )
    
    # Seleccionar generador según tipo
    if generador:
        gen_func = generador
    elif tipo_datos == 'ordenado':
        gen_func = generar_ordenado
    elif tipo_datos == 'inverso':
        gen_func = generar_inverso
    else:
        gen_func = generar_aleatorio
    
    resultados = []
    
    for n in tamanos:
        datos = gen_func(n)
        tiempo, desviacion, _, comparaciones, operaciones = medir_tiempo(
            algoritmo, datos, repeticiones=3
        )
        
        resultados.append({
            'tamano': n,
            'tiempo': tiempo,
            'desviacion': desviacion,
            'comparaciones': comparaciones,
            'operaciones': operaciones
        })
    
    return resultados


def calcular_metricas(resultados: Dict) -> Dict:
    """
    Calcula métricas comparativas entre algoritmos
    
    Args:
        resultados: Diccionario con resultados de comparación
        
    Returns:
        dict: Métricas calculadas
    """
    metricas = {}
    
    # Encontrar el más rápido
    tiempos = {nombre: datos['tiempo'] for nombre, datos in resultados.items()}
    mas_rapido = min(tiempos, key=tiempos.get)
    mas_lento = max(tiempos, key=tiempos.get)
    
    # Calcular speedup
    tiempo_base = tiempos[mas_lento]
    speedups = {
        nombre: tiempo_base / tiempo if tiempo > 0 else float('inf')
        for nombre, tiempo in tiempos.items()
    }
    
    metricas['mas_rapido'] = mas_rapido
    metricas['mas_lento'] = mas_lento
    metricas['speedups'] = speedups
    metricas['diferencia_max'] = tiempos[mas_lento] - tiempos[mas_rapido]
    
    return metricas


def estimar_complejidad_empirica(datos_analisis: List[Dict]) -> str:
    """
    Estima la complejidad empírica basándose en datos de ejecución
    
    Args:
        datos_analisis: Lista de resultados de analizar_complejidad
        
    Returns:
        str: Estimación de la complejidad
    """
    if len(datos_analisis) < 3:
        return "Datos insuficientes"
    
    # Extraer tamaños y tiempos
    tamanos = np.array([d['tamano'] for d in datos_analisis])
    tiempos = np.array([d['tiempo'] for d in datos_analisis])
    
    # Calcular ratios de crecimiento
    ratios_n = []
    for i in range(1, len(tamanos)):
        ratio = tiempos[i] / tiempos[i-1] if tiempos[i-1] > 0 else 0
        ratio_tamano = tamanos[i] / tamanos[i-1]
        ratios_n.append(ratio / ratio_tamano)
    
    ratio_promedio = np.mean(ratios_n)
    
    # Clasificar complejidad
    if ratio_promedio < 1.5:
        return "O(n) - Lineal"
    elif ratio_promedio < 3:
        return "O(n log n) - Logarítmico lineal"
    elif ratio_promedio < 10:
        return "O(n²) - Cuadrática"
    else:
        return "O(n³) o mayor - Cúbica o superior"
