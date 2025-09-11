import { URL } from "./info.js";

fetch(`${URL}/random.php`)
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        data = data.meals[0];

        const article = document.createElement("article");
        const header = document.createElement("header");
        const h3 = document.createElement("h3");
        header.append(h3);
        article.append(header);

        const img = document.createElement("img");
        img.setAttribute("src", data.strMealThumb);

        const areaPill = document.createElement("p");
        areaPill.innerText = data.strArea;
        areaPill.classList.add("recipe-attribute", "recipe-area");
        article.append(areaPill);

        const categoryPill = document.createElement("p");
        categoryPill.innerText = data.strCategory;
        categoryPill.classList.add("recipe-attribute", "recipe-category");
        article.append(categoryPill);

        // article.innerHTML = `
        //     <header>
        //         <h3>${data.strMeal}</h3>
        //     </header>
        //     <img src="${data.strMealThumb}"/>
        //     <p class="recipe-attribute recipe-area">${data.strCategory}</p>
        //     <p class="recipe-attribute recipe-category">${data.strArea}</p>
        // `;

        document.querySelector("#recipelist").append(article);
    })
    .catch((error) => console.log(error));
