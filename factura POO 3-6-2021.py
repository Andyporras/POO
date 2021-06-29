class Factura:
    numeroFactura=0  #varible clse
    def __init__(self):
        Factura.numeroFactura+=1
        self.numeroFactura=Factura.numeroFactura
        self.fecha=""
        self.cliente=""
        self.totalFacturado=0
        self.totalImpuesto=0
        self.listaItem=[]
        #Factura.numeroFactura+=1
        #self #variable instancia
    def crearFactura(self,fecha,cliente):
        #self.numeroFactura=numero
        self.fecha=fecha
        self.cliente=cliente
    def verNumfactura(self):
        return self.numeroFactura

    def agregarItem(self,producto,precioU,cantidad):
        self.listaItem+=[[producto,precioU,cantidad]]

    def verTotal(self):
        subtotal=1
        total=0
        impuesto=0
        for item in self.listaItem:
            subtotal=item[1]*item[2]
            impuesto=subtotal*0.13
            total+=subtotal+impuesto
        self.totalFacturado=total

        return f"Total facturado es de: {total}"
    def cerrarFactura(self):
        return f"Total a pagar es de: {self.totalFacturado}"
    
class Cuenta:
    cantidadCuentas=0
    def __init__(self,saldoInicial):
        self.saldoInicial=saldoInicial
        self.montoTotalDebitos=0
        self.montoTotalCreditos=0
        self.saldoActual=saldoInicial
        Cuenta.cantidadCuentas+=1
        self.cuenta=Cuenta.cantidadCuentas

    def depositar(self,monto):
        if(monto>0):
            self.montoTotalCreditos+=monto
            self.saldoActual+=monto
        else:
            return "Error: el monto debe ser mayor a cero colones"

    def retirar(self,monto):
        if(monto>0):
            if(self.saldoActual>monto):
                self.montoTotalDebitos+=monto
                self.saldoActual-=monto
            else:
                return f"Error: fondos insuficientes"
        else:
            return "Error: monto debe ser mayor a cero colones"

    def determinarEstadoCuenta(self):
        mensaje="Estado de cuenta \n"
        mensaje+="------------------------\n"
        mensaje+=f"Saldo Inicial: \t{self.saldoInicial}\n"
        mensaje+=f"Total debito:  \t{self.montoTotalDebitos}\n"
        mensaje+=f"Total credito: \t{self.montoTotalCreditos}\n"
        mensaje+=f"Saldo Actual:  \t{self.saldoActual}\n"

        print(mensaje)






class Veterinaria:
    totalPerros=0
    totalGatos=0
    totalAves=0
    
    def __init__(self):
        self.Tipo=""
        self.Peso=0.0

    def agregar(self,tipo,peso):
        if(isinstance(peso,float)and peso>0):
            if("perro"==tipo):
                Veterinaria.totalPerros+=1
                self.Tipo=tipo
                self.Peso=peso
            elif("gato"==tipo):
                Veterinaria.totalGatos+=1
               
                self.Tipo=tipo
                self.Peso=peso
            elif("ave"==tipo):
                
                Veterinaria.totalAves+=1
                self.Tipo=tipo
                self.Peso=peso
                
    def mostrarDatos(self):
        return f"Tipo: {self.Tipo} con un peso de: {self.Peso}"
    def VerTotalPerros(self):
        return f"Total de perros: {Veterinaria.totalPerros}"
    def VerTotalGatos(self):
        return f"Total de gatos: {Veterinaria.totalGatos}"
    def VerTotalAves(self):
        return f"Total de aves: {Veterinaria.totalAves}"

    


        
