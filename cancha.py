class AdCanchas:
    numeroReserva=0
    def __init__(self,nombreEst,telefono,direccion,correo):
        self.NombreEst=nombreEst
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.cliente=[]
        self.cancha=[]
        self.factura=[]
        self.reservacio=[]

    def mostrar_info(self):
        return f"{self.telefono} {self.direccion} {self.correo}"

    def crear_cliente(self,cedula,nombre,telefono,correo):
        for dato in self.cliente:
            if(dato.Cedula==cedula):
                return "Error"
            else:
                continue
        

        c1=Clientes(cedula,nombre,telefono,correo)
        self.cliente+=[c1]
        print(c1.Cedula)
        
    def Crear_Cancha(self,identificador,Precio):
        if(isinstance(identificador,int)):
            for dato in self.cancha:
                if(dato.Identificador==identificador):
                    return "Error"
                else:
                    continue
                
            CN1=Canchas(identificador,Precio)
            self.cancha+=[CN1]
            print(CN1.Identificador)
        else:
            return "Error; no es entero"    

    def modificar_cliente(self,cedula):
        cont=0
        for dato in self.cliente:
            if(dato.Cedula==cedula):
                modificar=input("Ingrese el nuevo telefono: ")
                dato.Telefono=modificar
                self.cliente[cont]=dato
                return    
            else:
                cont+=1
        return "Error"
        
    def mostrar_cliente(self):
        for objecto in self.cliente:
            objecto.MOstrar()
            
    def reservar_cancha(self,cliente,cancha,fecha,hora_ini,hora_fin):
        AdCanchas.numeroReserva+=1
        for dato in self.cliente:
            if(dato.Cedula==cliente):
                R1=Reservaciones(cliente,cancha,fecha,hora_ini,hora_fin,AdCanchas.numeroReserva)
                self.reservacio+=[R1]
                return f"{AdCanchas.numeroReserva}"
            else:
                continue
        return "Error"
        
    def modificar_reserva(self,identificador):
        cont=0
        for dato in self.reservacio:
            if(dato.Identificador==identificador):
                fecha=input("Ingrese la fecha: ")
                hora_i=input("Ingrese la hora de inicio: ")
                hora_F=input("Ingrese la hora de fin:")
                
                dato.Fecha=fecha
                dato.Hora_ini=int(hora_i)
                dato.Hora_fin=int(hora_F)
                self.reservacio[cont]=dato
                return "$"
            else:
                cont+=1
    
    def quitar_reserva(self,numero):
        nuevo=[]
        for dato in self.reservacio:
            if(dato.Identificador):
                continue
            else:
                nuevo+=[dato]
        self.reservacio=nuevo
                 
    def mostrar_info_reserva(self,identificador):
        for dato in self.reservacio:
            if(dato.Identificador==identificador):
                dato.mostrar()
                return
            else:
                continue
        return "No existe"
                
        
    def ver_reservas(self,fecha):
        for dato in self.reservacio:
            if(dato.Fecha==fecha):
                dato.mostrar()
            else:
                continue
                
    """
    def facturar(self,reserva):

    def mostrar_factura(self,fecha):
    """
        

class Clientes:
    def __init__(self,cedula,nombre,telefono,correo):
        self.Cedula=cedula
        self.Nombre=nombre
        self.Telefono=telefono
        self.Correo=correo
    def MOstrar(self):
        print(f"Cedula: {self.Cedula}\n Nombre: {self.Nombre} \n Telefono: {self.Telefono}\n Email: {self.Correo}")
        
        
class Reservaciones:
    
    
    def __init__(self,cliente,cancha,fecha,hora_ini,hora_fin,identificador):
        self.Cliente=cliente
        self.Fecha=fecha
        self.Hora_ini=hora_ini
        self.Hora_fin=hora_fin
        self.Identificador=identificador
        self.Cancha=cancha
    def mostrar(self):
        info=f"Reserva{self.Identificador}\n"
        info+=f"{self.Fecha}\n"
        info+=f"{self.Hora_ini}\n"
        info+=f"{self.Hora_fin}\n"
        print(info)
        

class Canchas:
    def __init__(self,identificador,precio):
        self.Identificador=identificador
        self.Precio=precio
    """
    def Crear_Cancha_1(self):
        for datos in self.Identificador:
            if(datos==identificador):
                return "Error"
            else:
                continue
        self.Identificador+=[identificador]
        self.Precio+=[precio]
     """          

class Facturas:
    Factura=0
    def __init__(self):
        Facturas.Factura+=1
        



