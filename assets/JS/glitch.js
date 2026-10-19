const glitchPanels = document.querySelectorAll('.insect-card, .intro-panel');
const glitchEffects = ['is-chromatic', 'is-jittering', 'is-flickering', 'is-scanning'];
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

function glitchAtRandom() {
  if (reducedMotion.matches || glitchPanels.length === 0) return;

  const panel = glitchPanels[Math.floor(Math.random() * glitchPanels.length)];
  const effect = glitchEffects[Math.floor(Math.random() * glitchEffects.length)];
  panel.classList.add('is-glitching', effect);

  window.setTimeout(() => {
    panel.classList.remove('is-glitching', effect);
    window.setTimeout(glitchAtRandom, 600 + Math.random() * 800);
  }, 520);
}

if (!reducedMotion.matches) {
  window.setTimeout(glitchAtRandom, 800);
}
a
reducedMotion.addEventListener('change', (event) => {
  if (event.matches) {
    glitchPanels.forEach((panel) => {
      panel.classList.remove('is-glitching', ...glitchEffects);
    });
  } else {
    window.setTimeout(glitchAtRandom, 500);
  }
});
