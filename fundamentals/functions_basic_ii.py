# Ejercicio 1: cuenta regresiva
def countdown(numero):
    lista = []
    for i in range(numero, -1, -1):
        lista.append(i)
    return lista
print(countdown(5))

# Ejercicio 2: imprimir y devolver
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]
print(imprimir_y_devolver([1,2]))

# Ejercicio 3: primero mas longitud
def primero_mas_longitud(lista):
    return lista [0] + len(lista)
print(primero_mas_longitud([1,2,3,4,5]))

# Ejercicio 4: Valores mayores que el segundo
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False
    nuevaLista = []
    for i in range(0,len(lista)):
        if lista[i] > lista[1]:
            nuevaLista.append(lista[i])

    print(len(nuevaLista))
    return nuevaLista

print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

# Ejercicio 5: esta longitud, ese valor
def length_and_value(tamaño,valor):
    lista = []
    for i in range(0, tamaño):
        lista.append(valor)
    return lista
print(length_and_value(4,7))
print(length_and_value(6,2))