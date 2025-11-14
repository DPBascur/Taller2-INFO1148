"""
Quick Sort (Ordenamiento Rápido)
Complejidad Temporal: O(n log n) en promedio, O(n²) en el peor caso
Complejidad Espacial: O(log n) debido a la recursión

Referencia:
Hoare, C. A. R. (1962). "Quicksort". The Computer Journal, 5(1), 10-16.
https://doi.org/10.1093/comjnl/5.1.10
"""

import sys
import random

def quick_sort(arr):
    """
    Implementa el algoritmo Quick Sort con pivote aleatorio
    para evitar el peor caso con datos ordenados
    
    Args:
        arr (list): Lista de elementos a ordenar
        
    Returns:
        tuple: (lista_ordenada, numero_comparaciones, numero_intercambios)
    """
    arr_copy = arr.copy()
    comparaciones = [0]
    intercambios = [0]
    
    # Aumentar límite de recursión para arreglos grandes
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(max(10000, len(arr_copy) * 2))
    
    def _quick_sort_recursive(arr, low, high):
        """
        Función recursiva auxiliar para Quick Sort
        """
        if low < high:
            # Particionar el arreglo y obtener el índice del pivote
            pi = partition(arr, low, high)
            
            # Ordenar recursivamente los elementos antes y después del pivote
            _quick_sort_recursive(arr, low, pi - 1)
            _quick_sort_recursive(arr, pi + 1, high)
    
    def partition(arr, low, high):
        """
        Función de partición con pivote aleatorio
        """
        # Elegir un pivote aleatorio para evitar O(n²) en datos ordenados
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparaciones[0] += 1
            
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                if i != j:
                    intercambios[0] += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        if (i + 1) != high:
            intercambios[0] += 1
        
        return i + 1
    
    # Llamar a la función recursiva
    _quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    
    # Restaurar límite de recursión
    sys.setrecursionlimit(old_limit)
    
    return arr_copy, comparaciones[0], intercambios[0]


def quick_sort_animacion(arr):
    """
    Versión que retorna los pasos de la ordenación para visualización
    
    Args:
        arr (list): Lista de elementos a ordenar
        
    Returns:
        list: Lista de estados del arreglo en cada paso
    """
    arr_copy = arr.copy()
    pasos = [arr_copy.copy()]
    
    def _quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            pasos.append(arr.copy())
            _quick_sort_recursive(arr, low, pi - 1)
            _quick_sort_recursive(arr, pi + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    return pasos
