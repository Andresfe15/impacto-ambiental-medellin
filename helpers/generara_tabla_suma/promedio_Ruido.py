import pandas as pd

def crearTablaHTML(dataFrame, nombreTabla, promedio_rango1, promedio_rango2, promedio_rango3,
                   suma_rango1, suma_rango2, suma_rango3,
                   filtro_rango1, filtro_rango2, filtro_rango3):
    
    # Convertimos el DataFrame en HTML
    archivoHTML = dataFrame.to_html()

    # Convertimos los DataFrames de filtros en HTML
    html_filtro_rango1 = filtro_rango1.to_html()
    html_filtro_rango2 = filtro_rango2.to_html()
    html_filtro_rango3 = filtro_rango3.to_html()

    # Abrimos el archivo HTML en una ruta específica
    archivo = open(f"/tablas_suma_promedio_{nombreTabla}.html", "w")

    # Escribimos la información en el archivo
    archivo.write(
        '''
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Tablas de Suma y Promedio</title>
            </head>
            <body>
        ''')
    
    # Tabla de promedios y sumas
    archivo.write("<h2>Promedios y Sumas</h2>")
    archivo.write("<table>")
    archivo.write("<tr><th></th><th>Valor</th></tr>")
    archivo.write(f"<tr><td>Promedio Rango 1:</td><td>{promedio_rango1}</td></tr>")
    archivo.write(f"<tr><td>Promedio Rango 2:</td><td>{promedio_rango2}</td></tr>")
    archivo.write(f"<tr><td>Promedio Rango 3:</td><td>{promedio_rango3}</td></tr>")
    archivo.write(f"<tr><td>Suma Rango 1:</td><td>{suma_rango1}</td></tr>")
    archivo.write(f"<tr><td>Suma Rango 2:</td><td>{suma_rango2}</td></tr>")
    archivo.write(f"<tr><td>Suma Rango 3:</td><td>{suma_rango3}</td></tr>")
    archivo.write("</table>")
    
    # Tabla de datos filtrados por rango
    archivo.write(f"<h2>Datos con Rango 1</h2>{html_filtro_rango1}<br><br>")
    archivo.write(f"<h2>Datos con Rango 2</h2>{html_filtro_rango2}<br><br>")
    archivo.write(f"<h2>Datos con Rango 3</h2>{html_filtro_rango3}<br><br>")
    
    # Agregamos la tabla original
    archivo.write(archivoHTML)
    
    archivo.write(
        '''
        </body>
        </html>
        '''
    )
    archivo.close()
