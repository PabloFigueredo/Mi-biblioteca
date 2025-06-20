// Confirmación personalizada para eliminar un libro
document.addEventListener('DOMContentLoaded', function () {
    const deleteForms = document.querySelectorAll('form[action*="eliminar_libro"]');

    deleteForms.forEach(form => {
        form.addEventListener('submit', function (event) {
            const libroNombre = this.querySelector('button').getAttribute('data-libro-nombre');
            const confirmacion = confirm(`¿Estás seguro de que deseas eliminar el libro "${libroNombre}"?`);
            if (!confirmacion) {
                event.preventDefault();
            }
        });
    });
});