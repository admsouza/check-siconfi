document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.total-card');

    cards.forEach((card) => {
        const statusText = card.querySelector('p').textContent.trim();

        // Se o texto for "Dado Divergente", altera para laranja suave e transparente
        if (statusText === "Dado Divergente") {
            const cardBody = card.querySelector('.card-body');
            cardBody.classList.remove('bg-success', 'text-white');
            cardBody.classList.add('bg-soft-orange'); // Adiciona a nova classe CSS
        }
    });
});
