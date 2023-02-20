alumnos = {}
cantidad = int(input("Cuantos alumnos hay:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("El alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame la nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame la nota del alumno (negativo para terminar):"))
        alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))