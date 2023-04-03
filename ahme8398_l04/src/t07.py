"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie_utilities import read_movies
from utilities import list_test
# Constants

fv = open("movies.txt", "r")

movies = read_movies(fv)

fv.close()

lst = List()

list_test(movies)
