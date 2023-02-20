numero = int(input("Introduce el número de elementos a añadir al diccionario: "))
diccionario = {}

for i in range(numero):
    nombre = input("Introduce el nombre: ") 
    anio = int(input("Introduce el año de nacimiento: "))
    
    while anio < 1900:
        print("El año no puede ser menor a 1900")
        anio = int(input("Introduce el año de nacimiento: "))
    diccionario[nombre] = anio

print("Datos del diccionario:", diccionario)