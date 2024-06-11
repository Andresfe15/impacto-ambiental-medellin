import random

def generarDatosSiembraArboles():
    listDatos = []
    for i in range(500):
        corregimiento = random.choice(['subregion de bajo cauca', 'subregion del medio magdalena', 'subregion del nordeste', 'subregion del occidente', 'subregion de oriente', 'subregion de suroeste', 'subregion del uraba', 'subregion del norte', 'subregio del valle de aburra'])
        nombre = random.choice(['Juan Pablo', 'Valentina Mejia', 'Miguel Paz', 'Andrey Garcia', 'Andres Sanchez'])
        id = random.randint(0, 1000000)
        hectareasSembradasUltimoAño = random.randint(0, 100)
        especiesSembradas = random.choice(['Ceiba (Ceiba pentandra)', 'Guayacán (Tabebuia spp.)', 'Ceroxylon (Ceroxylon spp., palma de cera)', 'Aliso (Alnus acuminata)', 'Nogal cafetero (Cordia alliodora)', 'Guadua (Guadua angustifolia, bambú)', 'Chicalá (Erythrina fusca)', 'Palma de vino (Attalea butyracea)'])
        siembraArboles = [corregimiento, nombre, id, hectareasSembradasUltimoAño, especiesSembradas]
        
        listDatos.append(siembraArboles)
    return listDatos
