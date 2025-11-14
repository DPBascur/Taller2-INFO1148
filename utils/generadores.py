"""
Módulo de generadores de datos
Genera diferentes tipos de arreglos para pruebas
"""

import random
import numpy as np
from typing import List


def generar_aleatorio(n: int, min_val: int = 0, max_val: int = 1000) -> List[int]:
    """
    Genera un arreglo con valores aleatorios
    
    Args:
        n: Tamaño del arreglo
        min_val: Valor mínimo
        max_val: Valor máximo
        
    Returns:
        list: Arreglo con valores aleatorios
    """
    return [random.randint(min_val, max_val) for _ in range(n)]


def generar_ordenado(n: int, min_val: int = 0, max_val: int = 1000) -> List[int]:
    """
    Genera un arreglo ordenado ascendentemente
    
    Args:
        n: Tamaño del arreglo
        min_val: Valor mínimo
        max_val: Valor máximo
        
    Returns:
        list: Arreglo ordenado
    """
    # Generar números espaciados uniformemente
    return sorted([random.randint(min_val, max_val) for _ in range(n)])


def generar_inverso(n: int, min_val: int = 0, max_val: int = 1000) -> List[int]:
    """
    Genera un arreglo ordenado descendentemente (peor caso para algunos algoritmos)
    
    Args:
        n: Tamaño del arreglo
        min_val: Valor mínimo
        max_val: Valor máximo
        
    Returns:
        list: Arreglo ordenado inversamente
    """
    # Generar números espaciados uniformemente en orden inverso
    return sorted([random.randint(min_val, max_val) for _ in range(n)], reverse=True)


def generar_parcialmente_ordenado(n: int, porcentaje_ordenado: float = 0.7) -> List[int]:
    """
    Genera un arreglo parcialmente ordenado
    
    Args:
        n: Tamaño del arreglo
        porcentaje_ordenado: Porcentaje del arreglo que estará ordenado
        
    Returns:
        list: Arreglo parcialmente ordenado
    """
    arr = list(range(n))
    
    # Calcular cuántos elementos desordenar
    num_desordenar = int(n * (1 - porcentaje_ordenado))
    
    # Desordenar aleatoriamente algunos elementos
    for _ in range(num_desordenar):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr


def generar_duplicados(n: int, num_valores_unicos: int = None) -> List[int]:
    """
    Genera un arreglo con muchos valores duplicados
    
    Args:
        n: Tamaño del arreglo
        num_valores_unicos: Número de valores únicos (por defecto n/10)
        
    Returns:
        list: Arreglo con duplicados
    """
    if num_valores_unicos is None:
        num_valores_unicos = max(1, n // 10)
    
    valores = [random.randint(0, 1000) for _ in range(num_valores_unicos)]
    return [random.choice(valores) for _ in range(n)]


def generar_casi_ordenado(n: int, num_swaps: int = None) -> List[int]:
    """
    Genera un arreglo casi ordenado con pocos elementos fuera de lugar
    
    Args:
        n: Tamaño del arreglo
        num_swaps: Número de intercambios aleatorios (por defecto sqrt(n))
        
    Returns:
        list: Arreglo casi ordenado
    """
    if num_swaps is None:
        num_swaps = max(1, int(np.sqrt(n)))
    
    arr = list(range(n))
    
    # Realizar pocos intercambios aleatorios
    for _ in range(num_swaps):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr


def generar_con_patron(n: int, patron: str = 'ascendente-descendente') -> List[int]:
    """
    Genera arreglos con patrones específicos
    
    Args:
        n: Tamaño del arreglo
        patron: Tipo de patrón ('ascendente-descendente', 'dientes-sierra', 'v-shape')
        
    Returns:
        list: Arreglo con el patrón especificado
    """
    if patron == 'ascendente-descendente':
        # Primera mitad ascendente, segunda mitad descendente
        mitad = n // 2
        return list(range(mitad)) + list(range(mitad, 0, -1))
    
    elif patron == 'dientes-sierra':
        # Patrón en zigzag
        arr = []
        for i in range(0, n, 10):
            arr.extend(list(range(10)))
        return arr[:n]
    
    elif patron == 'v-shape':
        # Patrón en V
        mitad = n // 2
        return list(range(mitad, 0, -1)) + list(range(mitad))
    
    else:
        return generar_aleatorio(n)


def generar_dataset_completo(tamano: int) -> dict:
    """
    Genera un conjunto completo de datasets para pruebas exhaustivas
    
    Args:
        tamano: Tamaño de cada arreglo
        
    Returns:
        dict: Diccionario con diferentes tipos de arreglos
    """
    return {
        'Aleatorio': generar_aleatorio(tamano),
        'Ordenado': generar_ordenado(tamano),
        'Inverso': generar_inverso(tamano),
        'Casi Ordenado': generar_casi_ordenado(tamano),
        'Con Duplicados': generar_duplicados(tamano),
        'Parcialmente Ordenado': generar_parcialmente_ordenado(tamano)
    }
