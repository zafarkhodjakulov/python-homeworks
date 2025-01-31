import requests
import random

def fetch_movies_by_genre(api_key, genre_name):
    genres_url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        "api_key": api_key,
        "language": "en-US"
    }

    response = requests.get(genres_url, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch genres: {response.status_code} - {response.reason}")
        return None

    genres = response.json().get("genres", [])
    genre = next((g for g in genres if g["name"].lower() == genre_name.lower()), None)

    if not genre:
        print(f"Genre '{genre_name}' not found.")
        return None

    discover_url = "https://api.themoviedb.org/3/discover/movie"

    params = {
        "api_key": api_key,
        "with_genres": genre["id"],
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": 1
    }
    response = requests.get(discover_url, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch movies: {response.status_code} - {response.reason}")
        return None

    movies = response.json().get("results", [])
    return movies

def recommend_movie(api_key, genre_name):
    movies = fetch_movies_by_genre(api_key, genre_name)
    if movies:
        movie = random.choice(movies)
        print(f"Recommended Movie in '{genre_name}' Genre:")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Rating: {movie['vote_average']}")

if __name__ == "__main__":
    genre_name = input("Enter a movie genre: ").strip()
    api_key = "must-put-api-key"

    recommend_movie(api_key, genre_name)