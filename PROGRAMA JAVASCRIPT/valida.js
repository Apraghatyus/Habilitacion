function validarNombre(nombre) {
     return /^[a-zA-Z\s]+$/.test(nombre) && nombre.trim() !== "";
}

function validarNota(nota) { 
    return !isNaN(nota) && nota >= 1.0 && nota <= 5.0;
}