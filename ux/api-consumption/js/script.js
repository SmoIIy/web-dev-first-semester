import "./modules.js";
import { getMovieList, IMAGE_URL } from "./modules.js";

const template = document.querySelector("#movielist template");
const container = document.querySelector("#movielist");
const navButtons = document.querySelectorAll("nav button");

const renderMovieList = async (category) => {
    container.querySelectorAll(".list-item").forEach((el) => el.remove());
    document.querySelector(
        "title"
    ).textContent = `Movie Database | ${category}`;

    const movieListData = await getMovieList(category);

    movieListData.results.forEach((result) => {
        const clone = template.content.cloneNode(true);

        const title = result.title;
        const originalTitle = result.original_title;
        const overview = result.overview;
        const imagePath = result.poster_path;
        const release_date = result.release_date;

        clone.querySelector("h2").textContent = title;
        clone.querySelector(".description").textContent = overview;
        clone.querySelector(".original-title span").textContent = originalTitle;
        clone.querySelector(".release-date span").textContent = release_date;
        clone.querySelector(".list-item img").src = `${IMAGE_URL}${imagePath}`;
        container.appendChild(clone);
        console.log(result);
    });
};
navButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
        const category = btn.dataset.category;
        navButtons.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        renderMovieList(category);
    });
});

renderMovieList("now_playing");
