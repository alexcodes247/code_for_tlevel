
const form = document.getElementById("form");
const emailInput = document.getElementById("email");
const nameInput = document.getElementById("name");
const positionInput = document.getElementById("position");
const quantityInput = document.getElementById("quantity");

let perticket;

form.addEventListener("submit", function (e) {
    let isValid = validateForm();
    if (!isValid) {
        e.preventDefault();
    } else {
        if (positionInput.value === "Standing") {
            perticket = 30;
        } else if (positionInput.value === "Sitting") {
            perticket = 60;
        } else {
            perticket = 120;
        }

        

        let price = perticket * quantityInput.value;
        alert("Form successfully sent!");


        window.location.href = `payment.html?total=${encodeURIComponent(price)}`;

        alert("You have been charged" + price);
    }
});

function validateForm() {
    let errors = [];

    validateEmail(emailInput.value, errors);
    validateName(nameInput.value, errors);
    validatePosition(positionInput.value, errors);
    validateQuantity(quantityInput.value, errors);

    if (errors.length > 0) {
        alert(errors.join("\n"));
        return false;
    }
    return true;
}

function validateEmail(value, errors) {
    if (isEmpty(value)) {
        errors.push("Email is required.");
    } else if (!matchesEmailFormat(value)) {
        errors.push("Please enter a valid email address.");
    }
}

function validateName(value, errors) {
    if (isEmpty(value)) {
        errors.push("Name is required.");
    } else if (!hasMinimumLength(value, 3)) {
        errors.push("Name must be at least 3 characters long.");
    }
}

function validatePosition(value, errors) {
    if (isEmpty(value)) {
        errors.push("Position is required.");
    } else if (!hasMinimumLength(value, 2)) {
        errors.push("Position must be at least 2 characters long.");
    }
}

function validateQuantity(value, errors) {
    if (isEmpty(value)) {
        errors.push("Quantity is required.");
    } else if (!isPositiveInteger(value)) {
        errors.push("Quantity must be a positive integer.");
    }
}

function isEmpty(value) {
    return value.trim() === "";
}

function hasMinimumLength(value, minLen) {
    return value.trim().length >= minLen;
}

function matchesEmailFormat(input) {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(input);
}

function isPositiveInteger(value) {
    return Number.isInteger(Number(value)) && Number(value) > 0;
}
