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
def VerificarError(error):
    while error != "S" and error != "N":
        print("La respuesta debe ser S o N.")
        error = input("¿Desea repetir la digitación de este estudiante? (S/N): ")
        error = error.upper()
    return error

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
