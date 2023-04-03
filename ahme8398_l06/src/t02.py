"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-20"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

print("--TEST WITH INTEGERS--")
lst = List()

while True:
    value = input("Enter a value (or 'x' to exit): ")
    if value == 'x':
        break
    lst.append(value)

key = input("Enter a key to search for: ")

previous, current, index = lst._linear_search(key)

if index == -1:
    print("Key not found in the list.")
else:
    if current is not None:
        print(f"Key found at index [{index}] = {current._value}")
    else:
        print("Current is None.")

print(" ")
print("--TEST WITH MOVIE DATA--")
movie_list = List()

movie_list.append('Zulu|2013|Jerome Salle|6.7|2')
movie_list.append('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list.append('Z|1969|Costa-Gavras|8.2|2')
movie_list.append(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list.append('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list.append('Finding Dory|2016|Andrew Stanton, Angus MacLane|7.5|4')
movie_list.append('Wrong Box, The|1966|Bryan Forbes|7.0|4')
movie_list.append('Jason and the Argonauts|1963|Don Chaffey|7.4|1,6')
movie_list.append('Horror of Dracula|1958|Terence Fisher|7.4|8')
movie_list.append(
    'Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6')

key = 'Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8'

previous, current, index = movie_list._linear_search(key)

print("Original list:")
for i in movie_list:
    print(i)
    
print("")

if index == -1:
    print("Key not found in the list.")
else:
    if current is not None:
        print(f"Key found at index [{index}] = {current._value}")
    else:
        print("Current is None.")