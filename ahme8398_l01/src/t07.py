"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-01-14"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
# Constants

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close()
