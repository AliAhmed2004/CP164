"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Movie_utilities import read_movies

# Constants

fv = open("movies.txt", "r")

movies = read_movies(fv)

stack_test(movies)

fv.close()
