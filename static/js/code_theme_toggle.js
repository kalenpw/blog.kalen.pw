function toggleCodeTheme() {
    const codeBlocks = document.querySelectorAll(".code-block");

    for (let i = 0; i < codeBlocks.length; i++) {
        codeBlocks[i].classList.toggle('light');
        codeBlocks[i].classList.toggle('dark');

        if (codeBlocks[i].classList.contains('light')) {
            codeBlocks[i].querySelector('.toggle-icon').classList.remove('fa-sun');
            codeBlocks[i].querySelector('.toggle-icon').classList.add('fa-moon');
        } else {
            codeBlocks[i].querySelector('.toggle-icon').classList.remove('fa-moon');
            codeBlocks[i].querySelector('.toggle-icon').classList.add('fa-sun');
        }
    }
}