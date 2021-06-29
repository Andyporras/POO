class Reloj:
    def __init__(self):
        self.tipo="Reloj"
        self.hora=0
        self.minuto=0
    def Tipo(self):
        return f"{self.tipo}"

    def Mostrar(self):
        if(self.minuto==0):
            return f"{self.hora}:{self.minuto}0"
        else:
            return f"{self.hora}:{self.minuto}"
    def Set(self,hora,minuto):
        self.hora=hora
        self.minuto=minuto
        return f"{self.hora}:{self.minuto}"
    def actualizarH(self,hora):
        if(hora<13)and hora>=0:
            self.hora=hora
        else:
            return f"Error:la hora debe ser entre 12 o 0"

    def actualizarM(self,minuto):
        if(minuto<60)and minuto>=0:
            self.minuto=minuto
        else:
            return "Error: el minuto debe estar entre 59 a 0"
    def resetH(self):
        self.hora=1
        return f"0{self.hora}:{self.minuto}"
    def resetM(self):
        self.minuto=0
        return f"{self.hora}:{self.minuto}0"
    

class Reloj12h(Reloj):
    def tipo(self):
        return "Resloj12h"
    def avanzarH(self):
        self.hora+=1
        if(self.hora<=12):
            return f"{self.hora}:{self.minuto}"
        else:
            self.hora=1
            return f"{self.hora}:{self.minuto}"
    def avanzarM(self):
        self.minuto+=1
        if(self.minuto<=59):
            return f"{self.hora}:{self.minuto}"
        else:
            if(self.hora+1)<=12:
                self.hora+=1
                self.minuto=0
                return f"{self.hora}:{self.minuto}0"
            else:
                self.hora=1
                self.minuto=0
                return f"{self.hora}:{self.minuto}0"
                



        
        
        
