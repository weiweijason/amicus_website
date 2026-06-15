/* ── Scroll Reveal ── */
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
  { threshold: 0.15 }
);

revealElements.forEach((element) => revealObserver.observe(element));

/* ── Counter Animation ── */
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

/* ── Mobile Nav Auto-close ── */
const navCollapse = document.getElementById('mainNav');
if (navCollapse) {
  const bsCollapse = bootstrap.Collapse.getOrCreateInstance(navCollapse, { toggle: false });
  navCollapse.querySelectorAll('.nav-link').forEach((link) => {
    link.addEventListener('click', () => {
      if (window.innerWidth < 992) {
        bsCollapse.hide();
      }
    });
  });
}

/* ── Scroll Spy (active nav link) ── */
const spySections = document.querySelectorAll('main section[id]');
const spyLinks = document.querySelectorAll('.navbar-nav .nav-link[href^="#"]');

if (spySections.length && spyLinks.length) {
  const spyObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          spyLinks.forEach((link) => link.classList.remove('active'));
          const active = document.querySelector(
            `.navbar-nav .nav-link[href="#${entry.target.id}"]`
          );
          if (active) active.classList.add('active');
        }
      });
    },
    { threshold: 0.35, rootMargin: '-60px 0px -40% 0px' }
  );

  spySections.forEach((section) => spyObserver.observe(section));
}

/* ── Back to Top ── */
const backToTop = document.querySelector('.back-to-top');
if (backToTop) {
  window.addEventListener('scroll', () => {
    backToTop.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
