var menuToggle = document.getElementById("mobile");
var mobileMenu = document.getElementById("mobile-menu");

document.addEventListener("DOMContentLoaded", function () {
  menuToggle.addEventListener("click", function () {
    mobileMenu.classList.toggle("hide-mobile-menu");
  });
});

document.addEventListener("scroll", function () {
  mobileMenu.classList.add("hide-mobile-menu");
});
