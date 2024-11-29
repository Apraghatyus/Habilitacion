#En esta parte implementaremos la clase Estudiante
class Estudiante:
    def __init__(self, id, nombre, apellido, nota1, nota2, nota3, promedio):    
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.promedio = promedio

    def __str__(self):
        return f"ID: {self.id}, {self.nombre}, {self.apellido}, N°1: {self.nota1}, N°2: {self.nota2}, N°3: {self.nota3}, Promedio: {self.promedio:.2f}"

#implementamos la funcion que calcula el promedio
def Promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    return round(prom, 2)
