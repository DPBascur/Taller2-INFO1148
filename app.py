"""
Aplicación Streamlit para Análisis de Complejidad Algorítmica
Taller 2 - INFO1148 - Teoría de la Computación

Herramienta práctica para ejecutar y medir algoritmos de ordenamiento
Los datos obtenidos deben usarse en el informe para análisis y comparación

Fecha: Noviembre 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
from algoritmos import bubble_sort, quick_sort, merge_sort
from analisis.medicion import (
    comparar_algoritmos, 
    analizar_complejidad, 
    calcular_metricas,
    estimar_complejidad_empirica
)
from analisis.visualizacion import (
    graficar_comparacion, 
    graficar_comparacion_operaciones,
    graficar_crecimiento_asintotico,
    crear_tabla_comparativa
)
from utils.generadores import (
    generar_aleatorio,
    generar_ordenado,
    generar_inverso,
    generar_casi_ordenado,
    generar_duplicados
)


# Configuración de la página
st.set_page_config(
    page_title="Análisis de Complejidad Algorítmica",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


def main():
    # Título principal
    st.markdown('<h1 class="main-header">📊 Medición de Algoritmos de Ordenamiento</h1>', 
                unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #7f8c8d;">Taller 2 - INFO1148 - Herramienta de Experimentación</p>', 
                unsafe_allow_html=True)
    
    st.info("💡 **Instrucciones:** Esta herramienta ejecuta los algoritmos y genera datos experimentales. Usa estos resultados en tu informe para análisis y comparación teórica.")
    
    # Sidebar - Configuración
    with st.sidebar:
        st.header("⚙️ Configuración")
        
        # Selección de modo
        modo = st.radio(
            "Modo de Ejecución:",
            ["Ejecución Simple", "Análisis de Escalabilidad"]
        )
        
        st.divider()
        
        # Configuración de datos
        st.subheader("Configuración de Datos")
        
        tamano = st.slider(
            "Tamaño del arreglo:",
            min_value=10,
            max_value=10000,
            value=1000,
            step=10,
            help="Tamaño de los datos a ordenar"
        )
        
        tipo_datos = st.selectbox(
            "Tipo de datos:",
            ["Aleatorio", "Ordenado", "Inverso", "Casi Ordenado", "Con Duplicados"]
        )
        
        st.divider()
        
        # Selección de algoritmos
        st.subheader("Algoritmos a Comparar")
        
        usar_bubble = st.checkbox("Bubble Sort", value=True)
        usar_quick = st.checkbox("Quick Sort", value=True)
        usar_merge = st.checkbox("Merge Sort", value=True)
        
        st.divider()
        
        # Información
        with st.expander("ℹ️ Sobre los Algoritmos"):
            st.markdown("""
            **Algoritmos Implementados:**
            - **Bubble Sort:** O(n²) - Simple, educativo
            - **Quick Sort:** O(n log n) promedio - Eficiente en práctica
            - **Merge Sort:** O(n log n) garantizado - Estable
            
            **Nota:** Los datos obtenidos son para uso en tu informe.
            El análisis teórico y comparación se hace en el documento.
            """)
    
    # Contenido principal según el modo seleccionado
    if modo == "Ejecución Simple":
        mostrar_ejecucion_simple(tamano, tipo_datos, usar_bubble, usar_quick, usar_merge)
    
    elif modo == "Análisis de Escalabilidad":
        mostrar_analisis_escalabilidad(usar_bubble, usar_quick, usar_merge)


def mostrar_ejecucion_simple(tamano, tipo_datos, usar_bubble, usar_quick, usar_merge):
    """Ejecuta los algoritmos y muestra resultados experimentales"""
    st.markdown('<h2 class="sub-header">⚡ Ejecución y Medición de Algoritmos</h2>', 
                unsafe_allow_html=True)
    
    # Generar datos según el tipo seleccionado
    if tipo_datos == "Aleatorio":
        datos = generar_aleatorio(tamano)
    elif tipo_datos == "Ordenado":
        datos = generar_ordenado(tamano)
    elif tipo_datos == "Inverso":
        datos = generar_inverso(tamano)
    elif tipo_datos == "Casi Ordenado":
        datos = generar_casi_ordenado(tamano)
    else:
        datos = generar_duplicados(tamano)
    
    # Mostrar información de los datos
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tamaño del Arreglo", f"{len(datos):,}")
    with col2:
        st.metric("Tipo de Datos", tipo_datos)
    with col3:
        st.metric("Rango de Valores", f"{min(datos)} - {max(datos)}")
    
    # Vista previa de datos (primeros 20 elementos)
    with st.expander("👁️ Ver datos de entrada (primeros 20)"):
        st.write(datos[:20])
    
    st.divider()
    
    # Seleccionar algoritmos
    algoritmos = {}
    if usar_bubble:
        algoritmos["Bubble Sort"] = bubble_sort
    if usar_quick:
        algoritmos["Quick Sort"] = quick_sort
    if usar_merge:
        algoritmos["Merge Sort"] = merge_sort
    
    if not algoritmos:
        st.warning("⚠️ Selecciona al menos un algoritmo para comparar")
        return
    
    # Ejecutar comparación
    with st.spinner("🔄 Ejecutando algoritmos..."):
        resultados = comparar_algoritmos(algoritmos, datos, repeticiones=3)
        metricas = calcular_metricas(resultados)
    
    # Mostrar resultados destacados
    st.success("✅ Análisis completado!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"🏆 **Más Rápido:**  \n{metricas['mas_rapido']}")
    with col2:
        st.warning(f"🐌 **Más Lento:**  \n{metricas['mas_lento']}")
    with col3:
        speedup = metricas['speedups'][metricas['mas_rapido']]
        st.success(f"⚡ **Speedup:**  \n{speedup:.2f}x")
    
    st.divider()
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Tiempos de Ejecución")
        fig_tiempo = graficar_comparacion(resultados)
        st.plotly_chart(fig_tiempo, use_container_width=True)
    
    with col2:
        st.subheader("🔢 Operaciones Realizadas")
        fig_ops = graficar_comparacion_operaciones(resultados)
        st.plotly_chart(fig_ops, use_container_width=True)
    
    # Tabla detallada
    st.subheader("📋 Datos para el Informe")
    tabla = crear_tabla_comparativa(resultados)
    st.dataframe(tabla, use_container_width=True)
    
    st.info("💾 **Tip:** Puedes copiar estos datos directamente a tu informe. Haz clic en la tabla y usa Ctrl+C.")
    
    # Datos adicionales
    st.subheader("📈 Datos Experimentales Detallados")
    
    for nombre, res in resultados.items():
        with st.expander(f"📌 Datos de {nombre}"):
            st.markdown(f"""
            **Mediciones Experimentales:**
            - Tamaño de entrada (n): {res['tamano']:,} elementos
            - Tiempo promedio: {res['tiempo']*1000:.6f} ms
            - Desviación estándar: {res['desviacion']*1000:.6f} ms
            - Comparaciones: {res['comparaciones']:,}
            - Intercambios/Movimientos: {res['operaciones']:,}
            - Tipo de datos: {tipo_datos}
            
            **Usa estos datos en tu informe para:**
            - Tabla de resultados experimentales
            - Gráficos comparativos
            - Análisis de complejidad empírica
            """)


def mostrar_analisis_escalabilidad(usar_bubble, usar_quick, usar_merge):
    """Analiza cómo escalan los algoritmos con diferentes tamaños"""
    st.markdown('<h2 class="sub-header">📈 Análisis de Escalabilidad</h2>', 
                unsafe_allow_html=True)
    
    st.info("""
    📊 **Objetivo:** Medir cómo crece el tiempo de ejecución al aumentar el tamaño de entrada.
    Usa estos datos en tu informe para graficar el crecimiento y comparar con la teoría.
    """)
    
    # Configuración del análisis
    col1, col2 = st.columns(2)
    with col1:
        tamanos = st.multiselect(
            "Tamaños de entrada a probar:",
            [100, 250, 500, 750, 1000, 1500, 2000, 3000],
            default=[100, 500, 1000, 2000]
        )
    with col2:
        tipo_analisis = st.selectbox(
            "Tipo de datos:",
            ["aleatorio"]
        )
        st.caption("⚠️ Solo aleatorio para evitar O(n²) en Quick Sort")
    
    if not tamanos:
        st.warning("⚠️ Selecciona al menos un tamaño para analizar")
        return
    
    tamanos = sorted(tamanos)
    
    # Seleccionar algoritmos
    algoritmos_analisis = {}
    if usar_bubble and max(tamanos) <= 3000:  # Limitar Bubble Sort
        algoritmos_analisis["Bubble Sort"] = bubble_sort
    elif usar_bubble:
        st.warning("⚠️ Bubble Sort deshabilitado para tamaños > 3000 (muy lento)")
    
    if usar_quick:
        algoritmos_analisis["Quick Sort"] = quick_sort
    if usar_merge:
        algoritmos_analisis["Merge Sort"] = merge_sort
    
    if not algoritmos_analisis:
        st.warning("⚠️ Selecciona al menos un algoritmo")
        return
    
    # Ejecutar análisis
    if st.button("🚀 Ejecutar Medición de Escalabilidad", type="primary"):
        resultados_complejidad = {}
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        total_pasos = len(algoritmos_analisis) * len(tamanos)
        paso_actual = 0
        
        for nombre, algoritmo in algoritmos_analisis.items():
            status_text.text(f"Midiendo {nombre}...")
            
            resultados = analizar_complejidad(
                algoritmo, 
                tamanos, 
                tipo_datos=tipo_analisis
            )
            resultados_complejidad[nombre] = resultados
            
            for _ in tamanos:
                paso_actual += 1
                progress_bar.progress(paso_actual / total_pasos)
        
        progress_bar.empty()
        status_text.empty()
        
        st.success("✅ Medición completada!")
        
        # Gráfico de crecimiento
        st.subheader("📊 Curva de Crecimiento")
        fig_crecimiento = graficar_crecimiento_asintotico(resultados_complejidad)
        st.plotly_chart(fig_crecimiento, use_container_width=True)
        
        st.info("💡 Usa este gráfico en tu informe para mostrar el comportamiento experimental")
        
        # Tabla de resultados
        st.subheader("📋 Tabla de Datos Experimentales")
        
        for nombre, datos in resultados_complejidad.items():
            with st.expander(f"📊 Datos de {nombre}"):
                df = pd.DataFrame(datos)
                df['tiempo_ms'] = df['tiempo'] * 1000
                df_mostrar = df[['tamano', 'tiempo_ms', 'comparaciones', 'operaciones']].copy()
                df_mostrar.columns = ['Tamaño (n)', 'Tiempo (ms)', 'Comparaciones', 'Operaciones']
                st.dataframe(df_mostrar, use_container_width=True)
                
                st.markdown("""
                **Copia esta tabla a tu informe para:**
                - Mostrar resultados experimentales
                - Comparar con complejidad teórica
                - Calcular ratios de crecimiento
                """)




# Ejecutar aplicación
if __name__ == "__main__":
    main()

