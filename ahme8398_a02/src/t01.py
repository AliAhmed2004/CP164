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
from Movie import Movie
from Movie_utilities import get_by_year
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

year = int(input("Enter the year: "))

year_movies = get_by_year(movies, year)

year_movies_titles = [movie.title for movie in year_movies]
print(year_movies_titles)
