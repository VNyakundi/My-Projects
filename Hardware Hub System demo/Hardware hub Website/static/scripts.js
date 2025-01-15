// Handle form submission with client-side validation
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", event => {
            const inputs = form.querySelectorAll("input");
            let isValid = true;

            inputs.forEach(input => {
                if (input.value.trim() === "") {
                    input.style.borderColor = "red";
                    isValid = false;
                } else {
                    input.style.borderColor = "#c70000";
                }
            });

            if (!isValid) {
                event.preventDefault();
                alert("Please fill out all fields.");
            }
        });
    });
});
