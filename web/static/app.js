const tweet = async () => {
    const conn = await fetch("/tweet");
    const response = await conn.text();
    document.querySelector("#message").innerHTML = response;
    console.log(response);
};

const save = async () => {
    console.log(event);
    console.log(event.target);
    console.log(event.target.form.user_name.value);
    const theForm = event.target.form;
    const conn = await fetch("/save", {
        method: "POST",
        body: new FormData(theForm),
    });
    const response = await conn.json();
    document.querySelector(
        "#message"
    ).innerHTML = `Hi ${response.user_name} ${response.last_name} `;
};

const likeTweet = async () => {
    const conn = await fetch("/api-like-tweet");
    const response = await conn.text();
};

// const burger = document.querySelector(".burger");
// const nav = document.querySelector("nav");

// burger.addEventListener("click", () => {
//   // toggle nav
//   nav.classList.toggle("active");

//   // toggle icon
//   burger.classList.toggle("open");
// });
