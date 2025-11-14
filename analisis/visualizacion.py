"""
Módulo de visualización de resultados
Genera gráficos comparativos y de crecimiento asintótico
"""

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from typing import Dict, List


def graficar_comparacion(resultados: Dict, titulo: str = "Comparación de Algoritmos") -> go.Figure:
    """
    Crea un gráfico de barras comparando tiempos de ejecución
    
    Args:
        resultados: Diccionario con resultados de comparación
        titulo: Título del gráfico
        
    Returns:
        Figure: Objeto de gráfico Plotly
    """
    nombres = list(resultados.keys())
    tiempos = [resultados[nombre]['tiempo'] * 1000 for nombre in nombres]  # Convertir a ms
    desviaciones = [resultados[nombre]['desviacion'] * 1000 for nombre in nombres]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=nombres,
        y=tiempos,
        error_y=dict(type='data', array=desviaciones),
        marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1'],
        text=[f'{t:.4f} ms' for t in tiempos],
        textposition='outside'
    ))
    
    fig.update_layout(
        title=titulo,
        xaxis_title="Algoritmo",
        yaxis_title="Tiempo de Ejecución (ms)",
        template="plotly_white",
        height=500,
        showlegend=False
    )
    
    return fig


def graficar_comparacion_operaciones(resultados: Dict) -> go.Figure:
    """
    Crea un gráfico comparando comparaciones y operaciones
    
    Args:
        resultados: Diccionario con resultados de comparación
        
    Returns:
        Figure: Objeto de gráfico Plotly
    """
    nombres = list(resultados.keys())
    comparaciones = [resultados[nombre]['comparaciones'] for nombre in nombres]
    operaciones = [resultados[nombre]['operaciones'] for nombre in nombres]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Comparaciones',
        x=nombres,
        y=comparaciones,
        marker_color='#FF6B6B'
    ))
    
    fig.add_trace(go.Bar(
        name='Intercambios/Movimientos',
        x=nombres,
        y=operaciones,
        marker_color='#4ECDC4'
    ))
    
    fig.update_layout(
        title="Comparación de Operaciones",
        xaxis_title="Algoritmo",
        yaxis_title="Número de Operaciones",
        barmode='group',
        template="plotly_white",
        height=500
    )
    
    return fig


def graficar_crecimiento_asintotico(datos_analisis: Dict[str, List[Dict]]) -> go.Figure:
    """
    Crea un gráfico mostrando el crecimiento asintótico de múltiples algoritmos
    
    Args:
        datos_analisis: Diccionario con nombre de algoritmo y sus datos de análisis
        
    Returns:
        Figure: Objeto de gráfico Plotly
    """
    fig = go.Figure()
    
    colores = {
        'Bubble Sort': '#FF6B6B',
        'Quick Sort': '#4ECDC4',
        'Merge Sort': '#45B7D1'
    }
    
    for nombre, datos in datos_analisis.items():
        tamanos = [d['tamano'] for d in datos]
        tiempos = [d['tiempo'] * 1000 for d in datos]  # Convertir a ms
        
        fig.add_trace(go.Scatter(
            x=tamanos,
            y=tiempos,
            mode='lines+markers',
            name=nombre,
            line=dict(width=3, color=colores.get(nombre, '#95a5a6')),
            marker=dict(size=8)
        ))
    
    fig.update_layout(
        title="Crecimiento Asintótico de Algoritmos",
        xaxis_title="Tamaño de Entrada (n)",
        yaxis_title="Tiempo de Ejecución (ms)",
        template="plotly_white",
        height=600,
        hovermode='x unified',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )
    
    return fig


def graficar_complejidad_teorica(tamano_max: int = 1000) -> go.Figure:
    """
    Grafica las complejidades teóricas para comparación
    
    Args:
        tamano_max: Tamaño máximo de entrada a graficar
        
    Returns:
        Figure: Objeto de gráfico Plotly
    """
    n = np.linspace(1, tamano_max, 100)
    
    fig = go.Figure()
    
    # O(n)
    fig.add_trace(go.Scatter(
        x=n,
        y=n,
        mode='lines',
        name='O(n) - Lineal',
        line=dict(dash='dash', width=2)
    ))
    
    # O(n log n)
    fig.add_trace(go.Scatter(
        x=n,
        y=n * np.log2(n),
        mode='lines',
        name='O(n log n) - Linearítmico',
        line=dict(dash='dash', width=2)
    ))
    
    # O(n²)
    fig.add_trace(go.Scatter(
        x=n,
        y=n ** 2,
        mode='lines',
        name='O(n²) - Cuadrático',
        line=dict(dash='dash', width=2)
    ))
    
    fig.update_layout(
        title="Complejidades Teóricas - Notación Big-O",
        xaxis_title="Tamaño de Entrada (n)",
        yaxis_title="Operaciones",
        template="plotly_white",
        height=600,
        yaxis_type="log",
        hovermode='x unified'
    )
    
    return fig


def crear_tabla_comparativa(resultados: Dict) -> pd.DataFrame:
    """
    Crea una tabla DataFrame con los resultados comparativos
    
    Args:
        resultados: Diccionario con resultados de comparación
        
    Returns:
        DataFrame: Tabla con resultados formateados
    """
    datos = []
    
    for nombre, res in resultados.items():
        datos.append({
            'Algoritmo': nombre,
            'Tiempo (ms)': f"{res['tiempo'] * 1000:.4f}",
            'Desviación (ms)': f"{res['desviacion'] * 1000:.4f}",
            'Comparaciones': f"{res['comparaciones']:,}",
            'Operaciones': f"{res['operaciones']:,}",
            'Tamaño': f"{res['tamano']:,}"
        })
    
    return pd.DataFrame(datos)


def graficar_heatmap_rendimiento(datos_multiple: Dict[str, Dict]) -> go.Figure:
    """
    Crea un heatmap comparando algoritmos en diferentes escenarios
    
    Args:
        datos_multiple: Diccionario anidado con escenarios y resultados
        
    Returns:
        Figure: Objeto de gráfico Plotly
    """
    # Preparar datos para el heatmap
    algoritmos = list(next(iter(datos_multiple.values())).keys())
    escenarios = list(datos_multiple.keys())
    
    tiempos = []
    for escenario in escenarios:
        tiempos.append([
            datos_multiple[escenario][algo]['tiempo'] * 1000 
            for algo in algoritmos
        ])
    
    fig = go.Figure(data=go.Heatmap(
        z=tiempos,
        x=algoritmos,
        y=escenarios,
        colorscale='RdYlGn_r',
        text=[[f'{val:.3f} ms' for val in row] for row in tiempos],
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Tiempo (ms)")
    ))
    
    fig.update_layout(
        title="Mapa de Calor: Rendimiento por Escenario",
        xaxis_title="Algoritmo",
        yaxis_title="Escenario",
        height=400
    )
    
    return fig
