document.getElementById('btnTraerMensajes').addEventListener('click', () => {
    fetch('http://127.0.0.1:5000/mensajes')  // Por default, Method = 'GET' //
      .then(response => response.json())
      .then(datos => {
        console.log("datos", datos)
        const tablaBody = document.querySelector('#tablaMensajes tbody');  // Selecciono tbody de tablaMensajes y lo guardo
        tablaBody.innerHTML = ''; // Limpiar tabla antes de agregar nuevos datos (innerHTML = '' borra todo el contenido)

        // Busca entradas en la tabla "mensajes" de la BD y agrega filas a la tabla html con los campos deseados
        datos.forEach(dato => {
            excur = ""  
            if (dato.excursion=="1"){
                excur = "Circuito Diurno";
            }
            else {
                excur = "Circuito Nocturno";
            }
            const fila = document.createElement('tr');    // Crea una nueva fila (Table row) para cada entrada
            fila.innerHTML = `
                <td>${dato.id}</td>
                <td>${dato.nombre}</td>
                <td>${dato.email}</td>
                <td>${excur}</td>
                <td>${dato.fecha_envio}</td>
                <td>${dato.comentario_cliente}</td>
                <td>${dato.leido}</td>
            `;
          tablaBody.appendChild(fila);         // Agrega la nueva fila con los datos importados de la BD a la tabla html
        });
      })
      .catch(error => {
        console.error('Error al obtener los datos:', error);
    });
});

document.getElementById('formularioContacto').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario por defecto
    
    // Obtener los valores de los campos
    const id = document.getElementById('idInput').value;
    const gestion = document.getElementById('detalleInput').value;

    const dataFormulario = new FormData();
    dataFormulario.append('gestion', gestion); // Agrega como campo 'gestion' a dataFormulario, al contenido de gestion

    fetch(`http://127.0.0.1:5000/mensajes/${id}`, {         // Usa el ID ingresado por el usuario, para definir la ruta
      method: 'PUT',
      body: dataFormulario
    })
    .then(response => response.json())
    .then(data => {
      console.log('Respuesta del servidor: ', data);
      // Aquí podrías mostrar una confirmación al usuario o hacer algo con la respuesta del servidor
    })
    .catch(error => {
      console.error('Error al enviar los datos:', error);
    });
});