//Como el anterior programa y el taller expuesto en el readme.md //
//Codificación en Javascript realizando únicamente el método para listar los datos de los estudiantes por medio de Node//

// NOTA... Durante el curso de Desarrollo Lógico para Programación e Inteligencia Artificial se realizaron todo los programas que se realizaron en JavaScript fueron ejecutados a través del explotador por ende solo se mostrarán la consola por HTML.

let estudiantes = {};

// Función para agregar estudiantes
function agregarEstudiante(id, nombre, apellido, nota1, nota2, nota3) {
    estudiantes[id] = {
        nombre: nombre,
        apellido: apellido,
        notas: [nota1, nota2, nota3]
    };
}

// Función para actualizar estudiantes
function actualizarEstudiante(id, nombre, apellido, nota1, nota2, nota3) {
    if (estudiantes[id]) {
        estudiantes[id] = {
            nombre: nombre,
            apellido: apellido,
            notas: [nota1, nota2, nota3]
        };
    } else {
        console.log("Estudiante no encontrado");
    }
}

// Función para borrar estudiantes
function borrarEstudiante(id) {
    if (estudiantes[id]) {
        delete estudiantes[id];
    } else {
        console.log("Estudiante no encontrado");
    }
}

// Función para listar estudiantes
function listarEstudiantes() {
    console.log(estudiantes);
}

