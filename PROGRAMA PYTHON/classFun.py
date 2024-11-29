import csv
import os

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

# Implementamos la función que calcula el promedio
def Promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    return round(prom, 2)

# Función para leer un archivo CSV
def leer_csv(nombre_archivo, estudiantes):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id = int(row['ID'])
                nombre = row['Nombre']
                apellido = row['Apellido']
                nota1 = float(row['Nota 1'])
                nota2 = float(row['Nota 2'])
                nota3 = float(row['Nota 3'])
                promedio = Promedio(nota1, nota2, nota3)
                estudiante = Estudiante(id, nombre, apellido, nota1, nota2, nota3, promedio)
                estudiantes.append(estudiante)
        print(f"Archivo CSV '{nombre_archivo}' leído correctamente.")
    else:
        print(f"Archivo '{nombre_archivo}' no encontrado.")
    return estudiantes

# Función para exportar a un archivo CSV
def exportar_csv(nombre_archivo, estudiantes):
    with open(nombre_archivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Nombre', 'Apellido', 'Nota 1', 'Nota 2', 'Nota 3', 'Promedio'])
        for estudiante in estudiantes:
            writer.writerow([estudiante.id, estudiante.nombre, estudiante.apellido, estudiante.nota1, estudiante.nota2, estudiante.nota3, estudiante.promedio])
    print(f"Archivo CSV '{nombre_archivo}' exportado correctamente.")
