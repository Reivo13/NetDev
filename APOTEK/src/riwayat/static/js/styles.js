let lastScrollTop = 0;
  const navbar = document.getElementById("navbar");

  window.addEventListener("scroll", function () {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
      // Scroll down → hide navbar
      navbar.style.top = "-100px";
    } else {
      // Scroll up → show navbar
      navbar.style.top = "0";
    }

    lastScrollTop = scrollTop;
  });
  