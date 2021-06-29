
class Cliente:
    def __init__(self,ced,nomb,gen):
        self.cedula = ced
        self.nombre = nomb
        self.genero = gen
    def ver(self):
        info = "Cedula: "+str(self.cedula)
        info += "\nNombre: "+str(self.nombre)
        info += "\nGenero: "+str(self.genero)
        print(info)
class Cola:
    def __init__(self):
        self.cola = []
        self.atendidos = 0
        self.tipo = "Cola de Clientes"
    def tipo(self):
        print(self.tipo)
    def vacio_p(self):
        return self.cola == []
    def mostrar(self):
        cont = 0
        for cliente in self.cola:
            cont += 1
        return cont
    def agregar(self,ced,nomb,gen):
        if (gen == "M" or gen == "F") and nomb != "":
            c1 = Cliente(ced,nomb,gen)
            self.cola += [c1]
        else:
            print("El genero debe ser F o M")
    def sacar(self):
        primero = self.cola[0]
        print("Atendiendo a",str(primero.nombre))
        self.atendidos += 1
        self.cola = self.cola[1:] #El primero de la fila o cola
    def ver(self):
        if self.cola != []:
            cl1 = self.cola[0] #El primer elemento del arreglo
            cl1.ver() #El primero de la fila o cola
    def ultimo(self):
        if self.cola != []:
            cl1 = self.cola[-1] #El último elemento del arreglo
            cl1.ver()
    def reset(self):
        self.cola = []
        self.atendidos = 0
    def imprimirCola(self):
        if self.cola!=[]:
            for indice in self.cola:
                clientes.ver()
                print("---------------")
            
        else:
            return "No hay clientes por atender"
    def cantidadGenero(self):
        if(self.cola!=[]):
            F=0
            M=0
            for linea in self.cola:
                print()
                if("M" == linea.genero):
                    M+=1
                else:
                    F+=1
            print(f"Cantidad de Mujeres en la cola: {F}")
            print(f"Cantidad de Hombres en la cola: {M}")
        else:
            return
                    

