#Rutina para generar de forma aleatoria multiples datos con python

import random

def generarDatosCalidadAire():
    listaDatos=[]
    for i in range(1000):
        comuna=random.choice(['comuna 1 Popular', 'comuna 2 Santa Cruz', 'comuna 3 Manrique', 'comuna 4 Aranjuez',
            'comuna 5 Castilla', 'comuna 6 Doce de Octubre', 'comuna 7 Robledo', 'comuna 8 Villa Hermosa',
            'comuna 9 Buenos Aires', 'comuna 10 La Candelaria', 'comuna 11 Laureles-Estadio',
            'comuna 12 La America', 'comuna 13 San Javier', 'comuna 14 Poblado', 'comuna 15 Guayabal',
            'comuna 16 Belen','sin','-'])
        totalPoblacion=random.choice(['3000','4500','5000','10000'])
        tamanoMuestra=random.choice(['1000','2000','3500','6000'])
        ica=random.randint(20,100)
        fecha=random.choice(['2024-05-14','2024-05-15'])
        nombreEncuestado=random.choice(['Pedro Martinez','Sandra Velez','Juan Castro','Sebastian Martinez'])
        id=random.randint(0,1000000)
        calidadAire=[comuna,totalPoblacion,tamanoMuestra,ica,fecha,nombreEncuestado,id]
        
        listaDatos.append(calidadAire)
    return listaDatos
