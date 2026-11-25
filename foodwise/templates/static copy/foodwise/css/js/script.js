
function searchFood() {
    const searchInput = document.getElementById("foodSearch");
    const searchValue = searchInput.value.trim();

    if (searchValue === "") {
        alert("Please enter a food or restaurant name!");
        return;
    }

    alert("Searching for: " + searchValue);
}
