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

#Para iniciar este problema se hará como primer esquema una solucion con 3 estudiantes definidos a través de variables.#
nombre1 = "Estudiante 1"
apellido1 = "Apellido 1"
nota1 = 10
nota2 = 9   
nota3 = 8

nombre2 = "Estudiante 2"
apellido2 = "Apellido 2"
nota4 = 10
nota5 = 9
nota6 = 7

nombre3 = "Estudiante 3"
apellido3 = "Apellido 3"
nota7 = 10  
nota8 = 9
nota9 = 8

#Para calcular este problema emplearemos la operación de sumar cada nota de los estudiantes y dividirlo por 3.#
promedio1 = (nota1 + nota2 + nota3) / 3
promedio2 = (nota4 + nota5 + nota6) / 3
promedio3 = (nota7 + nota8 + nota9) / 3

#para calcular el promedio de mayor y menor del curso aplicamos las operaciones basicas a través de funciones definidas por Python.#

promedio_mayor = max(promedio1, promedio2, promedio3)
promedio_menor = min(promedio1, promedio2, promedio3)

print("El promedio mayor es:", promedio_mayor)
print("El promedio menor es:", promedio_menor)

#por ahora no vinculamos a los estudiantes con su promedio#
#Y por ultimo calculamos el promedio total del curso#

promedio_total = (promedio1 + promedio2 + promedio3) / 3
print("El promedio total es:", promedio_total)

#Con este primer planteamiento podemos determinar promedio de mayor y menor del curso y promedio total del curso.#
#El problema actual que presenta este esquema es vincular los promedios de los estudiantes con sus respectivos nombres.#