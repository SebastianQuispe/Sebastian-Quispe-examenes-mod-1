import random

def generar_numeros_aleatorios():
    numeros = [random.randint(1, 100) for _ in range(10)]
    print("Números aleatorios:", numeros)
    return numeros

def obtener_numeros_no_repetidos(numeros):
    numeros_unicos = list(set(numeros))
    print("Números no repetidos:", numeros_unicos)
    return numeros_unicos

def ordenar_numeros(numeros):
    numeros_mayor_a_menor = sorted(numeros, reverse=True)
    numeros_menor_a_mayor = sorted(numeros)
    print("Ordenados de mayor a menor:", numeros_mayor_a_menor)
    print("Ordenados de menor a mayor:", numeros_menor_a_mayor)
    return numeros_mayor_a_menor, numeros_menor_a_mayor

def mayor_par(numeros):
    numeros_pares = [num for num in numeros if num % 2 == 0]
    mayor_par = max(numeros_pares) if numeros_pares else None
    print("Mayor número par:", mayor_par)
    return mayor_par

lista_numeros = generar_numeros_aleatorios()
lista_unicos = obtener_numeros_no_repetidos(lista_numeros)
numeros_ordenados = ordenar_numeros(lista_unicos)
mayor_par(lista_unicos)
