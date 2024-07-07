const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

navLinks.addEventListener("click", () => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-line");
});

const scrollRevealOption = {
  origin: "bottom",
  distance: "50px",
  duration: 1000,
};


ScrollReveal().reveal(".header__content p", {
  ...scrollRevealOption,
});

ScrollReveal().reveal(".header__content h1", {
  ...scrollRevealOption,
  delay: 500,
});

ScrollReveal().reveal(".header__content .header__btn", {
  ...scrollRevealOption,
  delay: 1000,
});

// about container
ScrollReveal().reveal(".about__container .section__header", {
  ...scrollRevealOption,
});

ScrollReveal().reveal(".about__container .section__description", {
  ...scrollRevealOption,
  delay: 500,
});


ScrollReveal().reveal(".blog__card", {
  ...scrollRevealOption,
  interval: 500,
});

const instagram = document.querySelector(".instagram__flex");

const instagramContent = Array.from(instagram.children);

instagramContent.forEach((item) => {
  const duplicateNode = item.cloneNode(true);
  duplicateNode.setAttribute("aria-hidder", true);
  instagram.appendChild(duplicateNode);
});


// about form

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
      const aceptarTerminos = document.getElementById("aceptar-terminos").checked;

      
      const errores = document.querySelectorAll(".error");// Limpiar errores anteriores
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
          formulario.style.display = 'none'; // Oculta el formulario
          successMessage.style.display = 'block'; // Muestra el mensaje de éxito

          setTimeout(() => {
            successMessage.style.display = 'none'; 
              formulario.style.display = 'block'; 
              formulario.reset(); 
          }, 3000);
      }
  }

  formulario.addEventListener("submit", validarFormulario)

});

