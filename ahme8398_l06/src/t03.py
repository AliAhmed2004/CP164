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

input_list = input("Enter a list of integers separated by spaces: ").split()
for value in input_list:
    lst.append((value))

# max
print(" ")
print("Test max and min")
max_value = lst.max()
print("Maximum value in the list = ", max_value)

min_value = lst.min()
print("Minimum value in the list = ", min_value)

# count
print(" ")
print("Test count")
key = int(input("Enter a value to count in the list: "))
count = lst.count(key)
print(f"Number of times {key} is in the list:", count)


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
movie_list.append('Wrong Box, The|1966|Bryan Forbes|7.0|4')
movie_list.append('Jason and the Argonauts|1963|Don Chaffey|7.4|1,6')
movie_list.append('Horror of Dracula|1958|Terence Fisher|7.4|8')
movie_list.append(
    'Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6')

print("Movie list:")
for i in movie_list:
    print(i)
    
# max
print(" ")
print("Test max and min")
max_value = movie_list.max()
print("Maximum value in the list = ", max_value)

min_value = movie_list.min()
print("Minimum value in the list = ", min_value)

# count
print(" ")
print("Test count")
key = 'Wrong Box, The|1966|Bryan Forbes|7.0|4'
count = movie_list.count(key)
print(f"Key = {key}")
print(f"Number of times key is in the list:", count)