## 1. Introduction ##

import csv
f=open("top100.csv","r")
music =list(csv.reader(f))
print(music[0:5])
artists = []
for row in music:
    artists.append(row[1])
artists = artists[1:len(artists)]


## 2. Extract the Artists Using a List Comprehension ##


    
artists_lc = [(row[1]) for row in music[1:]]

## 3. Getting the Artist Count Using a Function ##

def counter(ilist):
    artc={}
    for row in ilist:
        if row in artc:
            artc[row] = artc[row]+1
        else:
            artc[row] = 1
    return artc

counts = counter(artists)

## 4. Getting the Artist Count Using Collections ##

import collections as co
artist_counts = co.Counter(artists)

## 5. Looping Through Counts Using Items() ##

from collections import Counter
artist_counts = Counter(artists)

# Add your code here
artist_counts_list = []
for first,second in artist_counts.items():
    artist_counts_list.append( [first,second])
print(artist_counts_list) 

## 6. Using a List Comprehension ##

from collections import Counter
artist_counts = Counter(artists)
artist_counts_list = []
artist_counts_two = [[artist,count] for artist,count in artist_counts.items()]
print(artist_counts_two)