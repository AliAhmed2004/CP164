"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq
from utilities import pq_to_array
from utilities import priority_queue_test
from Movie_utilities import read_movies

# opening movies text file for reading
fv = open("movies.txt", "r")

# putting it into function read_movies from lab 1
movies = read_movies(fv)

# closing the text file
fv.close()

pq = Priority_Queue()

priority_queue_test(movies)

print()

array_to_pq(pq, movies)

for i in pq:
    print(i)

target = []

pq_to_array(pq, target)

for values in target:
    print(values)
