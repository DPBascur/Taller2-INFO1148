"""
Merge Sort (Ordenamiento por Mezcla)
Complejidad Temporal: O(n log n) en todos los casos
Complejidad Espacial: O(n)

Referencia:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). 
Introduction to Algorithms (3rd ed.). MIT Press.
"""

def merge_sort(arr):
    """
    Implementa el algoritmo Merge Sort
    
    Args:
        arr (list): Lista de elementos a ordenar
        
    Returns:
        tuple: (lista_ordenada, numero_comparaciones, numero_intercambios)
    """
    arr_copy = arr.copy()
    comparaciones = [0]  # Usar lista para mantener referencia en recursión
    movimientos = [0]    # En merge sort contamos movimientos en lugar de intercambios
    
    def _merge_sort_recursive(arr, left, right):
        """
        Función recursiva auxiliar para Merge Sort
        """
        if left < right:
            # Encontrar el punto medio
            mid = (left + right) // 2
            
            # Ordenar recursivamente las dos mitades
            _merge_sort_recursive(arr, left, mid)
            _merge_sort_recursive(arr, mid + 1, right)
            
            # Mezclar las mitades ordenadas
            merge(arr, left, mid, right)
    
    def merge(arr, left, mid, right):
        """
        Función que mezcla dos subarreglos ordenados
        arr[left:mid+1] y arr[mid+1:right+1]
        """
        # Crear copias de los subarreglos
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        # Índices para recorrer los subarreglos
        i = 0  # Índice inicial del primer subarreglo
        j = 0  # Índice inicial del segundo subarreglo
        k = left  # Índice inicial del arreglo mezclado
        
        # Mezclar los elementos en orden
        while i < len(left_arr) and j < len(right_arr):
            comparaciones[0] += 1
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            
            movimientos[0] += 1
            k += 1
        
        # Copiar los elementos restantes de left_arr, si hay alguno
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            movimientos[0] += 1
        
        # Copiar los elementos restantes de right_arr, si hay alguno
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            movimientos[0] += 1
    
    # Llamar a la función recursiva
    _merge_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    
    return arr_copy, comparaciones[0], movimientos[0]


def merge_sort_animacion(arr):
    """
    Versión que retorna los pasos de la ordenación para visualización
    
    Args:
        arr (list): Lista de elementos a ordenar
        
    Returns:
        list: Lista de estados del arreglo en cada paso
    """
    arr_copy = arr.copy()
    pasos = [arr_copy.copy()]
    
    def _merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            _merge_sort_recursive(arr, left, mid)
            _merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)
            pasos.append(arr.copy())
    
    def merge(arr, left, mid, right):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    _merge_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    return pasos
