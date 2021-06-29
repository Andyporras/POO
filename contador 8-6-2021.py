class Acumulador:
    def __init__(self):
        self.valor=0
    def tipo(self):
        return "Acumulador"
    def actualizar(self,valor):
        self.valor+=valor
    def mostrar(self):
        return self.valor
    def reset(self):
        self.valor=0
        return self.valor

from Acumulador import Acumulador

class Medidor(Acumulador):
    def tipo(self):
        return "Medidor"
    def arriba(self):
        self.valor+=1
        return self.valor
    def abajo(self):
        self.valor-=1
        return self.valor
    
