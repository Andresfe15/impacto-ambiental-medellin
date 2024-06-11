import pandas as pd
from data.generators.generadorEducacionAmbiental import generarDatosEducacionAmbiental
from helpers.generarTabla import crearTablaHTML
import re

def construirDataFrameEducacionAmbiental():
    datosEducacionAmbiental = generarDatosEducacionAmbiental()

    educacionAmbientalDF = pd.DataFrame(datosEducacionAmbiental, columns=['comuna', 'Total Población', 'Institución', 'Fecha', 'Nombre', 'id'])

    educacionAmbientalDF['Total Población'] = educacionAmbientalDF['Total Población'].apply(lambda x: re.sub(r'\D', '', str(x)))

    educacionAmbientalDF['Total Población'] = pd.to_numeric(educacionAmbientalDF['Total Población'], errors='coerce')

    educacionAmbientalDF.dropna(subset=['Total Población'], inplace=True)

    filtroEducacionRango1 = educacionAmbientalDF.query("(`Total Población` >= 0) and (`Total Población` < 25000)")
    filtroEducacionRango2 = educacionAmbientalDF.query("(`Total Población` >= 25000) and (`Total Población` < 50000)")
    filtroEducacionRango3 = educacionAmbientalDF.query("(`Total Población` >= 50000) and (`Total Población` <= 100000)")

    sumaRango1 = filtroEducacionRango1['Total Población'].sum()
    sumaRango2 = filtroEducacionRango2['Total Población'].sum()
    sumaRango3 = filtroEducacionRango3['Total Población'].sum()

    promedioRango1 = filtroEducacionRango1['Total Población'].mean()
    promedioRango2 = filtroEducacionRango2['Total Población'].mean()
    promedioRango3 = filtroEducacionRango3['Total Población'].mean()

    crearTablaHTML(educacionAmbientalDF, "educacionAmbiental")
    crearTablaHTML(filtroEducacionRango1, "filtroEducacionRango1")
    crearTablaHTML(filtroEducacionRango2, "filtroEducacionRango2")
    crearTablaHTML(filtroEducacionRango3, "filtroEducacionRango3")

    sumas_df = pd.DataFrame({
        'Filtro': ['Total Población (0-25000)', 'Total Población (25000-50000)', 'Total Población (50000-100000)'],
        'Suma_Total Población': [sumaRango1, sumaRango2, sumaRango3]
    })

    promedios_df = pd.DataFrame({
        'Filtro': ['Total Población (0-25000)', 'Total Población (25000-50000)', 'Total Población (50000-100000)'],
        'Promedio_Total Población': [promedioRango1, promedioRango2, promedioRango3]
    })

    print("\nTabla de sumas:")
    print(sumas_df)

    print("\nTabla de promedios:")
    print(promedios_df)

    print("\nDatos con Total Población 0-25000:")
    print(filtroEducacionRango1)

    print("\nDatos con Total Población 25000-50000:")
    print(filtroEducacionRango2)

    print("\nDatos con Total Población 50000-100000:")
    print(filtroEducacionRango3)

    crearTablaHTML(sumas_df, "sumas_educacion")
    crearTablaHTML(promedios_df, "promedios_educacion")   

construirDataFrameEducacionAmbiental()

