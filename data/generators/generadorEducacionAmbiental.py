import random

def generarDatosEducacionAmbiental():
    listaDatos=[]
    for i in range(500):
       comuna=random.choice(['Popular (Comuna 1)  ' , ' Santa Cruz (Comuna 2) ', ' Manrique (Comuna 3) ',' Aranjuez (Comuna 4)','Castilla (Comuna 5)','Doce de Octubre (Comuna 6) ','Robledo (Comuna 7) ','Villa Hermosa (Comuna 8)','Buenos Aires (Comuna 9) ','La Candelaria (Comuna 10) ','Laureles-Estadio (Comuna 11)','La América (Comuna 12) ','San Javier (Comuna 13)','El Poblado (Comuna 14) ','Guayabal (Comuna 15)','Belén (Comuna 16)'])
       totalpoblacion=random.choice(['10,000 habitantes',' 13,000 habitantes','18,000 habitantes.','80,000 habitantes','130,000 habitantes',' 100,000 habitantes',' 20,000 habitantes',' 30,000 habitantes',' 35,000 habitantes','55,000 habitantes',' 70,000 habitantes','90,000 habitante',' 75,000 habitantes','70,000 habitantes','90,000 habitantes',' 100,000 habitantes'])
       institucion=random.choice(['Rafael Uribe Uribe','Colegio Calasanz','Colegio San ignacio','cesde','itm','Palermo','Corazonista','Colegio la presentacion','INEM','Salazar y Herrera','Montessori','Jorge Robledo'])
       fechaCapacitacion=random.choice(['2024-05-09','2024-05-10','2024-05-11','2024-05-12','2024-05-13'])
       nombreCapacitado=random.choice(['Sebastian Castro','Carolina Mendez','Juan Carlos Perez','Beatriz Muñoz','Marcos Villa','Liliana Toro','Andrea Castro','Andres Perez'])
       id=random.randint(0,1000000)
       educacionAmbiental=[comuna,totalpoblacion,institucion,fechaCapacitacion,nombreCapacitado,id]

       listaDatos.append(educacionAmbiental)
    return listaDatos
