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
    

