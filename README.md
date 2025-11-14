# Taller 2 - Complejidad Algorítmica
## INFO1148 - Teoría de la Computación
### Semestre II-2025

## Herramienta de Experimentación: Algoritmos de Ordenamiento

### Descripción del Proyecto
Esta herramienta implementa tres algoritmos clásicos de ordenamiento para realizar mediciones experimentales. Los datos obtenidos deben usarse en el informe para análisis teórico y comparación.

### Algoritmos Seleccionados

#### 1. Bubble Sort (Ordenamiento Burbuja)
**Descripción:** Algoritmo de ordenamiento simple que compara repetidamente pares de elementos adyacentes y los intercambia si están en el orden incorrecto.

**Complejidad Temporal:**
- Mejor caso: O(n) - cuando el arreglo ya está ordenado
- Caso promedio: O(n²)
- Peor caso: O(n²)

**Complejidad Espacial:** O(1) - ordenamiento in-place

**Referencia:** Knuth, D. E. (1998). *The Art of Computer Programming, Volume 3: Sorting and Searching* (2nd ed.). Addison-Wesley Professional. ISBN 0-201-89685-0.

#### 2. Quick Sort (Ordenamiento Rápido)
**Descripción:** Algoritmo de divide y conquista que selecciona un elemento como pivote y particiona el arreglo alrededor del pivote, colocando elementos menores a la izquierda y mayores a la derecha.

**Complejidad Temporal:**
- Mejor caso: O(n log n)
- Caso promedio: O(n log n)
- Peor caso: O(n²) - cuando el pivote siempre es el menor o mayor elemento

**Complejidad Espacial:** O(log n) - debido a la recursión

**Referencia:** Hoare, C. A. R. (1962). "Quicksort". *The Computer Journal*, 5(1), 10-16. https://doi.org/10.1093/comjnl/5.1.10

#### 3. Merge Sort (Ordenamiento por Mezcla)
**Descripción:** Algoritmo de divide y conquista que divide recursivamente el arreglo en mitades, las ordena y luego las combina de manera ordenada.

**Complejidad Temporal:**
- Mejor caso: O(n log n)
- Caso promedio: O(n log n)
- Peor caso: O(n log n)

**Complejidad Espacial:** O(n) - requiere espacio adicional para la mezcla

**Referencia:** Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. ISBN 978-0-262-03384-8.

### Clasificación de Complejidad
- **Bubble Sort:** Pertenece a la clase de complejidad O(n²), considerado ineficiente para conjuntos de datos grandes. Útil solo para propósitos educativos o datasets muy pequeños.
- **Quick Sort:** En promedio O(n log n), pero puede degradarse a O(n²). Ampliamente utilizado por su eficiencia práctica y buen uso de caché.
- **Merge Sort:** Garantiza O(n log n) en todos los casos. Estable y predecible, ideal cuando se requiere rendimiento consistente.

### Estructura del Proyecto
```
Taller2-INFO1148/
│
├── README.md
├── requirements.txt
├── app.py                      # Aplicación principal Streamlit
│
├── algoritmos/                 # Módulo de algoritmos
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   └── merge_sort.py
│
├── analisis/                   # Módulo de análisis
│   ├── __init__.py
│   ├── medicion.py
│   └── visualizacion.py
│
└── utils/                      # Utilidades
    ├── __init__.py
    └── generadores.py
```

### Instalación y Ejecución

#### Requisitos
- Python 3.8 o superior

#### Instalación
```bash
pip install -r requirements.txt
```

#### Ejecución
```bash
streamlit run app.py
```

### Características de la Aplicación
- ✅ Implementación de tres algoritmos de ordenamiento
- ✅ Medición experimental de tiempos de ejecución
- ✅ Gráficos para incluir en el informe
- ✅ Tablas de datos experimentales
- ✅ Generación de datos de prueba (aleatorios, ordenados, etc.)
- ✅ Análisis de escalabilidad

### Uso de la Herramienta
1. **Ejecución Simple:** Mide los algoritmos con un tamaño y tipo de datos específico
2. **Análisis de Escalabilidad:** Mide cómo crece el tiempo con diferentes tamaños

### Importante para el Informe
- Los gráficos y tablas generados deben incluirse en el informe
- El análisis teórico (Big-O, comparación, conclusiones) se hace en el informe
- Las referencias bibliográficas están documentadas para citar en el informe

### Referencias Adicionales
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley Professional.
- Skiena, S. S. (2008). *The Algorithm Design Manual* (2nd ed.). Springer.
- IEEE Standard 754-2019 - IEEE Standard for Floating-Point Arithmetic

### Autor
Repositorio: DPBascur/Taller3-INFO1148

### Licencia
Proyecto académico - INFO1148 UCSC