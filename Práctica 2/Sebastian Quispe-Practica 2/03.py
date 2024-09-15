class BilleteraElectronica:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.__saldo_soles = saldo_soles
        self.__saldo_dolares = saldo_dolares
        self.__tasa_cambio = 3.5

    def __str__(self):
        return ("Titular: {} {}".format(self.nombre, self.apellido),
                "Saldo en Soles: {}".format(self.__saldo_soles),
                "Saldo en Dólares: {}".format(self.__saldo_dolares))

    def transferir(self, monto, desde, hacia):
        if desde == "soles" and self.__saldo_soles >= monto:
            if hacia == "dolares":
                self.__saldo_soles -= monto
                self.__saldo_dolares += monto / self.__tasa_cambio
            elif hacia == "soles":
                self.__saldo_soles -= monto
        elif desde == "dolares" and self.__saldo_dolares >= monto:
            if hacia == "soles":
                self.__saldo_dolares -= monto
                self.__saldo_soles += monto * self.__tasa_cambio
            elif hacia == "dolares":
                self.__saldo_dolares -= monto
        else:
            print("Fondos insuficientes o moneda de destino inválida")
            return
        print("Transferencia realizada.")
        print(self)

    def retirar(self, monto, moneda):
        if moneda == "soles" and self.__saldo_soles >= monto:
            self.__saldo_soles -= monto
        elif moneda == "dolares" and self.__saldo_dolares >= monto:
            self.__saldo_dolares -= monto
        else:
            print("Saldo insuficiente en {}".format(moneda))
            return
        print("Retiro realizado.")
        print(self)

billetera1 = BilleteraElectronica("Sebastian", "Quispe", 1000, 500)
billetera2 = BilleteraElectronica("Zebas", "Twitter", 1500, 200)
billetera3 = BilleteraElectronica("Xebas", "Twister", 2000, 1000)

billetera1.transferir(500, "soles", "dolares")
billetera2.transferir(50, "dolares", "soles")
billetera3.transferir(100, "dolares", "dolares")

billetera1.retirar(200, "soles")
billetera2.retirar(30, "dolares")
billetera3.retirar(1500, "soles")
