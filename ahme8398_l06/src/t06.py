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

lst = List()

lst_values = input("Enter a list of integers separated by spaces: ").split()

for value in lst_values:
    lst.append(int(value))

print("Original List:")
for i in lst:
    print(i)

# Test __getitem__ function
print(" ")
print("Test __getitem__")
index = int(input("Enter an index to get: "))
print("Value at index", index, ":", lst[index])

# Test __setitem__ function
print(" ")
print("Test __setitem__")
index = int(input("Enter an index to set: "))
value = int(input("Enter a value to set: "))
lst[index] = value
print("New List:")
for i in lst:
    print(i)

print(" ")

print("--TEST WITH MOVIE DATA--")
movie_list = List()

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

print("Original List:")
for i in movie_list:
    print(i)
    
print("")

print("Test __getitem__")
index = 5
print("Value at index", index, ":", movie_list[index])

print(" ")

print("Test __setitem__")
index = 5
value = 'Horror of Dracula|1958|Terence Fisher|7.4|8'

print("Set value at index", index, "to:", movie_list[index])

print("")

movie_list[index] = value
print("New List:")
for i in movie_list:
    print(i)