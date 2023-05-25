# Ejercicio 1: Actualizar valores
x = [ [5,2,3], [15,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Andrés', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

#Ejercicio 2: Iterar a traves de una lista de diccionarios
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
def iterateDictionary(some_list):
    for estudiante in some_list:
        for key, value in estudiante.items():
            print(f"{key} - {value}")
iterateDictionary(estudiantes)

#Ejercicio 3: obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
    for estudiante in some_list:
            print(estudiante[key_name])
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#Ejercicio 4: iterar a traves de un diccionario con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f'{len(some_dict[key])} {key.upper()}')  
        for value in some_dict[key]:
            print(value)

printInfo(dojo)