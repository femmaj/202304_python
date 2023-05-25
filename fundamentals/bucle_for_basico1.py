# ejercicio 1: imprimir numeros enteros del 0 al 150
for i in range(151):
    print(i)

# ejercicio 2: imprimir multiplos de 5 entre 5 y 1000
for i in range(5,1005):
    if i % 5 == 0:
        print(i)

# ejercicio 3: imprimir numeros del 1 al 100. 5 coding 10 coding dojo
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# ejercicio 4: impares del 0 al 500000 e imprimir suma final

suma_final = 0
for i in range(1,500000,2):
    suma_final = suma_final + i
print(suma_final)

# ejercicio 5: cuenta regresiva desde 2018 de 4 en 4
for num in range(2018,0,-4):
    print(num)

# ejercicio 6: contador flexible

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
