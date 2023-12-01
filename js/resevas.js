function validarFormulario() {
    var nombre = document.getElementById("nombre");
    var email = document.getElementById("email");
    var telefono = document.getElementById("telefono");
    var excursion = document.getElementById("excursion");
    var fecha = document.getElementById("fecha");
    var personas = document.getElementById("personas");

    function mostrarAlerta(mensaje, elemento) {
        alert(mensaje);
        elemento.focus();
    }

    if (nombre.value.trim() === "" || nombre.value.length <3  || !isNaN(nombre.value))  {
        mostrarAlerta("Por favor, ingresa un nombre válido.", nombre);
        return false;
    }

    var emailExpresion = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!email.value.match(emailExpresion)) {
        mostrarAlerta("Por favor, ingresa un correo electrónico válido.", email);
        return false;
    }

    if (telefono.value.trim() === "" || isNaN(telefono.value)) {
        mostrarAlerta("Por favor, ingresa un número de teléfono válido.", telefono);
        return false;
    }

    if (excursion.value === "") {
        mostrarAlerta("Por favor, selecciona una excursión.", excursion);
        return false;
    }

    var today = new Date();
    if (new Date(fecha.value) <= today || fecha.value === "") {
        mostrarAlerta("Por favor, selecciona una fecha futura.", fecha);
        return false;
    }

    if (personas.value <= 0) {
        mostrarAlerta("Por favor, ingresa un número válido de personas.", personas);
        return false;
    }

    alert("¡Tu reserva ha sido exitosa! Gracias por elegirnos para tu próxima experiencia.");
    return true;
}

