// Código 1 Actualizado: Manejo de menú con submenús al pasar el mouse
$(".menu > ul > li").mouseenter(function (e) {
  // Elimina la clase "active" de todos los elementos hermanos del <li> sobre el que se pasó el ratón.
  $(this).siblings().removeClass("active");

  // Agrega la clase "active" al elemento <li> sobre el que se pasó el ratón.
  $(this).addClass("active");

  // Muestra el submenú <ul> dentro del <li> con una animación deslizante.
  $(this).find("ul").stop(true, true).slideDown();

  // Oculta los submenús de los hermanos del <li> con una animación deslizante.
  $(this).siblings().find("ul").stop(true, true).slideUp();
});

// Evento para cerrar el submenú cuando el mouse se va del <li>
$(".menu > ul > li").mouseleave(function (e) {
  // Oculta el submenú <ul> dentro del <li> con una animación deslizante.
  $(this).find("ul").stop(true, true).slideUp();

  // Elimina la clase "active" del elemento <li> cuando el ratón se va.
  $(this).removeClass("active");
});

// Código 2: Funcionalidades adicionales (hover en navcontainer, dark mode, etc.)
const navcontainer = document.querySelector(".navcontainer");
const linkItems = document.querySelectorAll(".link-item");
const darkMode = document.querySelector(".dark-mode");
const logo = document.querySelector(".logo svg");

// navcontainer Hover
navcontainer.addEventListener("mouseenter", () => {
  navcontainer.classList.add("active");
});

// navcontainer Hover Leave
navcontainer.addEventListener("mouseleave", () => {
  navcontainer.classList.remove("active");
});

// Link-items Clicked (sin incluir dark-mode)
linkItems.forEach((linkItem) => {
  if (!linkItem.classList.contains("dark-mode")) {
    linkItem.addEventListener("click", () => {
      linkItems.forEach((item) => {
        item.classList.remove("active");
      });
      linkItem.classList.add("active");
    });
  }
});

// Dark Mode Functionality
darkMode.addEventListener("click", function () {
  if (document.body.classList.contains("dark-mode")) {
    darkMode.querySelector("span").textContent = "dark mode";
    darkMode.querySelector("ion-icon").setAttribute("name", "moon-outline");
    
  } else {
    darkMode.querySelector("span").textContent = "light mode";
    darkMode.querySelector("ion-icon").setAttribute("name", "sunny-outline");
    
  }
  document.body.classList.toggle("dark-mode");
});