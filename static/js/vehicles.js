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
    const maxPrice = document.getElementById('maxPrice');

    if (priceRange && maxPrice) {
        priceRange.addEventListener('input', function() {
            maxPrice.textContent = this.value + '€';
        });
    }
}); 