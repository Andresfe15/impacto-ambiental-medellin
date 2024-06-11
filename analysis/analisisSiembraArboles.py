import pandas as pd
from data.generators.generadorSiembraArboles import generarDatosSiembraArboles
from helpers.generarTabla import crearTablaHTML

def construirDataFrameSiembraArboles():
    datosSiembraArboles = generarDatosSiembraArboles()

    siembraArbolesDF = pd.DataFrame(datosSiembraArboles, columns=['Corregimiento', 'Nombre', 'id', 'Hectareas sembradas', 'Especie sembreada'])

    SiembraRango1 = siembraArbolesDF.query("(`Hectareas sembradas` >= 0) and (`Hectareas sembradas` < 10)")
    SiembraRango2 = siembraArbolesDF.query("(`Hectareas sembradas` >= 10) and (`Hectareas sembradas` < 50)")
    SiembraRango3 = siembraArbolesDF.query("(`Hectareas sembradas` >= 50) and (`Hectareas sembradas` <= 100)")

    sumaRango1 = SiembraRango1['Hectareas sembradas'].sum()
    sumaRango2 = SiembraRango2['Hectareas sembradas'].sum()
    sumaRango3 = SiembraRango3['Hectareas sembradas'].sum()

    promedioRango1 = SiembraRango1['Hectareas sembradas'].mean()
    promedioRango2 = SiembraRango2['Hectareas sembradas'].mean()
    promedioRango3 = SiembraRango3['Hectareas sembradas'].mean()

    crearTablaHTML(siembraArbolesDF, "siembra arboles")
    crearTablaHTML(SiembraRango1, "SiembraRango1")
    crearTablaHTML(SiembraRango2, "SiembraRango2")
    crearTablaHTML(SiembraRango3, "SiembraRango3")
    
    sumas_df = pd.DataFrame({
        'Filtro': ['Hectareas Sembradas (0-10)', 'Hectareas Sembradas (10-50)', 'Hectareas Sembradas (50-100)'],
        'Suma_Hectareas Sembradas': [sumaRango1, sumaRango2, sumaRango3]
    })

    promedios_df = pd.DataFrame({
        'Filtro': ['Hectareas Sembradas (0-10)', 'Hectareas Sembradas (10-50)', 'Hectareas Sembradas (50-100)'],
        'Promedio_Hectareas Sembradas': [promedioRango1, promedioRango2, promedioRango3]
    })

    print("\nTabla de sumas:")
    print(sumas_df)

    print("\nTabla de promedios:")
    print(promedios_df)

    print("\nDatos con Hectareas Sembradas 0-10:")
    print(SiembraRango1)

    print("\nDatos con Hectareas Sembradas 10-50:")
    print(SiembraRango2)

    print("\nDatos con Hectareas Sembradas 50-100:")
    print(SiembraRango3)

    crearTablaHTML(sumas_df, "sumas_siembra_arboles")
    crearTablaHTML(promedios_df, "promedios_siembra_arboles")   


construirDataFrameSiembraArboles()

