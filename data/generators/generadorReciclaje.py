import random

def generarDatosReciclaje():
    listaDatos = []
    for i in range(500):
        comuna = random.choice(['Popular (Comuna 1)', 'Santa Cruz (Comuna 2)', 'Manrique (Comuna 3)', 'Aranjuez (Comuna 4)', 'Castilla (Comuna 5)', 'Doce de Octubre (Comuna 6)', 'Robledo (Comuna 7)', 'Villa Hermosa (Comuna 8)', 'Buenos Aires (Comuna 9)', 'La Candelaria (Comuna 10)', 'Laureles-Estadio (Comuna 11)', 'La América (Comuna 12)', 'San Javier (Comuna 13)', 'El Poblado (Comuna 14)', 'Guayabal (Comuna 15)', 'Belén (Comuna 16)'])
        cantidadDiariaKg = random.choice([5000, 15000, 20000, 2000, 12000, 50000, 70000, 85000, 75000, 60000, 35000, 48000])
        manejoResiduos = random.choice(['papel', 'carton', 'vidrio', 'metal', 'plastico'])

        reciclaje = [comuna, cantidadDiariaKg, manejoResiduos]

        listaDatos.append(reciclaje)
    
    return listaDatos


