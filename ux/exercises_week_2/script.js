document.querySelector(".tax-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const inputAmount = document.querySelector("#amount");
    const inputPercentage = document.querySelector("#percentage");

    const taxAmountOutput = document.querySelector("#tax-amount");
    const finalAmountOuput = document.querySelector("#final-amount");

    const calculateTaxPercentage = 100 - parseFloat(inputPercentage.value);
    //mængden betalt i tax
    const taxAmountValue =
        (parseFloat(inputAmount.value) * parseFloat(inputPercentage.value)) /
        100;
    //Mængden der er tilbage efter tax
    const finalAmountValue =
        parseFloat(inputAmount.value) * (calculateTaxPercentage / 100);

    taxAmountOutput.innerText = taxAmountValue.toFixed(2);
    finalAmountOuput.innerText = finalAmountValue.toFixed(2);
});
