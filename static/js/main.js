const revealElements = document.querySelectorAll('.reveal-up');

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

revealElements.forEach((element) => revealObserver.observe(element));

const counters = document.querySelectorAll('.counter');

const animateCounter = (element) => {
  const target = Number(element.dataset.target || 0);
  const duration = 1200;
  const stepTime = 20;
  const increment = Math.max(1, Math.floor(target / (duration / stepTime)));

  let current = 0;
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = current.toLocaleString('zh-TW');
  }, stepTime);
};

const counterObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.4 }
);

counters.forEach((counter) => counterObserver.observe(counter));
