num1 = 42 # declaracion variable, numero
num2 = 2.3 # declaracion variable, float
boolean = True #booleano
string = 'Hello World' # declaracion variable, cadena
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #diccionario
fruit = ('blueberry', 'strawberry', 'banana') # Tupla
print(type(fruit)) # imprimir en consola, checkea que tipo es
print(pizza_toppings[1]) #imprime y elige el elemento 1 de la lista
pizza_toppings.append('Mushrooms') # imprime y agrega al final champiñones
print(person['name']) #accede al nombre
person['name'] = 'George' #cambia el valor de nombre
person['eye_color'] = 'blue' #cambia el valor del color de ojos
print(fruit[2]) #imprime y elije el elemento dos de la tupla

#condicional
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# loop que parte en 0 y para en el 5
for x in range(5):
    print(x)
    # loop que parte en el 2 y para en el 5
for x in range(2,5):
    print(x)
    #loop que parte en el dos, para en el 10 y va de 3 en 3
for x in range(2,10,3):
    print(x)
x = 0

while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #elimina el ultimo el elemento de la lista
pizza_toppings.pop(1) # elimina el valor del indice

print(person) #imprime
person.pop('eye_color') #elimina ese valor
print(person) # imprime

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

#funcion
def print_hello_ten_times():
    for num in range(10): #loop va del 0 al 10
        print('Hello') #imprime Hello

print_hello_ten_times() #llama a la funcion

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)