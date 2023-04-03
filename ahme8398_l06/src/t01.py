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
# append
print("Test append")
lst = List()
while True:
    user_input = input("Enter a value to append (or 'x' to exit): ")
    if user_input == "x":
        break
    lst.append(user_input)
for i in lst:
    print(i)

print(" ")

# prepend
print("Test prepend")
lst = List()
while True:
    user_input = input("Enter a value to prepend (or 'x' to exit): ")
    if user_input == "x":
        break
    lst.prepend(user_input)
for i in lst:
    print(i)

print(" ")

# insert
print("Test insert")
lst = List()
while True:
    user_input = input(
        "Enter an index and a value to insert (or 'x' to exit): ")
    if user_input == "x":
        break
    if " " not in user_input:
        print("Invalid input. Please enter an index and a value separated by a space.")
        continue
    index, value = user_input.split()
    lst.insert(int(index), value)
for i in lst:
    print(i)

print(" ")
print("--TEST WITH MOVIE DATA--")
# append
print("Test append")
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
for i in movie_list:
    print(i)

print(" ")
# prepend
print("Test prepend")
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
movie_list.prepend(
    'Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6')
for i in movie_list:
    print(i)

print(" ")
# insert
print("Test insert")
movie_list = List()
movie_list.insert(8,'Zulu|2013|Jerome Salle|6.7|2')
movie_list.insert(0,'Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list.insert(1,'Z|1969|Costa-Gavras|8.2|2')
movie_list.insert(9,
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list.insert(2,'Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list.insert(3,'Finding Dory|2016|Andrew Stanton, Angus MacLane|7.5|4')
movie_list.insert(4,'Wrong Box, The|1966|Bryan Forbes|7.0|4')
movie_list.insert(5,'Jason and the Argonauts|1963|Don Chaffey|7.4|1,6')
movie_list.insert(6,'Horror of Dracula|1958|Terence Fisher|7.4|8')
movie_list.insert(7,
    'Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6')
for i in movie_list:
    print(i)