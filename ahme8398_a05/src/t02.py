"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-19"
-------------------------------------------------------
"""
# Imports
# Imports
from Sorted_List_array import Sorted_List
from Movie_utilities import read_movies

movie_list = Sorted_List()

with open('movies.txt', 'r') as fv:
    movie_list = read_movies(fv)

# __eq__
print("--__eq__--")
movie1 = movie_list[0]
movie2 = movie_list[1]

equal = movie_list[0] == movie_list[1]
print(equal)

print(" ")

# getitem
print("--getitem--")
print(movie_list[3])

print(" ")

# clean
print("--clean--")
movie_list = Sorted_List()
movie_list.insert("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
movie_list.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list.insert("Zulu|1964|Cy Endfield|7.8|9")
movie_list.insert("I Am Legend|2007|Francis Lawrence|7.1|0,6")
movie_list.insert("I Am Legend|2007|Francis Lawrence|7.1|0,6")
movie_list.insert("I Am Legend|2007|Francis Lawrence|7.1|0,6")

movie_list.clean()
for i in movie_list:
    print(i)

print(" ")

# intersection
print("--intersection--")
movie_list1 = Sorted_List()
movie_list2 = Sorted_List()
target = Sorted_List()
movie_list1.insert("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
movie_list1.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list1.insert("Zulu|1964|Cy Endfield|7.8|9")

movie_list2.insert("Darjeeling Limited, The|2007|Wes Anderson|7.1|4")
movie_list2.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list2.insert(
    "Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6")

target.intersection(movie_list1, movie_list2)

for i in target:
    print(i)

print(" ")

# split
print("--split--")
movie_list = Sorted_List()
target1 = Sorted_List()
target2 = Sorted_List()
movie_list.insert("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
movie_list.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list.insert("Zulu|1964|Cy Endfield|7.8|9")
movie_list.insert("I Am Legend|2007|Francis Lawrence|7.1|0,6")
target1, target2 = movie_list.split()

print("Target1: ")
for i in target1:
    print(i)

print(" ")

print("Target2: ")
for i in target2:
    print(i)

print(" ")

# union
print("--union--")
movie_list1 = Sorted_List()
movie_list2 = Sorted_List()
target = Sorted_List()
movie_list1.insert("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
movie_list1.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list1.insert("Zulu|1964|Cy Endfield|7.8|9")

movie_list2.insert("Darjeeling Limited, The|2007|Wes Anderson|7.1|4")
movie_list2.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list2.insert(
    "Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6")
target.union(movie_list1, movie_list2)

for i in target:
    print(i)

print(" ")

# __contains__
print("--__contains__--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list1.insert('Zulu|1964|Cy Endfield|7.8|9')
movie_list1.insert('Dark City|1998|Alex Proyas|7.8|0')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

key = 'Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8'

print(key in movie_list1)

print(" ")

# remove_front
print("--remove_front--")
movie_list = Sorted_List()
movie_list.insert("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
movie_list.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list.insert("Zulu|1964|Cy Endfield|7.8|9")
movie_list.insert("I Am Legend|2007|Francis Lawrence|7.1|0,6")
movie_list.remove_front()
for i in movie_list:
    print(i)

print(" ")

# remove_many
print("--remove_many--")
movie_list = Sorted_List()
movie_list.insert("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
movie_list.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list.insert("Zulu|1964|Cy Endfield|7.8|9")
movie_list.insert("I Am Legend|2007|Francis Lawrence|7.1|0,6")
key = "I Am Legend|2007|Francis Lawrence|7.1|0,6"
movie_list.remove_many(key)
for i in movie_list:
    print(i)

print(" ")

# split_alt
print("--split_alt--")
movie_list = Sorted_List()
target1 = Sorted_List()
target2 = Sorted_List()
movie_list.insert("Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8")
movie_list.insert("Dark City|1998|Alex Proyas|7.8|0")
movie_list.insert("Zulu|1964|Cy Endfield|7.8|9")
movie_list.insert("I Am Legend|2007|Francis Lawrence|7.1|0,6")
target1, target2 = movie_list.split_alt()

print("Target1: ")
for i in target1:
    print(i)

print(" ")

print("Target2: ")
for i in target2:
    print(i)

print(" ")

# count
print("--count--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list1.insert('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list1.insert('Zulu|1964|Cy Endfield|7.8|9')
movie_list1.insert('Dark City|1998|Alex Proyas|7.8|0')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

key = 'Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8'

print(movie_list1.count(key))

print(" ")

# find
print("--find--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list1.insert('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list1.insert('Zulu|1964|Cy Endfield|7.8|9')
movie_list1.insert('Dark City|1998|Alex Proyas|7.8|0')

key = '|8.2|2'

value = movie_list1.find(key)

print(value)

print(" ")

# index
print("--index--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list1.insert('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list1.insert('Zulu|1964|Cy Endfield|7.8|9')
movie_list1.insert('Dark City|1998|Alex Proyas|7.8|0')

key = 'Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8'

n = movie_list1.index(key)

print(n)

print(" ")

# max
print("--max--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list1.insert('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list1.insert('Zulu|1964|Cy Endfield|7.8|9')
movie_list1.insert('Dark City|1998|Alex Proyas|7.8|0')

value = movie_list1.max()

print(value)

print(" ")

# max
print("--min--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list1.insert('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list1.insert('Zulu|1964|Cy Endfield|7.8|9')
movie_list1.insert('Dark City|1998|Alex Proyas|7.8|0')

value = movie_list1.min()

print(value)

print(" ")

# peek
print("--peek--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

value = movie_list1.peek()

print(value)

print(" ")

# remove
print("--remove--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

key = 'Z|1969|Costa-Gavras|8.2|2'

value = movie_list1.remove(key)

print(value)

print(" ")
print("List after removing:")
for i in movie_list1:
    print(i)

print(" ")

# split_key
print("--split_key--")
movie_list1 = Sorted_List()

movie_list1.insert('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.insert('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.insert('Z|1969|Costa-Gavras|8.2|2')
movie_list1.insert(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.insert('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.insert('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list1.insert('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list1.insert('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list1.insert('Zulu|1964|Cy Endfield|7.8|9')
movie_list1.insert('Dark City|1998|Alex Proyas|7.8|0')

target1 = Sorted_List()
target2 = Sorted_List()

key = 'Omega Man, The|1971|Boris Sagal|6.6|0,6'

target1, target2 = movie_list1.split_key(key)

print("Target1:")
for i in target1:
    print(i)

print(" ")

print("Target2:")
for i in target2:
    print(i)
