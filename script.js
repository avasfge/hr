// Плавный скролл
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: "smooth" });
  }
  
  // Анимация появления секций
  const sections = document.querySelectorAll('.section');
  
  function revealOnScroll() {
    sections.forEach((section) => {
      const rect = section.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.85) {
        section.style.opacity = "1";
        section.style.transform = "translateY(0)";
      }
    });
  }
  
  window.addEventListener("scroll", revealOnScroll);
  window.addEventListener("load", revealOnScroll);
  