#Este documento valida los datos ingresados por el usuario.
#Revisa que solo contenga letras el nombre.
def VerificarNombre(nombre):
    while not nombre.isalpha():
        print("El nombre y/o apellido debe contener solo letras.")
        nombre = input("Ingrese nuevamente el dato: ")
    return nombre

#Revisa que la nota este entre 1.0 y 5.0, además de que sea un número.
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

#Digita el valor si el usuario desea corregir el dato.
def Verificarsino(sino):
    while sino != "S" and sino != "N":
        print("La respuesta debe ser S o N.")
        sino = input("¿Desea repetir la digitación de este estudiante? (S/N): ")
        sino = sino.upper()
    return sino

#Verifica el número inicial de estudiantes.
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

#Verifica que el ID sea un número entero.
# Verifica que el ID sea un número entero y esté dentro del rango válido de estudiantes
def VerificarID(estudiantes, id):
    while True:
        if not id.isnumeric():
            print("El ID del estudiante debe ser un número entero.")
            id = input("Ingrese nuevamente el ID del estudiante: ")
        else:
            id = int(id)
            if id < 1 or id > len(estudiantes):
                print(f"El ID debe estar dentro del rango de 1 a {len(estudiantes)}.")
                id = input("Ingrese nuevamente el ID del estudiante: ")
            else:
                break
    return id
