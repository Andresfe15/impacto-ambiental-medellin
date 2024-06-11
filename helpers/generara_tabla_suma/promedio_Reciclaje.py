def crearTablaHTML(dataFrame, nombreTabla, sumaRango1, sumaRango2, sumaRango3, promedioRango1, promedioRango2, promedioRango3,
                   filtroReciclajeRango1, filtroReciclajeRango2, filtroReciclajeRango3):
    
    # Convertimos el DataFrame en HTML
    archivoHTML = dataFrame.to_html()

    # Convertimos los DataFrames de filtros en HTML
    html_filtro_reciclaje_rango1 = filtroReciclajeRango1.to_html()
    html_filtro_reciclaje_rango2 = filtroReciclajeRango2.to_html()
    html_filtro_reciclaje_rango3 = filtroReciclajeRango3.to_html()

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
    archivo.write(f"<tr><td>Promedio Cantidad Kg (0-25000):</td><td>{promedioRango1}</td></tr>")
    archivo.write(f"<tr><td>Promedio Cantidad Kg (25000-50000):</td><td>{promedioRango2}</td></tr>")
    archivo.write(f"<tr><td>Promedio Cantidad Kg (50000-100000):</td><td>{promedioRango3}</td></tr>")
    archivo.write(f"<tr><td>Suma Cantidad Kg (0-25000):</td><td>{sumaRango1}</td></tr>")
    archivo.write(f"<tr><td>Suma Cantidad Kg (25000-50000):</td><td>{sumaRango2}</td></tr>")
    archivo.write(f"<tr><td>Suma Cantidad Kg (50000-100000):</td><td>{sumaRango3}</td></tr>")
    archivo.write("</table>")
    
    # Tabla de datos filtrados por rango de Cantidad Kg
    archivo.write(f"<h2>Datos con Cantidad Kg 0-25000</h2>{html_filtro_reciclaje_rango1}<br><br>")
    archivo.write(f"<h2>Datos con Cantidad Kg 25000-50000</h2>{html_filtro_reciclaje_rango2}<br><br>")
    archivo.write(f"<h2>Datos con Cantidad Kg 50000-100000</h2>{html_filtro_reciclaje_rango3}<br><br>")
    
    # Agregamos la tabla original
    archivo.write(archivoHTML)
    
    archivo.write(
        '''
        </body>
        </html>
        '''
    )
    archivo.close()

