def crearTablaHTML(dataFrame, nombreTabla, promedio_ica_positivo, promedio_ica_moderado, promedio_ica_peligroso,
                   suma_ica_positivo, suma_ica_moderado, suma_ica_peligroso,
                   filtro_ica_positivo, filtro_ica_moderado, filtro_ica_peligroso):
    
    # Convertimos el DataFrame en HTML
    archivoHTML = dataFrame.to_html()

    # Convertimos los DataFrames de filtros en HTML
    html_filtro_ica_positivo = filtro_ica_positivo.to_html()
    html_filtro_ica_moderado = filtro_ica_moderado.to_html()
    html_filtro_ica_peligroso = filtro_ica_peligroso.to_html()

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
    archivo.write(f"<tr><td>Promedio ICA Positivo (20-50):</td><td>{promedio_ica_positivo}</td></tr>")
    archivo.write(f"<tr><td>Promedio ICA Moderado (50-70):</td><td>{promedio_ica_moderado}</td></tr>")
    archivo.write(f"<tr><td>Promedio ICA Peligroso (70+):</td><td>{promedio_ica_peligroso}</td></tr>")
    archivo.write(f"<tr><td>Suma ICA Positivo:</td><td>{suma_ica_positivo}</td></tr>")
    archivo.write(f"<tr><td>Suma ICA Moderado:</td><td>{suma_ica_moderado}</td></tr>")
    archivo.write(f"<tr><td>Suma ICA Peligroso:</td><td>{suma_ica_peligroso}</td></tr>")
    archivo.write("</table>")
    
    # Tabla de datos filtrados por rango de ICA
    archivo.write(f"<h2>Datos con ICA Positivo (20-50)</h2>{html_filtro_ica_positivo}<br><br>")
    archivo.write(f"<h2>Datos con ICA Moderado (50-70)</h2>{html_filtro_ica_moderado}<br><br>")
    archivo.write(f"<h2>Datos con ICA Peligroso (70+)</h2>{html_filtro_ica_peligroso}<br><br>")
    
    # Agregamos la tabla original
    archivo.write(archivoHTML)
    
    archivo.write(
        '''
        </body>
        </html>
        '''
    )
    archivo.close()
