"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

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

# __eq__
print("--__eq__--")
movie1 = movie_list[0]
movie2 = movie_list[1]

equal = movie1.__eq__(movie2)
print(equal)

print(" ")

# __getitem__
print("--__getitem__--")
print(movie_list[3])

print(" ")

# append
print("--append--")
new_movie = "25"
movie_list.append(new_movie)
for i in movie_list:
    print(i)

print(" ")

# clean
print("--clean--")
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
movie_list.append('Broken Flowers|2005|Jim Jarmusch|7.2|3,4')
movie_list.append('Darjeeling Limited, The|2007|Wes Anderson|7.1|4')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list.append('Stardust|2007|Matthew Vaughn|7.7|1,4')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')
movie_list.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

movie_list.clean()
for i in movie_list:
    print(i)

print(" ")

# combine
print("--combine--")
movie_list1 = List()

movie_list1.append('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.append('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.append('Z|1969|Costa-Gavras|8.2|2')
movie_list1.append(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.append('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list1.append('Finding Dory|2016|Andrew Stanton, Angus MacLane|7.5|4')
movie_list1.append('Wrong Box, The|1966|Bryan Forbes|7.0|4')
movie_list1.append('Jason and the Argonauts|1963|Don Chaffey|7.4|1,6')
movie_list1.append('Horror of Dracula|1958|Terence Fisher|7.4|8')
movie_list1.append(
    'Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6')

movie_list2 = List()

movie_list2.append('Broken Flowers|2005|Jim Jarmusch|7.2|3,4')
movie_list2.append('Darjeeling Limited, The|2007|Wes Anderson|7.1|4')
movie_list2.append('Juno|2007|Jason Reitman|7.7|3,4')
movie_list2.append('Stardust|2007|Matthew Vaughn|7.7|1,4')
movie_list2.append('Alphaville|1965|Jean-Luc Godard|7.1|0,4')
movie_list2.append('Last Man On Earth, The|1964|Ubaldo Ragona|6.9|0')
movie_list2.append('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list2.append('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list2.append('Zulu|1964|Cy Endfield|7.8|9')
movie_list2.append('Dark City|1998|Alex Proyas|7.8|0')
movie_list2.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

target = List()

target.combine(movie_list1, movie_list2)

for i in target:
    print(i)

print(" ")

# intersection
print("--intersection--")
movie_list1 = List()

movie_list1.append('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.append('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.append('Z|1969|Costa-Gavras|8.2|2')
movie_list1.append(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.append('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list2.append('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list2.append('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list2.append('Zulu|1964|Cy Endfield|7.8|9')
movie_list2.append('Dark City|1998|Alex Proyas|7.8|0')
movie_list2.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

movie_list2 = List()

movie_list2.append('Broken Flowers|2005|Jim Jarmusch|7.2|3,4')
movie_list2.append('Darjeeling Limited, The|2007|Wes Anderson|7.1|4')
movie_list2.append('Juno|2007|Jason Reitman|7.7|3,4')
movie_list2.append('Stardust|2007|Matthew Vaughn|7.7|1,4')
movie_list2.append('Alphaville|1965|Jean-Luc Godard|7.1|0,4')
movie_list2.append('Last Man On Earth, The|1964|Ubaldo Ragona|6.9|0')
movie_list2.append('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list2.append('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list2.append('Zulu|1964|Cy Endfield|7.8|9')
movie_list2.append('Dark City|1998|Alex Proyas|7.8|0')
movie_list2.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

target = List()

target.intersection(movie_list1, movie_list2)

for i in target:
    print(i)

print(" ")

# remove front
print("--remove_front--")
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

print("Initial list")
for i in movie_list:
    print(i)

movie_list.remove_front()

print(" ")
print("After using remove_front")
for i in movie_list:
    print(i)

print(" ")

# remove many
print("--remove_many--")
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

key1 = 'Star Wars: Episode IV - A New Hope|1977|George Lucas|8.7|0,6'
key2 = 'Horror of Dracula|1958|Terence Fisher|7.4|8'

movie_list.remove_many(key1)
movie_list.remove_many(key2)

for i in movie_list:
    print(i)

print(" ")

# split
print("--split--")
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

target1 = List()
target2 = List()
target1, target2 = movie_list.split()

print("Target 1:")
for i in target1:
    print(i)

print(" ")

print("Target 2:")
for i in target2:
    print(i)

print(" ")

# split_alt
print("--split_alt--")
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

target1 = List()
target2 = List()
target1, target2 = movie_list.split_alt()

print("Target 1:")
for i in target1:
    print(i)

print(" ")

print("Target 2:")
for i in target2:
    print(i)

print(" ")

# union
print("--union--")
movie_list1 = List()

movie_list1.append('Zulu|2013|Jerome Salle|6.7|2')
movie_list1.append('Wonder Woman|2017|Patty Jenkins|8.1|1,6')
movie_list1.append('Z|1969|Costa-Gavras|8.2|2')
movie_list1.append(
    'Incredibly Strange Creatures Who Stopped Living and Became Mixed-Up Zombies!!?, The|1964|Ray Dennis Steckler|2.2|8')
movie_list1.append('Manos: The Hands of Fate|1966|Harold P. Warren|1.9|8')
movie_list2.append('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list2.append('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list2.append('Zulu|1964|Cy Endfield|7.8|9')
movie_list2.append('Dark City|1998|Alex Proyas|7.8|0')
movie_list2.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

movie_list2 = List()

movie_list2.append('Broken Flowers|2005|Jim Jarmusch|7.2|3,4')
movie_list2.append('Darjeeling Limited, The|2007|Wes Anderson|7.1|4')
movie_list2.append('Juno|2007|Jason Reitman|7.7|3,4')
movie_list2.append('Stardust|2007|Matthew Vaughn|7.7|1,4')
movie_list2.append('Alphaville|1965|Jean-Luc Godard|7.1|0,4')
movie_list2.append('Last Man On Earth, The|1964|Ubaldo Ragona|6.9|0')
movie_list2.append('Omega Man, The|1971|Boris Sagal|6.6|0,6')
movie_list2.append('I Am Legend|2007|Francis Lawrence|7.1|0,6')
movie_list2.append('Zulu|1964|Cy Endfield|7.8|9')
movie_list2.append('Dark City|1998|Alex Proyas|7.8|0')
movie_list2.append('Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8')

target = List()

target.union(movie_list1, movie_list2)

for i in target:
    print(i)