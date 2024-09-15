
class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.__nacionalidad = "Peruano"

    def pedir_nombre_edad_saldo(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Saldo: {}".format(self.saldo))

    def cumpleanos(self):
        return self.edad + 1

    def aumetar_saldo(self):
        aumento = self.saldo * 0.3
        return self.saldo + aumento

    def prediccion(self):
        print("En el año 2025 tendra una {} años".format(self.cumpleanos()))

class Usuario(Persona):
    def transferencia(self,monto,destino):
        if self.saldo >= monto:
            self.saldo -= monto
            destino.saldo += monto
            print("Transferencia exitosa. Saldo actual de {}: {}".format(self.nombre,self.saldo))
            print("Saldo actual de {}: {}".format(destino.nombre,destino.saldo))
        else:
            print("Saldo insuficiente")

usuario1= Usuario("Luis",22,500)
usuario2= Usuario("Pepe", 21, 1000)

usuario1.pedir_nombre_edad_saldo()
usuario2.pedir_nombre_edad_saldo()

monto_transferido= 500
usuario1.transferencia(monto_transferido, usuario2)

usuario1.pedir_nombre_edad_saldo()
usuario2.pedir_nombre_edad_saldo()

monto_insuficiente = 2000
usuario1.transferencia(monto_insuficiente, usuario2)

