window.onload = () => {
    const searchText = document.getElementById("search-text");
    const searchButton = document.getElementById("search-button");

    searchText.addEventListener('input', (event) => {
        searchButton.href = "/search/?q=" + searchText.value;
    })

    searchText.addEventListener('keypress', (event) => {
        if (event.key == "Enter") {
            searchButton.click()
        }
    })
}