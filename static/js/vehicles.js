document.addEventListener('DOMContentLoaded', function() {
    // Gestion de l'affichage grille/liste
    const viewButtons = document.querySelectorAll('.view-options button');
    const vehicleGrid = document.querySelector('.vehicle-grid');

    viewButtons.forEach(button => {
        button.addEventListener('click', () => {
            viewButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            if (button.dataset.view === 'list') {
                vehicleGrid.classList.add('list-view');
            } else {
                vehicleGrid.classList.remove('list-view');
            }
        });
    });

    // Gestion du slider de prix
    const priceRange = document.getElementById('priceRange');
    const minPrice = document.getElementById('minPrice');
    const maxPrice = document.getElementById('maxPrice');

    if (priceRange) {
        priceRange.addEventListener('input', (e) => {
            maxPrice.textContent = `${e.target.value}€`;
        });
    }
}); 