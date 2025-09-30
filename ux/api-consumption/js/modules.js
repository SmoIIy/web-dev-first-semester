export const API_KEY = "3cf3cc7f87563d892d2d81caa0ea5e2a";
export const BASE_URL = "https://api.themoviedb.org/3/movie/";
export const IMAGE_URL = "https://image.tmdb.org/t/p/w500/";

export const getMovieList = async (endpoint) => {
    const conn = await fetch(`${BASE_URL}${endpoint}?api_key=${API_KEY}`);
    const response = await conn.json();
    console.log(response);
};
