document.addEventListener('DOMContentLoaded', function () {
  const cards = document.querySelectorAll('.roadmap-card');
  const modal = document.getElementById('roadmap-modal');
  const modalTitle = document.getElementById('modal-title');
  const modalDescription = document.getElementById('modal-description');
  const modalTopics = document.getElementById('modal-topics');
  const modalClose = document.getElementById('roadmap-modal-close');
  const roadmapSteps = JSON.parse(document.getElementById('roadmapSteps').textContent);

  function openModal(step) {
    modalTitle.textContent = step.title;
    modalDescription.textContent = step.description;
    modalTopics.innerHTML = '';

    if (step.learn && step.learn.length) {
      step.learn.forEach(function (topic) {
        const li = document.createElement('li');
        li.textContent = topic;
        modalTopics.appendChild(li);
      });
    }

    const videoLink = document.getElementById('modal-video-link');
    if (step.video_link) {
      videoLink.href = step.video_link;
      document.getElementById('modal-video-container').style.display = 'block';
    } else {
      document.getElementById('modal-video-container').style.display = 'none';
    }

    modal.classList.add('open');
  }

  function closeModal() {
    modal.classList.remove('open');
  }

  cards.forEach(function (card) {
    card.addEventListener('click', function () {
      const stepIndex = parseInt(card.dataset.index, 10);
      const step = roadmapSteps[stepIndex];
      openModal(step);
    });
  });

  modalClose.addEventListener('click', closeModal);
  modal.addEventListener('click', function (event) {
    if (event.target === modal) {
      closeModal();
    }
  });
});