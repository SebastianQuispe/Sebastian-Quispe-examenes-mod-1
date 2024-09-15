class Persona:
        def __init__(self, nombre, edad, saldo):
            self.nombre = nombre
            self.edad = edad
            self.saldo = saldo
            self.nacionalidad = "Peruano"
        def pedir_nombre_edad(self):
            print("Nombre: {}".format(self.nombre))
            print("Edad: {}".format(self.edad))
        def cumpleanos(self):
            return self.edad + 1
        def aumetar_saldo(self):
            aumento= self.saldo * 0.3
            return self.saldo + aumento
        def prediccion(self):
            print("En el año 2025 tendra una {} años".format(self.cumpleanos()))

persona_1= Persona("Luis",22,500)
persona_2= Persona("Pepe", 21, 1000)

persona_1.pedir_nombre_edad()
print("Incremento de sueldo es: {}".format(persona_1.aumetar_saldo()))
persona_1.prediccion()

persona_2.pedir_nombre_edad()
print("Incremento de sueldo es: {}".format(persona_2.aumetar_saldo()))
persona_2.prediccion()

