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
#Implementar un función que verique el dato ingresado
def VerificarNota(nota):
    while nota < 1.0 or nota > 5.0:
        print("La nota debe estar entre 1.0 y 5.0")
        nota = float(input("Ingrese nuevamente la nota: "))
    return nota


#Esta será la funcion que calcule los promedios
def Promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    return prom

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
        return f" {self.id}, {self.nombre}, {self.apellido}, {self.nota1}, {self.nota2}, {self.nota3},  {self.promedio}"

#Con nuestro objeto Estudiante podemos empezar a ingresar los datos de los estudiantes a través de un bucle
#Para esto solicitaremos la cantidad de estudiantes en el curso

print("Bienvenidos al programa que calcula promedios de estudiantes")
print("------------------------------------------------------------")
#ingresa la variable que contará la cantidad de estudiantes
#ingresamos una lista vacia para la cantidad de alumnos

cantidad = int(input("Ingrese la cantidad de estudiantes: "))
estudiantes = []

#con el bucle for, ingresaremos los datos de los estudiantes numerandolos 1 a 1 y añadiendolos a la lista
#para hacer bien el programa, podremos una lista para almacenar las notas de cada estudiante
#Es necesario que notas se defina en el inicio del primer ciclo para cuando almacene los datos no se acumulen los datos
for i in range(1, cantidad+1):
    nombre= input(f"Ingrese el nombre del estudiante {i}: ")
    apellido= input(f"Ingrese el apellido del estudiante {i}: ")
    notas = []
    
    for j in range(1, 4):
        nota = float(input(f"Ingrese la nota número {j} del estudiante {i}: "))
        nota = VerificarNota(nota)
        notas.append(nota)

    promedio = Promedio(notas[0], notas[1], notas[2])
    estudiante = Estudiante(i, nombre, apellido, notas[0], notas[1], notas[2], promedio)
    estudiantes.append(estudiante)

    print(f"Estudiante {i}: {estudiante.nombre}, {estudiante.apellido}, Promedio: {promedio}")

#lanzo en pantalla la lista de estudiantes ingresados
print("Tabla de estudiantes")
print("ID\tNombre\tApellido\tNota 1\tNota 2\tNota 3\tPromedio")
for estudiante in estudiantes:
    print(estudiante)

#Con este tabla se podrá ver el promedio de cada estudiante y el promedio general de todos

