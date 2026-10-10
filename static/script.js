document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

    forms.forEach((form) => {
        form.addEventListener("submit", function () {
            const button = form.querySelector("button");
            button.textContent = "Processing...";
            button.disabled = true;
        });
    });
});
