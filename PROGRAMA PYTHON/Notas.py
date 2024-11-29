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
#Implementamos una funcion para verficar el nombre de los estudiantes
def VerificarNombre(nombre):
    while not nombre.isalpha():
        print("El nombre y/o apellido debe contener solo letras")
        nombre = input("Ingrese nuevamente el dato: ")
    return nombre

#Implementar un función que verique el dato ingresado
def VerificarNota(nota):
    while True:
        try:
            nota = float(nota)
            if nota < 1.0 or nota > 5.0:
                print("La nota debe estar entre 1.0 y 5.0.")
                nota = input("Ingrese nuevamente la nota: ")
            else:
                break
        except ValueError:
            print("La nota del estudiante debe ser un número.")
            nota = input("Ingrese nuevamente la nota: ")
    return nota
#Implemento error en el ingreso de los datos del estudiante
def VerificarError(error): 
    while error != "S" and error != "N": 
        print("La respuesta debe ser S o N.") 
        error = input("¿Desea repetir la digitación de este estudiante? (S/N): ") 
        error = error.upper() 
    return error

#Implementar un función que verique el numero de estudiantes
#Esto validando casos como cantidad mínima, que sea un numero y que sea un numero entero
def VerificarEstudiantes(cantidad):
    while True:
        if not cantidad.isnumeric():
            print("La cantidad de estudiantes debe ser un número entero.")
            cantidad = input("Ingrese nuevamente la cantidad de estudiantes: ")
        else:
            cantidad = int(cantidad)
            if cantidad < 1:
                print("La cantidad de estudiantes debe ser mayor a 0.")
                cantidad = input("Ingrese nuevamente la cantidad de estudiantes: ")
            else:
                break
    return cantidad

#Esta será la funcion que calcule los promedios
def Promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    return round(prom, 2) #redondeo el promedio en 2 digitos

#dejaré mos tanto las funciones como los objetos arriba.
class Estudiante:
    def __init__(self, id, nombre, apellido, nota1, nota2, nota3, promedio):	
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.promedio = promedio

#definimos el metodo str para imprimir los estudiantes en forma de tabla
    def __str__(self):
        return f"ID: {self.id}, {self.nombre}, {self.apellido}, N°1: {self.nota1}, N°2: {self.nota2}, N°3: {self.nota3}, Promedio: {self.promedio}"

#Con nuestro objeto Estudiante podemos empezar a ingresar los datos de los estudiantes a través de un bucle
#Para esto solicitaremos la cantidad de estudiantes en el curso

print("Bienvenidos al programa que calcula promedios de estudiantes")
print("------------------------------------------------------------")
#ingresa la variable que contará la cantidad de estudiantes
#ingresamos una lista vacia para la cantidad de alumnos
#establecemos un validador para que solo acepte valores numericos

cantidad = input("Ingrese la cantidad de estudiantes: ")
cantidad = VerificarEstudiantes(cantidad)
estudiantes = []

#cambiaremos el bucle for por un bucle while con el fin de poder corregir los datos de los estudiantes en caso de error
i = 1
while i <= cantidad:
    nombre= input(f"Ingrese el nombre del estudiante {i}: ")
    nombre = VerificarNombre(nombre)
    apellido= input(f"Ingrese el apellido del estudiante {i}: ")
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

    error = input("¿Desea repetir la digitación de este estudiante? (S/N): ")
    error = VerificarError(error)
    if error == "S":
        estudiantes.pop()
        continue
    else:
        i += 1


#lanzo en pantalla la lista de estudiantes ingresados
print("Tabla de estudiantes")
for estudiante in estudiantes:
    print(estudiante)

#Calculamos el promedio mas alto del curso
promedio_max = max(estudiante.promedio for estudiante in estudiantes)
print(f"El promedio mas alto del curso es: {promedio_max}")

#Calculamos el promedio mas bajo del curso
promedio_min = min(estudiante.promedio for estudiante in estudiantes)
print(f"El promedio mas bajo del curso es: {promedio_min}")

#Calculamos el promedio general del curso
promedio_general = sum(estudiante.promedio for estudiante in estudiantes) / len(estudiantes)
print(f"El promedio general del curso es: {promedio_general}")

