# import
import imdb

# Search IMDb using movie name
def find_movie(movie_name):
    # Setup IMDb access object
    ia = imdb.IMDb()

    # Get list of potential movies
    movie_list = ia.search_movie(movie_name, results = 10)
    # Pick top choice
    movie = ia.get_movie(movie_list[0].movieID)
    return movie

# Search IMDb using person's name
def find_person(person_name, results):
    # Setup IMDb access object
    ia = imdb.IMDb()

    # Get list of movies this person is in
    movie_list = ia.search_person(person_name, results = results)
    
