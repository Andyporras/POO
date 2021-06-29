class PersonaFutbol:
    cantidadPersonas=0
    equipo="ND"

    def __init__(self,cedula,nombre):
        self.cedula=cedula
        self.nombre=nombre
        PersonaFutbol.cantidadPersonas+=1
    def setEquipo(equipo):
        personaFutbol.equipo=equipo

class Entrenador(PersonaFutbol):
    def __init__(self,cedula,nombre,idFifa):
        PersonaFutbol.__init__(self,cedula,nombre)
        self.idFifa=idFifa

class Futbolista(PersonaFutbol):
    def __init__(self,cedula,nombre,dorsal):
        PersonaFutbol.__init__(self,cedula,nombre)
        self.dorsal=dorsal
        
