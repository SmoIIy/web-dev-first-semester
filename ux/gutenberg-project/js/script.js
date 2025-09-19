import { getBooks } from "./modules.js";

const list = document.querySelector("section");
const books = await getBooks();

const renderBookList = () => {
    const fragment = document.createDocumentFragment();

    books.forEach((book) => {
        const article = document.createElement("article");
        const title = document.createElement("h4");
        const image = document.createElement("img");
        const description = document.createElement("p");
        const link = document.createElement("a");
        book.summaries[0]
            ? (description.innerText = book.summaries[0])
            : (description.innerText = "No Description Provided");
        title.innerText = book.title;
        image.setAttribute("src", book.formats["image/jpeg"]);
        link.innerText = "Link";
        link.setAttribute("href", book.formats["text/plain; charset=us-ascii"]);

        article.append(title);
        article.append(image);
        article.append(description);
        article.append(link);
        fragment.append(article);
    });
    list.append(fragment);
};
renderBookList();
