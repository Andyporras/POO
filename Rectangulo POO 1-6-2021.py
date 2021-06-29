class Rectangulo:
    def __init__(self,ancho,altura):
        self.ancho=ancho
        self.altura=altura
    def calcularArea(self):
        return self.ancho*self.altura
    def calcularPerimetro(self):
        return (self.ancho*2)+(self.altura*2)

class Calculadora:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def Suma(self):
        return self.num1+self.num2
    def resta(self):
        return self.num1-self.num2
    def Multiplicacion(self):
        return self.num1*self.num2
    def Divicion(self):
        return self.num1/self.num2
    def DivicionEntero(self):
        return self.num1//self.num2
    def Potencia(self):
        return self.num1**self.num2
