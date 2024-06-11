#Funcion generica para convertir un DataFrame en HTML

def crearTablaHTML(dataFrame,nombreTabla):
    
    #Convertimos el dataFrame en HTML
    archivoHTML=dataFrame.to_html()

    #Abrimos el archivo HTML en una ruta especifica
    archivo=open(f"./tables/{nombreTabla}.html","w")

    #Escribimos la informacion en el archivo
    archivo.write(
        '''
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
        ''')
    archivo.write(archivoHTML)
    archivo.write(

        '''
        </body>
        </html>
        '''
    )
    archivo.close()
        

   