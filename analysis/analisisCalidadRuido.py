import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorRuido import generarRuido
from helpers.generarTabla import crearTablaHTML
import re

def construirDataFrameCalidadRuido():
    # Generar datos de ruido
    datosCalidadRuido = generarRuido()

    # Crear DataFrame
    calidadRuidoDf = pd.DataFrame(datosCalidadRuido, columns=['comuna', 'Total Poblacion', 'Tamaño muestra', 'Desibeles noche', 'Fecha', 'nombre', 'id', 'nombre edificio'])

    # Limpiar la columna 'Desibeles noche' para quedarse solo con los números
    calidadRuidoDf['Desibeles noche'] = calidadRuidoDf['Desibeles noche'].apply(lambda x: re.sub(r'\D', '', str(x)))

    # Convertir 'Desibeles noche' a tipo numérico
    calidadRuidoDf['Desibeles noche'] = pd.to_numeric(calidadRuidoDf['Desibeles noche'], errors='coerce')

    # Filtrar los datos por rangos de decibeles noche
    filtroRango1 = calidadRuidoDf.query("(`Desibeles noche` >= 0) and (`Desibeles noche` < 25)")
    filtroRango2 = calidadRuidoDf.query("(`Desibeles noche` >= 25) and (`Desibeles noche` < 50)")
    filtroRango3 = calidadRuidoDf.query("(`Desibeles noche` >= 50) and (`Desibeles noche` <= 100)")

    # Calcular la suma de los valores para cada filtro
    sumaRango1 = filtroRango1['Desibeles noche'].sum()
    sumaRango2 = filtroRango2['Desibeles noche'].sum()
    sumaRango3 = filtroRango3['Desibeles noche'].sum()

    # Calcular promedios
    promedioRango1 = filtroRango1['Desibeles noche'].mean()
    promedioRango2 = filtroRango2['Desibeles noche'].mean()
    promedioRango3 = filtroRango3['Desibeles noche'].mean()

    # Crear tabla HTML para el DataFrame de calidad de ruido completo
    crearTablaHTML(calidadRuidoDf, "calidadRuido")

    # Crear tabla HTML para el DataFrame de filtroRango1
    crearTablaHTML(filtroRango1, "filtroRango1")

    # Crear tabla HTML para el DataFrame de filtroRango2
    crearTablaHTML(filtroRango2, "filtroRango2")

    # Crear tabla HTML para el DataFrame de filtroRango3
    crearTablaHTML(filtroRango3, "filtroRango3")

    # Crear DataFrames para las sumas y promedios
    sumas_ruido = pd.DataFrame({
        'Filtro': ['Desibeles noche (0-25)', 'Desibeles noche (25-50)', 'Desibeles noche (50-100)'],
        'Suma Desibeles noche': [sumaRango1, sumaRango2, sumaRango3]
    })

    promedios_ruido = pd.DataFrame({
        'Filtro': ['Desibeles noche (0-25)', 'Desibeles noche (25-50)', 'Desibeles noche (50-100)'],
        'Promedio Desibeles noche': [promedioRango1, promedioRango2, promedioRango3]
    })

    # Mostrar los DataFrames de sumas y promedios
    print("\nTabla de sumas:")
    print(sumas_ruido)

    print("\nTabla de promedios:")
    print(promedios_ruido)

    # Mostrar DataFrame de filtroRango1
    print("\nDatos con Desibeles noche 0-25:")
    print(filtroRango1)

    # Mostrar DataFrame de filtroRango2
    print("\nDatos con Desibeles noche 25-50:")
    print(filtroRango2)

    # Mostrar DataFrame de filtroRango3
    print("\nDatos con Desibeles noche 50-100:")
    print(filtroRango3)

    # Crear tabla HTML para las sumas y promedios
    crearTablaHTML(sumas_ruido, "sumas_ruido")
    crearTablaHTML(promedios_ruido, "promedios_ruido")

    #Agrupando datos
    datosAgrupados=calidadRuidoDf.groupby("comuna")["Desibeles noche"].mean()
    
    #Graficando datos
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Calidad de Ruido por comuna en Medellin')
    plt.xlabel('Comuna')
    plt.ylabel('Desibeles noche (Indice Calidad de Ruido)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/calidadRuido.png',format='png',dpi=300)
    #plt.show()

construirDataFrameCalidadRuido()

