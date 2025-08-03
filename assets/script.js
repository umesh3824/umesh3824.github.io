let menu = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

menu.onclick = () => {
  menu.classList.toggle("bx-x");
  navbar.classList.toggle("active");
};

window.onscroll = () => {
  menu.classList.remove("bx-x");
  navbar.classList.remove("active");
};

// const sr = ScrollReveal({
//   distance: '60px',
//   duration: 2500,
//   reset: true,
// });

// sr.reveal('.home-text', { delay: 200, origin: 'top' });
// sr.reveal('.home-img', { delay: 400, origin: 'top' });
// sr.reveal('.about, .cta, .resume, .contact, .footer', { delay: 200, origin: 'top' });

// Intersection Observer for section animations
// This code should be in your script.js
document.addEventListener("DOMContentLoaded", function () {
  const animatedSections = document.querySelectorAll(".section-animate");
  const animationName = "sectionFadeInUp 1.2s cubic-bezier(0.23, 1, 0.32, 1) forwards";

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // Reset animation to allow replay
          entry.target.style.animation = "none";
          // Force reflow
          void entry.target.offsetWidth;
          entry.target.style.animation = animationName;
          entry.target.style.opacity = 1;
        } else {
          entry.target.style.opacity = 0;
          entry.target.style.animation = "none";
        }
      });
    },
    { threshold: 0.15 }
  );

  animatedSections.forEach((section) => {
    section.style.opacity = 0;
    section.style.animation = "none";
    observer.observe(section);
  });
});
