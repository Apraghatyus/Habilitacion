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
#NUEVA VERSION: se establece una primera funcion para sintetizar
#Esta será la funcion que calcule los promedios
def Promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

#Le daremos un poco de presentación y por ahora solo lo trabajaremos con un solo estudiante para el buen uso de la función
#También le añadiremos el ingreso de datos a traves de la consola
print("Bienvenidos al programa que calcula promedios de estudiantes")


nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
nota1 = int(input("Ingrese la primera nota del estudiante: "))
nota2 = int(input("Ingrese la segunda nota del estudiante: "))
nota3 = int(input("Ingrese la tercera nota del estudiante: "))

promedio = Promedio(nota1, nota2, nota3)

print(f"El promedio del estudiante {nombre} {apellido} es: {promedio}")

#Esto facilita el ingreso de datos pero solo nos deja guardar un solo estudiante.
#para ello lo que se implementará como objetivo es un bucle el cual permita almacenar más estudiantes.
#para esto estableceremos Estudiantes como un objeto la cual almacenará la información