import json
import media
import fresh_tomatoes

films = []

# Load JSON file of film data
with open('films.json') as films_json:
    # Parse films from JSON
    raw_films = json.load(films_json)

    # Loop over JSON, creating array of Movie instances
    for film in raw_films:
        movie = media.Movie(film['title'], film['storyline'],
                            film['poster_image_url'],
                            film['trailer_youtube_url'],
                            film['release_year'])
        films.append(movie)


# Create fresh_tomatoes.html in same directory
fresh_tomatoes.open_movies_page(films)
