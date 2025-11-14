"""
Bubble Sort (Ordenamiento Burbuja)
Complejidad Temporal: O(n²) en el peor y caso promedio, O(n) en el mejor caso
Complejidad Espacial: O(1)

Referencia:
Knuth, D. E. (1998). The Art of Computer Programming, Volume 3: 
Sorting and Searching (2nd ed.). Addison-Wesley Professional.
"""

def bubble_sort(arr):
    """
    Implementa el algoritmo Bubble Sort
    
    Args:
        arr (list): Lista de elementos a ordenar
        
    Returns:
        tuple: (lista_ordenada, numero_comparaciones, numero_intercambios)
    """
    # Crear una copia para no modificar el original
    arr_copy = arr.copy()
    n = len(arr_copy)
    comparaciones = 0
    intercambios = 0
    
    # Recorrer todos los elementos del arreglo
    for i in range(n):
        # Flag para optimización: detectar si ya está ordenado
        swapped = False
        
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            comparaciones += 1
            
            # Comparar elementos adyacentes
            if arr_copy[j] > arr_copy[j + 1]:
                # Intercambiar si están en orden incorrecto
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                intercambios += 1
                swapped = True
        
        # Si no hubo intercambios, el arreglo ya está ordenado
        if not swapped:
            break
    
    return arr_copy, comparaciones, intercambios


def bubble_sort_animacion(arr):
    """
    Versión que retorna los pasos de la ordenación para visualización
    
    Args:
        arr (list): Lista de elementos a ordenar
        
    Returns:
        list: Lista de estados del arreglo en cada paso
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    pasos = [arr_copy.copy()]
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                pasos.append(arr_copy.copy())
                swapped = True
        
        if not swapped:
            break
    
    return pasos
