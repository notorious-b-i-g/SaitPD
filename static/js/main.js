// Простейший пример: плавный скролл к началу страницы по клику на логотип
document.addEventListener('DOMContentLoaded', () => {
  const logo = document.querySelector('header nav a');
  if (logo) {
    logo.addEventListener('click', (e) => {
      if (location.pathname === '/') {
        e.preventDefault();
        window.scrollTo({top: 0, behavior: 'smooth'});
      }
    });
  }
});
