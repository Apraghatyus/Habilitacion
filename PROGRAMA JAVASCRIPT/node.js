//Este será el codigo para NODE.JS generado por IA solicitado en el taller.
//Se realizo ligado a html por la necesidad del desconocimiento de Node.js


const readline = require('readline');
const Estudiantes = {};

// Configurar readline para entrada de consola
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Funciones de validación
function validarNombre(nombre) {
    return /^[a-zA-Z\s]+$/.test(nombre) && nombre.trim() !== "";
}

function validarNota(nota) {
    return !isNaN(nota) && nota >= 1.0 && nota <= 5.0;
}

function validarID(id) {
    return /^[0-9]+$/.test(id) && id.trim() !== "";
}

// Función para solicitar datos del estudiante
function solicitar(idExistente = null) {
    return new Promise((resolve) => {
        const id = idExistente || prompt("Ingrese el ID del estudiante: ");
        if (!validarID(id)) {
            console.log("ID inválido. Ingrese nuevamente el ID del estudiante.");
            return resolve(solicitar(idExistente));
        }

        rl.question("Ingrese el nombre del estudiante: ", (nombre) => {
            if (!validarNombre(nombre)) {
                console.log("Nombre inválido. El nombre no puede contener números.");
                return resolve(solicitar(idExistente));
            }

            rl.question("Ingrese el apellido del estudiante: ", (apellido) => {
                if (!validarNombre(apellido)) {
                    console.log("Apellido inválido. El apellido no puede contener números.");
                    return resolve(solicitar(idExistente));
                }

                rl.question("Ingrese la nota 1 del estudiante: ", (nota1) => {
                    nota1 = parseFloat(nota1);
                    if (!validarNota(nota1)) {
                        console.log("Nota inválida. Ingrese nuevamente la nota 1 del estudiante.");
                        return resolve(solicitar(idExistente));
                    }

                    rl.question("Ingrese la nota 2 del estudiante: ", (nota2) => {
                        nota2 = parseFloat(nota2);
                        if (!validarNota(nota2)) {
                            console.log("Nota inválida. Ingrese nuevamente la nota 2 del estudiante.");
                            return resolve(solicitar(idExistente));
                        }

                        rl.question("Ingrese la nota 3 del estudiante: ", (nota3) => {
                            nota3 = parseFloat(nota3);
                            if (!validarNota(nota3)) {
                                console.log("Nota inválida. Ingrese nuevamente la nota 3 del estudiante.");
                                return resolve(solicitar(idExistente));
                            }

                            addStudent(id, nombre, apellido, nota1, nota2, nota3);
                            console.log(idExistente ? "Estudiante actualizado correctamente" : "Estudiante agregado correctamente");
                            resolve();
                        });
                    });
                });
            });
        });
    });
}

// Función para agregar estudiantes
function addStudent(id, nombre, apellido, nota1, nota2, nota3) {
    Estudiantes[id] = {
        nombre: nombre,
        apellido: apellido,
        notas1: nota1,
        nota2: nota2,
        nota3: nota3
    };
}

// Función para actualizar estudiantes
function update() {
    rl.question("Ingrese el ID del estudiante que desea actualizar: ", (id) => {
        if (Estudiantes[id]) {
            solicitar(id).then(() => menu());
        } else {
            console.log("Estudiante no encontrado");
            menu();
        }
    });
}

// Función para borrar estudiantes
function deleteStudent() {
    rl.question("Ingrese el ID del estudiante que desea eliminar: ", (id) => {
        if (Estudiantes[id]) {
            delete Estudiantes[id];
            console.log("Estudiante eliminado correctamente");
        } else {
            console.log("Estudiante no encontrado");
        }
        menu();
    });
}

// Función para listar estudiantes
function listar() {
    console.log("Listado de estudiantes del curso:");
    console.log("La cantidad de estudiantes es: " + Object.keys(Estudiantes).length);
    console.log(Estudiantes);
    menu();
}

// Función del menú
function menu() {
    rl.question("Seleccione una opción:\n 1. Agregar Estudiante\n 2. Actualizar Estudiante\n 3. Eliminar Estudiante\n 4. Listar Estudiantes\n 5. Salir\n", (opcion) => {
        switch (opcion) {
            case "1":
                solicitar().then(() => menu());
                break;
            case "2":
                update();
                break;
            case "3":
                deleteStudent();
                break;
            case "4":
                listar();
                break;
            case "5":
                console.log("Gracias por utilizar el programa");
                rl.close();
                break;
            default:
                console.log("Opción incorrecta");
                menu();
        }
    });
}

// Iniciar el menú
menu();
