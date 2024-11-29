'''Sistema de notas en un instituto 
Este programa realiza el promedio de las notas de los alumnos de un instituto, que estudiante obtuvo el promedio más alto.
Se propone la construcion de un diccionario llamado estudiantes donde se almacene los datos que tendrán por llave el código del estudiante y una lista de sus atributos
    ID Estudiante
    Nombre
    Apellido
    Nota 1
    Nota 2
    Nota 3
Se solicita un CRUD que contenga las siguientes operaciones, Agregar, Actualizar, borrar y listar los estuadiates.
Para actualizar y borrar es necesario especificar todos los atributos del estudiante.

Adicionalmente, se está interasado en analizar los datos de los estudiantes junto con sus notar y conocer:
    Promedio para cada estudiante guardado en la base de datos.
    Nombre del estudiante con mayor promedio
    Nombre del estudiante con menor promedio
    Promedio general de todo el curso
 '''
#Se crea dos documentos más, los cuales tendrán las funciones y las validaciones de los datos ingresados
#serán importados en el programa principal

from classFun import Estudiante, Promedio
from valida import VerificarNombre, VerificarNota, Verificarsino, VerificarEstudiantes,  VerificarID

print("Bienvenidos al programa que calcula promedios de estudiantes")
print("------------------------------------------------------------")

# Ingresar la cantidad de estudiantes
cantidad = input("Ingrese la cantidad de estudiantes: ")
cantidad = VerificarEstudiantes(cantidad)
estudiantes = []

# Cambiar el bucle for por un bucle while con el fin de poder corregir los datos de los estudiantes en caso de error
i = 1
while i <= cantidad:
    nombre = input(f"Ingrese el nombre del estudiante {i}: ")
    nombre = VerificarNombre(nombre)
    apellido = input(f"Ingrese el apellido del estudiante {i}: ")
    apellido = VerificarNombre(apellido)
    notas = []
    
    for j in range(1, 4):
        nota = input(f"Ingrese la nota número {j} del estudiante {i}: ")
        nota = VerificarNota(nota)
        notas.append(nota)

    promedio = Promedio(notas[0], notas[1], notas[2])
    estudiante = Estudiante(i, nombre, apellido, notas[0], notas[1], notas[2], promedio)
    estudiantes.append(estudiante)

    print(f"Estudiante {i}: {estudiante.nombre}, {estudiante.apellido}, Promedio: {promedio}")

    sino = input("¿Desea repetir la digitación de este estudiante? (S/N): ").upper()
    sino = Verificarsino(sino)
    if sino == "S":
        estudiantes.pop()
        continue
    else:
        i += 1

# Lanzar en pantalla la lista de estudiantes ingresados
print("Tabla de estudiantes")
for estudiante in estudiantes:
    print(estudiante)

#Se implementa la un bucle para determinar si se desean eliminar estudiantes de la lista a través de su ID.
#Se presenta un error cuando eliminas toda la lista.
while True:
    sino = input("¿Desea eliminar un estudiante? (S/N): ").upper()
    sino = Verificarsino(sino)
    if sino == "S":
        id_deseado = input("Ingrese el ID del estudiante que desea eliminar: ")
        id_deseado = VerificarID(estudiantes, id_deseado)
        estudiante_delete = estudiantes.pop(id_deseado-1)
        print(f"Estudiante eliminado: {estudiante_delete}")
    else:
        break

# Lanzar la nueva tabla
print("Tabla de estudiantes")
for estudiante in estudiantes:
    print(estudiante)

# Calcular el promedio más alto del curso
promedio_max = max(estudiante.promedio for estudiante in estudiantes)
print(f"El promedio más alto del curso es: {promedio_max:.2f}")

# Calcular el promedio más bajo del curso
promedio_min = min(estudiante.promedio for estudiante in estudiantes)
print(f"El promedio más bajo del curso es: {promedio_min:.2f}")

# Calcular el promedio general del curso
promedio_general = sum(estudiante.promedio for estudiante in estudiantes) / len(estudiantes)
print(f"El promedio general del curso es: {promedio_general:.2f}")
