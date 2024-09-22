def conteo(func):
    def wrapper(*args, **kwargs):
        num_params = len(args) + len(kwargs)

        if num_params <= 1:
            print("Se requieren más de 1 parámetro para procesar la función.")
            return

        resultado = func(*args, **kwargs)

        print("La función '{}' fue ejecutada.".format(func.__name__))
        return resultado

    return wrapper


@conteo
def registrar_persona(edad, nombre, hora, minuto):
    print("Nombre: {}, Edad: {}, Registrado a las: {}:{}".format(nombre, edad, hora, minuto))


@conteo
def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("La media de las notas es: {:.2f}".format(media))
    return media


registrar_persona(21, "Sebas", 10, 30)
calcular_media(5, 7, 8, 6)
calcular_media(8)
