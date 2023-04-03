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
from Movie import Movie
# Constants

movie = Movie('Dellamorte Dellamore', 1994,
              'Michele Soavi', 7.2, [3, 4, 5, 8])
print(movie.genres_list_string())
