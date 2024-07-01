document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.getElementById("formulario");
  const successMessage = document.getElementById("mensaje-enviado");

  successMessage.style.display = 'none';

  function validarFormulario(event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const apellido = document.getElementById("apellido").value;
    const sexo = document.getElementById("sexo").value;
    const correo = document.getElementById("correo").value;
    const mensaje = document.getElementById("mensaje").value;
    const aceptarTerminos = document.getElementById("aceptar-terminos").checked;

    const errores = document.querySelectorAll(".error");
    errores.forEach(error => error.innerHTML = "");

    let formValid = true;

    if (nombre.trim().length < 3) {
      document.getElementById("error-nombre").innerHTML = "El nombre debe tener al menos 3 caracteres";
      formValid = false;
    }

    if (apellido.trim().length < 3) {
      document.getElementById("error-apellido").innerHTML = "El apellido debe tener al menos 3 caracteres";
      formValid = false;
    }

    if (!sexo) {
      document.getElementById("error-sexo").innerHTML = "Seleccione una opción de sexo";
      formValid = false;
    }

    const correoRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!correoRegExp.test(correo)) {
      document.getElementById("error-correo").innerHTML = "Ingrese un correo electrónico válido";
      formValid = false;
    }

    if (!aceptarTerminos) {
      document.getElementById("error-terminos").innerHTML = "Debe aceptar los términos y condiciones";
      formValid = false;
    }

    if (formValid) {
      const formData = new FormData();
      formData.append("nombre", nombre);
      formData.append("apellido", apellido);
      formData.append("sexo", sexo);
      formData.append("correo", correo);
      formData.append("mensaje", mensaje);

      fetch("/submit", {
        method: "POST",
        body: formData
      })
      .then(response => {
        if (response.ok) {
          formulario.style.display = 'none'; // Oculta el formulario
          successMessage.style.display = 'block'; // Muestra el mensaje de éxito

          setTimeout(() => {
            successMessage.style.display = 'none';
            formulario.style.display = 'block';
            formulario.reset();
          }, 3000);
        } else {
          throw new Error('Error al enviar el formulario');
        }
      })
      .catch(error => {
        console.error('Error en la solicitud fetch:', error);
      });
    }
  }

  formulario.addEventListener("submit", validarFormulario);
});
