// Las validaciones fueron generadas a través de expresiones regulares con IA
function validarNombre(nombre) {
     return /^[a-zA-Z\s]+$/.test(nombre) && nombre.trim() !== "";
}

function validarNota(nota) { 
    return !isNaN(nota) && nota >= 1.0 && nota <= 5.0;
}

function validarID(id) {
    return /^[0-9]+$/.test(id) && id.trim() !== "";
}

// Asegúrate de que las funciones de validación también estén disponibles globalmente 
window.validarNombre = validarNombre; 
window.validarNota = validarNota; 
window.validarID = validarID;