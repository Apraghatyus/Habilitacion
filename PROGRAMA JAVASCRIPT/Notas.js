//Como el anterior programa y el taller expuesto en el readme.md //
//Codificación en Javascript realizando únicamente el método para listar los datos de los estudiantes por medio de Node//

// NOTA... Durante el curso de Desarrollo Lógico para Programación e Inteligencia Artificial se realizaron todo los programas que se realizaron en JavaScript fueron ejecutados a través del explotador por ende solo se mostrarán la consola por HTML.

let Estudiantes = {};

// Función para agregar o actualizar estudiantes
function solicitar(idExistente = null) {
    let id = idExistente || prompt("Ingrese el ID del estudiante: ");
    while (!validarID(id)) {
        id = prompt("ID inválido. Ingrese nuevamente el ID del estudiante: ");
    }

    let nombre = prompt("Ingrese el nombre del estudiante: ");
    while (!validarNombre(nombre)) {
        nombre = prompt("Nombre inválido.\n  El nombre no puede contener números.\n Ingrese el nombre del estudiante: ");
    }
    let apellido = prompt("Ingrese el apellido del estudiante: ");
    while (!validarNombre(apellido)) {
        apellido = prompt("Apellido inválido.\n El apellido no puede contener números.\n Ingrese el apellido del estudiante: ");
    }

    let nota1 = parseFloat(prompt("Ingrese la nota 1 del estudiante: "));
    while (!validarNota(nota1)) {
        nota1 = parseFloat(prompt("Nota inválida. Ingrese la nota 1 del estudiante: "));
    }
    
    let nota2 = parseFloat(prompt("Ingrese la nota 2 del estudiante: "));
    while (!validarNota(nota2)) {
        nota2 = parseFloat(prompt("Nota inválida. Ingrese la nota 2 del estudiante: "));
    }
    
    let nota3 = parseFloat(prompt("Ingrese la nota 3 del estudiante: "));
    while (!validarNota(nota3)) {
        nota3 = parseFloat(prompt("Nota inválida. Ingrese la nota 3 del estudiante: "));
    }
    
    addstudent(id, nombre, apellido, nota1, nota2, nota3);
    console.log(idExistente ? "Estudiante actualizado correctamente" : "Estudiante agregado correctamente");
}


// Función para agregar estudiantes
function addstudent(id, nombre, apellido, nota1, nota2, nota3) {
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
    let id = prompt("Ingrese el ID del estudiante que desea actualizar: ");
    if (Estudiantes[id]) {
        solicitar(id);
    } else {
        console.log("Estudiante no encontrado");
    }
}

// Función para borrar estudiantes
function deletestudent() {
    let id = prompt("Ingrese el ID del estudiante que desea eliminar: ");
    if (Estudiantes[id]) {
        delete Estudiantes[id];
        console.log("Estudiante eliminado correctamente");
    } else {
        console.log("Estudiante no encontrado");
    }
}

// Función para listar estudiantes
function listar() {
    console.log("listado de estudiantes del curso");
    console.log("la cantidad de estudiantes es: " + Object.keys(Estudiantes).length);
    console.log(Estudiantes);
}

// Función del menú
function menu() {
    let opcion = prompt("Seleccione una opción:\n 1. Agregar Estudiante\n 2. Actualizar Estudiante\n 3. Eliminar Estudiante\n 4. Listar Estudiantes\n 5. Salir");
    switch (opcion) {
        case "1":
            solicitar();
            break;
        case "2":
            update();
            break;
        case "3":
            deletestudent();
            break;
        case "4":
            listar();
            break;
        case "5":
            console.log("Gracias por utilizar el programa");
            return;
        default:
            console.log("Opción incorrecta");
    }
    menu(); // Llamar nuevamente al menú para permitir más acciones
}

// Exportar las funciones y variables necesarias
window.Estudiantes = Estudiantes;
window.solicitar = solicitar;
window.addstudent = addstudent;
window.update = update;
window.deletestudent = deletestudent;
window.listar = listar;
window.menu = menu;