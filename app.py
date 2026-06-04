class Credito:
    def __init__(self, monto, tasa):
        self.monto = monto
        self.tasa = tasa
    def __str__(self): 
        #__str__ construye a un string que al llamar la instancia aparece esto
        return f"Credito(monto): ${self.monto}, tasa: {self.tasa*100}%"
        

class CreditoSinComision(Credito):
    pass


#capito 9, 8 crash code
#cap 1, 2 clean code
#cap 1, 2 achitecture patterns 
#los cuatro pilares fundamentales
#herencia | encapuslado | abstraccion | polimorfismo

#encapsulamiento

class Cliente:
    def __init__(self, nombre, ingresos):
        self.nombre = nombre
        self.__ingresos = ingresos # el __ es para hacerlo privado el atributo
        #privado es para que no se pueda editar el atributo fuera de la clase que lo creó
        #en cambio protegido puede ser editado por la clase y sus hijos
        self.creditos = []
    def asignar_credito(self, credito):
        self.creditos.append(credito)
    
CL01 = Cliente("Ana Lopez", 2000)
CR01 = Credito(1000,0.10)
CL01.asignar_credito(CR01)
print(CL01.creditos[0])