const elementsToReveal = document.querySelectorAll('.profile, .intro-text, h1, .description, .image-overlay');

// Add intersection observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.5,
});

// Observe each element
elementsToReveal.forEach((element) => {
  observer.observe(element);
});
