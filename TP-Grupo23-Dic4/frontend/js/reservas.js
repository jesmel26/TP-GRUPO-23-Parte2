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

    if (nombre.value.trim() === "") {
        mostrarAlerta("Por favor, ingresa tu nombre.", nombre);
        return false;
    }

    var emailExpresion = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!email.value.match(emailExpresion)) {
        mostrarAlerta("Por favor, ingresa un correo electrónico válido.", email);
        return false;
    }

    if (telefono.value.trim() === "" || isNaN(telefono.value) || telefono.value.length<10){
        mostrarAlerta("Por favor, ingresa un número de teléfono válido y sin espacios.", telefono);
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

document.getElementById('formContacto').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir el envío por defecto del formulario
    
    // Obtener los datos del formulario en una variable de tipo FormData (JSON) (Guarda datos de formulario)
    const dataFormulario = new FormData(document.getElementById('formContacto'));

    // Realizar el envío de dataFormulario utilizando "fetch" con 'POST', a la ruta de la app de flask usada para enviar una nueva entrada en la tabla "mensajes" de la Base de Datos
    // fetch se queda esperando una respuesta (response)
    fetch('http://127.0.0.1:5000/mensajes', {
    method: 'POST',
    body: dataFormulario                              // Aclaro que envío en el body a la variable dataFormulario
    })
    .then(response => {
    if (response.ok) {
        // Ocultar formulario
        document.getElementById('formContacto').style.display = 'none'; 
        // Mostrar el mensaje de "Datos enviados"
        document.getElementById('mensajeEnviado').style.display = 'block';
        
        // Reiniciar el formulario después de 2 segundos (puedes ajustar el tiempo)
        setTimeout(function() {
        // Ocultar formulario
        document.getElementById('formContacto').reset();
        document.getElementById('formContacto').style.display = 'block'; 
        document.getElementById('mensajeEnviado').style.display = 'none';
        }, 5000);
    } else {
        throw new Error('Error al enviar los datos');
    }
    })
    .catch(error => {
    console.error('Error: ', error);
    });
});