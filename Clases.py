class Reparto:

    totalReparto=0
    
    def __init__(self,nombre,sexo,fechaN):
        self.nombre=nombre
        self.sexo=sexo
        self.fechaN=fechaN
        Reparto.totalReparto+=1

    def mostrarReparto(self):
        return Reparto.totalReparto
    
        
class Actores(Reparto:
    def __init__(self,nombre,sexo,fechaN,estatura):
        Reparto.__init__(nombre,sexo,fechaN)
        self.esperiencia=experiencia

    def mostrar(self):
        return ""


class Directores(Reparto):
    def __init__(self,nombre,sexo,fechaN,experiencia):
        Reparto.__init__(nombre,sexo,fechaN)
        self.experiencia=experiencia

    def mostrar(self):
        return ""
    


class Utileros:
    
