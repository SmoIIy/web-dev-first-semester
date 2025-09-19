document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const formDataObject = Object.fromEntries(formData);

    const list = document.querySelector("#cd-list");
    const article = document.createElement("article");
    article.innerHTML = `
        <p>${formDataObject.author}</p>
        <p>${formDataObject.title}</p>
        <p>${formDataObject.year}</p>
        <button class="delete-button"><!--
category: System
tags: [garbage, delete, remove, bin, ash-bin, uninstall, dustbin]
version: "1.0"
unicode: "eb41"
-->
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="20"
  height="20"
  viewBox="0 0 24 24"
  fill="none"
  stroke="#000000"
  stroke-width="1.25"
  stroke-linecap="round"
  stroke-linejoin="round"
>
  <path d="M4 7l16 0" />
  <path d="M10 11l0 6" />
  <path d="M14 11l0 6" />
  <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
  <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
</svg>

</button>
    `;
    article
        .querySelector(".delete-button")
        .addEventListener("click", function () {
            article.remove();
        });

    list.append(article);
    console.log(formDataObject);
});
