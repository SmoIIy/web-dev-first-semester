document.querySelector(".email-form").addEventListener("submit", (e) => {
    e.preventDefault();

    const email = document.getElementById("mail").value.trim();
    const error = document.getElementById("error");
    const emailregex = "/^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/";

    if (!email.match(emailregex)) {
        error.innerText = "The email-adress is not valid";
    } else if (email.length < 10) {
        error.innerText =
            "The email address must be at least 10 characters long";
    } else {
        error.innerText = "";
    }
});
