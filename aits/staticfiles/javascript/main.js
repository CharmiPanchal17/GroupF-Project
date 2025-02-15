document.addEventListener("DOMContentLoaded", function () {
    const registerButtons = document.querySelectorAll(".register-btn");
    const dropdowns = document.querySelectorAll(".dropdown-content");
    const dropdownOptions = document.querySelectorAll(".dropdown-option");

    // Toggle dropdown on clicking "Register" button
    registerButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            let dropdown = this.nextElementSibling;

            // Close all dropdowns first
            dropdowns.forEach(menu => {
                if (menu !== dropdown) menu.style.display = "none";
            });

            // Toggle the current one
            dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
        });
    });

    // Close dropdown when clicking outside
    window.addEventListener("click", function (event) {
        if (!event.target.matches(".register-btn")) {
            dropdowns.forEach(menu => menu.style.display = "none");
        }
    });

    // Close dropdown when clicking "As Student" or "As Lecturer"
    dropdownOptions.forEach(option => {
        option.addEventListener("click", function () {
            dropdowns.forEach(menu => menu.style.display = "none");
        });
    });
});