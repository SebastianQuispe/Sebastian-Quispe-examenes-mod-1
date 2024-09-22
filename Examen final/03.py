import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print("Tiempo de ejecución de '{}' es: {:.4f} segundos.".format(func.__name__, fin - inicio))
        return resultado
    return wrapper

@medir_tiempo
def mayor_de_numeros(*args):
    mayor = max(args)
    print("El mayor número es:", mayor)
    return mayor

@medir_tiempo
def sumar_numeros(**kwargs):
    suma = sum(kwargs.values())
    print("La suma de los números es:", suma)
    return suma

@medir_tiempo
def promedio_de_numeros(**kwargs):
    suma = sum(kwargs.values())
    cantidad = len(kwargs)
    promedio = suma / cantidad if cantidad > 0 else 0
    print("El promedio de los números es:", promedio)
    return promedio

print("Ejemplo 1:")
mayor_de_numeros(10, 20, 30, 5, 50, 25)

print("Ejemplo 2:")
sumar_numeros(a=10, b=20, c=30)

print("Ejemplo 3:")
promedio_de_numeros(x=5, y=10, z=15, w=20)