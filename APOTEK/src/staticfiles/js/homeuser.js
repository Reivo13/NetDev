function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('hide');
}

let promoIndex = 0;
const promoSlides = document.querySelector('.promo-slides');
const totalPromo = document.querySelectorAll('.promo-slide').length;

setInterval(() => {
  promoIndex = (promoIndex + 1) % totalPromo;
  promoSlides.style.transform = `translateX(-${promoIndex * 100}%)`;
}, 4000);
  
