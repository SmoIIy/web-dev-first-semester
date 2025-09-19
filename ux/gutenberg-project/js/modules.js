const URL_ENDPOINT = "https://gutendex.com/books/";

export const getBooks = async () => {
    try {
        const response = await fetch(URL_ENDPOINT);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const responseJson = await response.json();

        console.log(responseJson.results);
        return responseJson.results;
    } catch (error) {
        alert(error);
    }
};
