"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""

# Imports
from Movie_utilities import get_by_genres
from Movie import Movie
# Constants

movies = []
with open("movies.txt", "r") as file:
    for line in file:
        movie_data = line.strip().split("|")
        title = movie_data[0]
        year = int(movie_data[1])
        director = movie_data[2]
        rating = float(movie_data[3])
        genres = [int(x) for x in movie_data[4].split(",")]
        movie = Movie(title, year, director, rating, genres)
        movies.append(movie)

genre_codes = [int(x) for x in input(
    "Enter the genre code numbers (1 to 9) separated by commas: ").split(",")]

movie_codes = get_by_genres(movies, genre_codes)

print([movie.title for movie in movie_codes])
