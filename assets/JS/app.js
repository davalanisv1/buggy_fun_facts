const statusMessage = document.querySelector('#status');
const image = document.querySelector('#insect-image');
const details = document.querySelector('.insect-details');

async function loadInsect() {
  try {
    const response = await fetch('/api/insect');
    const insect = await response.json();

    if (!response.ok) {
      throw new Error(insect.error || 'The insect could not be loaded.');
    }

    document.querySelector('#insect-name').textContent = insect.name;
    document.querySelector('#scientific-name').textContent = insect.scientific_name;
    document.querySelector('#fun-fact').textContent = insect.fun_fact;
    details.hidden = false;

    if (insect.image_url) {
      image.src = insect.image_url;
      image.alt = `A picture of ${insect.name}`;
      image.hidden = false;
    }

    statusMessage.hidden = true;
  } catch (error) {
    statusMessage.textContent = error.message;
    statusMessage.classList.add('error');
  }
}

loadInsect();