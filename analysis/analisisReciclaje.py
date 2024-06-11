import pandas as pd
from data.generators.generadorReciclaje import generarDatosReciclaje
from helpers.generarTabla import crearTablaHTML
import re

def construirDataFrameReciclaje():
    datosReciclaje = generarDatosReciclaje()

    reciclajeDF = pd.DataFrame(datosReciclaje, columns=['comuna', 'Cantidad Kg', 'Manejo residuos'])

    reciclajeDF['Cantidad Kg'] = reciclajeDF['Cantidad Kg'].apply(lambda x: re.sub(r'\D', '', str(x)))

    reciclajeDF['Cantidad Kg'] = pd.to_numeric(reciclajeDF['Cantidad Kg'], errors='coerce')

    reciclajeDF.dropna(subset=['Cantidad Kg'], inplace=True)

    filtroReciclajeRango1 = reciclajeDF.query("(`Cantidad Kg` >= 0) and (`Cantidad Kg` < 25000)")
    filtroReciclajeRango2 = reciclajeDF.query("(`Cantidad Kg` >= 25000) and (`Cantidad Kg` < 50000)")
    filtroReciclajeRango3 = reciclajeDF.query("(`Cantidad Kg` >= 50000) and (`Cantidad Kg` <= 100000)")

    sumaRango1 = filtroReciclajeRango1['Cantidad Kg'].sum()
    sumaRango2 = filtroReciclajeRango2['Cantidad Kg'].sum()
    sumaRango3 = filtroReciclajeRango3['Cantidad Kg'].sum()

    promedioRango1 = filtroReciclajeRango1['Cantidad Kg'].mean()
    promedioRango2 = filtroReciclajeRango2['Cantidad Kg'].mean()
    promedioRango3 = filtroReciclajeRango3['Cantidad Kg'].mean()

    crearTablaHTML(reciclajeDF, "reciclaje")
    crearTablaHTML(filtroReciclajeRango1, "filtroReciclajeRango1")
    crearTablaHTML(filtroReciclajeRango2, "filtroReciclajeRango2")
    crearTablaHTML(filtroReciclajeRango3, "filtroReciclajeRango3")

    sumas_df = pd.DataFrame({
        'Filtro': ['Cantidad Kg (0-25000)', 'Cantidad Kg (25000-50000)', 'Cantidad Kg (50000-100000)'],
        'Suma_Cantidad Kg': [sumaRango1, sumaRango2, sumaRango3]
    })

    promedios_df = pd.DataFrame({
        'Filtro': ['Cantidad Kg (0-25000)', 'Cantidad Kg (25000-50000)', 'Cantidad Kg (50000-100000)'],
        'Promedio_Cantidad Kg': [promedioRango1, promedioRango2, promedioRango3]
    })

    print("\nTabla de sumas:")
    print(sumas_df)

    print("\nTabla de promedios:")
    print(promedios_df)

    print("\nDatos con Cantidad Kg 0-25000:")
    print(filtroReciclajeRango1)

    print("\nDatos con Cantidad Kg 25000-50000:")
    print(filtroReciclajeRango2)

    print("\nDatos con Cantidad Kg 50000-100000:")
    print(filtroReciclajeRango3)

    crearTablaHTML(sumas_df, "sumas_reciclaje")
    crearTablaHTML(promedios_df, "promedios_reciclaje")   


construirDataFrameReciclaje()
