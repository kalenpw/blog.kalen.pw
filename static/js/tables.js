window.addEventListener('load', () => {
    document.querySelectorAll('.card-text table').forEach((element) => {
        element.classList.add('table', 'table-responsive-lg');
    });
});