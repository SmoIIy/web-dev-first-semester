document.querySelector(".temp-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const initialValueOutput = document.querySelector("#initial-value");
    const convertedValueOutput = document.querySelector("#converted-value");
    const from = document.querySelector("#from").value;
    const to = document.querySelector("#to").value;
    const input = parseFloat(document.querySelector("#convert-input").value);
    let output;
    let initialLetter;
    let convertedLetter;
    if (from === "celcius") {
        initialLetter = "C";
        if (to === "celcius") {
            convertedLetter = "C";
            output = input;
        } else if (to === "fahrenheit") {
            convertedLetter = "F";
            output = input * (9 / 5) + 32;
        } else if (to === "kelvin") {
            convertedLetter = "K";
            output = input + 273.15;
        }
    }
    if (from === "fahrenheit") {
        initialLetter = "F";
        if (to === "fahrenheit") {
            convertedLetter = "F";
            output = input;
        } else if (to === "celcius") {
            convertedLetter = "C";
            output = ((input - 32) * 5) / 9;
        } else if (to === "kelvin") {
            convertedLetter = "K";
            output = ((input - 32) * 5) / 9 + 273.15;
        }
    }
    if (from === "kelvin") {
        initialLetter = "K";
        if (to === "kelvin") {
            convertedLetter = "K";
            output = input;
        } else if (to === "fahrenheit") {
            convertedLetter = "F";
            output = ((input - 273.15) * 9) / 5 + 32;
        } else if (to === "celcius") {
            convertedLetter = "C";
            output = input - 273.15;
        }
    }
    initialValueOutput.innerText = input.toFixed(2) + initialLetter;
    convertedValueOutput.innerText = output.toFixed(2) + convertedLetter;
});
