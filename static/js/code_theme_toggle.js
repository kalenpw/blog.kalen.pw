function toggleCodeTheme() {
    const codeBlocks = document.querySelectorAll(".code-block");

    for (let i = 0; i < codeBlocks.length; i++) {
        codeBlocks[i].classList.toggle('light');
        codeBlocks[i].classList.toggle('dark');
        codeBlocks[i].querySelector('.toggle-icon').classList.toggle('fa-sun');
        codeBlocks[i].querySelector('.toggle-icon').classList.toggle('fa-moon');
    }
}