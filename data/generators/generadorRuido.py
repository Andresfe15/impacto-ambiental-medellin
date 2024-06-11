import random

def generarRuido ():
    listaDatos=[]
    for i in range(500):
        comuna=random.choice(['Popular (Comuna 1)  ' , ' Santa Cruz (Comuna 2) ', ' Manrique (Comuna 3) ',' Aranjuez (Comuna 4)','Castilla (Comuna 5)','Doce de Octubre (Comuna 6) ','Robledo (Comuna 7) ','Villa Hermosa (Comuna 8)','Buenos Aires (Comuna 9) ','La Candelaria (Comuna 10) ','Laureles-Estadio (Comuna 11)','La America (Comuna 12) ','San Javier (Comuna 13)','El Poblado (Comuna 14) ','Guayabal (Comuna 15)','Belen (Comuna 16)'])
        totalpoblacion=random.choice(['150,000 habitantes',' 130,000 habitantes','180,000 habitantes.','80,000 habitantes','130,000 habitantes',' 100,000 habitantes',' 200,000 habitantes',' 120,000 habitantes',' 130,000 habitantes','55,000 habitantes',' 130,000 habitantes','90,000 habitante',' 170,000 habitantes','150,000 habitantes','130,000 habitantes',' 170,000 habitantes'])
        tamañoMuestra=random.choice(['700','600','250','120','78'])
        decibelesNoche=random.choice(['70 decibeles','25 decibeles',' 10 decibeles ','70 decibeles','52 decibeles','65 decibeles ','920 decibeles',' 75 decibeles ','15 decibeles','80 decibeles',' 45 decibeles ','70 decibeles','75 decibeles ','10 decibeles'])
        fechaEncuesta=random.choice(['2024-02-15','2024-02-28','2024-02-18','2024-03-10','2024-03-12','2024-04-02','2024-05-01','2024-01-13','2024-02-20','2024-01-25','2024-01-25','2024-03-08','2024-03-05','2024-04-26','2024-05-14'])
        nombre=random.choice(['andrey','andres','miguel','alexander','edwin','alberto','julian','juan jose','jose','duvan','juaquin','julbrinner','mariana','adriana','elizabeth','lena'])
        id=random.randint(0,1000000)
        nombreEdificios=random.choice(['laureles','san martin','pedregalito', 'senseros de almeria'])
        calidadRuido=[comuna,totalpoblacion,tamañoMuestra,decibelesNoche,fechaEncuesta,nombre,id,nombreEdificios]

        listaDatos.append(calidadRuido)
    return listaDatos
