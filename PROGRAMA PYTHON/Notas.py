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
#Esta será la funcion que calcule los promedios
def Promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    return prom

#dejaré mos tanto las funciones como los objetos arriba.
class Estudiante:
    def __init__(self, id, nombre, apellido, nota1, nota2, nota3, promedio):	
        
        self.nombre = nombre
        self.apellido = apellido
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.promedio = promedio


#Con nuestro objeto Estudiante podemos empezar a ingresar los datos de los estudiantes a través de un bucle
#Para esto solicitaremos la cantidad de estudiantes en el curso

print("Bienvenidos al programa que calcula promedios de estudiantes")

#ingresa la variable que contará la cantidad de estudiantes
#ingresamos una lista vacia para la cantidad de alumnos
cantidad = int(input("Ingrese la cantidad de estudiantes: "))
estudiantes = []

#con el bucle for, ingresaremos los datos de los estudiantes numerandolos 1 a 1 y añadiendolos a la lista
for i in range(1, cantidad+1):
    nombre= input(f"Ingrese el nombre del estudiante {i}: ")
    apellido= input(f"Ingrese el apellido del estudiante {i}: ")
    nota1= float(input(f"Ingrese la primera nota del estudiante {i}: "))
    nota2= float(input(f"Ingrese la segunda nota del estudiante {i}: "))
    nota3= float(input(f"Ingrese la tercer nota del estudiante {i}: "))
    promedio = Promedio(nota1, nota2, nota3)
    estudiante = Estudiante(i, nombre, apellido, nota1, nota2, nota3, promedio)
    estudiantes.append(estudiante)


print(f"El promedio del ultimo estudiante ingresado es {estudiante.nombre} {estudiante.apellido} es: {estudiante.promedio}")

#Para imprimir los datos de los estudiantes es necesesario implementar otro bucle for
#También pondrémos funciones validadores y para acortar el codigo usaremos otro bucle dentro del bucle for el cual se encarge de validar los datos de los estudiantes