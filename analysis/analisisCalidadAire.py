import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorCalidadAire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML

def construirDataFrameCalidadAire():
    # Traigo los datos generados en el mock
    datosCalidadAire = generarDatosCalidadAire()
    
    # Construyo el dataframe
    calidadAireDF = pd.DataFrame(datosCalidadAire, columns=['comuna', 'Total Población', 'Tamaño muestra', 'ICA', 'Fecha', 'nombre', 'id'])

    # Limpiando el DataFrame
    calidadAireDF.replace('sin', pd.NA, inplace=True)
    calidadAireDF.dropna(inplace=True)
    calidadAireDF.replace('-', pd.NA, inplace=True)
    calidadAireDF.dropna(inplace=True)

    # Filtrando datos
    filtroIcaPositivo = calidadAireDF.query("(ICA > 20) and (ICA < 50)")
    filtroIcaModerado = calidadAireDF.query("(ICA > 50) and (ICA < 70)")
    filtroIcaPeligroso = calidadAireDF.query("(ICA > 70)")

    # Calcular la suma de los valores para cada filtro
    sumaIcaPositivo = filtroIcaPositivo['ICA'].sum()
    sumaIcaModerado = filtroIcaModerado['ICA'].sum()
    sumaIcaPeligroso = filtroIcaPeligroso['ICA'].sum()

    # Calcular promedios
    promedioIcaPositivo = filtroIcaPositivo['ICA'].mean()
    promedioIcaModerado = filtroIcaModerado['ICA'].mean()
    promedioIcaPeligroso = filtroIcaPeligroso['ICA'].mean()

  
    # Crear tabla HTML para el DataFrame de calidad de aire completo
    crearTablaHTML(calidadAireDF, "calidadAire")

    # Crear tabla HTML para el DataFrame de filtroIcaPositivo
    crearTablaHTML(filtroIcaPositivo, "filtroIcaPositivo")

    # Crear tabla HTML para el DataFrame de filtroIcaModerado
    crearTablaHTML(filtroIcaModerado, "filtroIcaModerado")

    # Crear tabla HTML para el DataFrame de filtroIcaPeligroso
    crearTablaHTML(filtroIcaPeligroso, "filtroIcaPeligroso")

    # Crear DataFrames para las sumas y promedios
    sumas_df = pd.DataFrame({
        'Filtro': ['ICA Positivo (20-50)', 'ICA Moderado (50-70)', 'ICA Peligroso (70+)'],
        'Suma ICA': [sumaIcaPositivo, sumaIcaModerado, sumaIcaPeligroso]
    })

    promedios_df = pd.DataFrame({
        'Filtro': ['ICA Positivo (20-50)', 'ICA Moderado (50-70)', 'ICA Peligroso (70+)'],
        'Promedio ICA': [promedioIcaPositivo, promedioIcaModerado, promedioIcaPeligroso]
    })

    # Mostrar los DataFrames de sumas y promedios
    print("\nTabla de sumas:")
    print(sumas_df)

    print("\nTabla de promedios:")
    print(promedios_df)
    print("\nDatos con ICA Positivo (20-50):")
    print(filtroIcaPositivo)

    # Mostrar DataFrame de filtroIcaModerado
    print("\nDatos con ICA Moderado (50-70):")
    print(filtroIcaModerado)

    # Mostrar DataFrame de filtroIcaPeligroso
    print("\nDatos con ICA Peligroso (70+):")
    print(filtroIcaPeligroso)

    # Crear tabla HTML para las sumas
    crearTablaHTML(sumas_df, "sumas")

    # Crear tabla HTML para los promedios
    crearTablaHTML(promedios_df, "promedios")  

    #Agrupando datos
    datosAgrupados=calidadAireDF.groupby("comuna")["ICA"].mean()
    
    #Graficando datos
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Calidad de aire por comuna en Medellin')
    plt.xlabel('Comuna')
    plt.ylabel('ICA (Indice Calidad de Aire)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./assets/img/calidaaire.png',format='png',dpi=300)
    #plt.show()
    
construirDataFrameCalidadAire()


