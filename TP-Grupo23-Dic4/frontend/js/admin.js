document.getElementById('btnTraerMensajes').addEventListener('click', () => {
    fetch('https://subtrooper14.pythonanywhere.com/mensajes')  // Por default, Method = 'GET' //
      .then(response => response.json())
      .then(datos => {
        console.log("datos", datos)
        const tablaBody = document.querySelector('#tablaMensajes tbody');
        tablaBody.innerHTML = '';

        datos.forEach(dato => {
            excur = ""  
            if (dato.excursion=="1"){
                excur = "Circuito Diurno";
            }
            else {
                excur = "Circuito Nocturno";
            }

            msj_leido = 0
                        if (dato.leido=="0"){
                msj_leido = "No";
            }
            else {
                msj_leido = "Si";
            }

            const fila = document.createElement('tr');
            fila.innerHTML = `
                <td>${dato.id}</td>
                <td>${dato.nombre}</td>
                <td>${dato.email}</td>
                <td>${excur}</td>
                <td>${dato.fecha_envio}</td>
                <td>${dato.comentario_cliente}</td>
                <td>${msj_leido}</td>
            `;
          tablaBody.appendChild(fila);
        });
      })
      .catch(error => {
        console.error('Error al obtener los datos:', error);
    });
});

document.getElementById('formularioContacto').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const id = document.getElementById('idInput').value;
    const gestion = document.getElementById('detalleInput').value;

    const dataFormulario = new FormData();
    dataFormulario.append('gestion', gestion);

    fetch(`https://subtrooper14.pythonanywhere.com/mensajes/${id}`, {
      method: 'PUT',
      body: dataFormulario
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('formularioContacto').style.display = 'none'; 
            document.getElementById('respuestaEnviada').style.display = 'block';
            document.getElementById('respuestaEnviada').style.marginBottom = '15%';
            setTimeout(function() {
            // Ocultar formulario
            document.getElementById('formularioContacto').reset();
            document.getElementById('formularioContacto').style.display = 'block'; 
            document.getElementById('respuestaEnviada').style.display = 'none';
            }, 5000);
      } else {
            throw new Error('No se puedo enviar la respuesta');
      }
      })
    .then(response => response.json())
    .then(data => {
      console.log('Respuesta del servidor: ', data);
    })
    .catch(error => {
      console.error('Error al enviar los datos:', error);
    });
});
