## 1. Introduction ##

# Stream column for top 5 songs only
top5_streams = [2993988783, 1829621841, 1460802540, 1386258295, 1311243745]
def average(inplist):
    n = len(top5_streams)
    lsum = 0
    for i in inplist:
        lsum = lsum + i
    avg = (lsum/n)
    return avg
total_average = average(top5_streams)
    

## 2. Introduction to Modules ##

import statistics as st
top5_streams = [2993988783, 1829621841, 1460802540, 1386258295, 1311243745]
average = st.mean(top5_streams)

## 3. Loading our data using the CSV module ##

import csv
f = open("top100.csv","r")
csvreader = csv.reader(f)
music = list(csvreader)

## 4. Understanding the namespace ##

import statistics
dir()
dir(statistics)

## 5. Cleaning Our Data ##

import csv
f = open("top100.csv","r")
music = list(csv.reader(f))
stream_numbers=[]
track_names=[]
music = music[1:len(music)]
for row in music:
    track_names.append(row[0])
    stream_numbers.append(int(row[3]))
    

## 6. Writing Modular Code ##

import csv
def read_data(fname):
    f = open(fname,"r")
    music = list(csv.reader(f))
    return music

def get_data(ilist):
    stream_numbers = []
    track_names = []
    for song in music[1:]:
        stream_numbers.append(int(song[3]))
        track_names.append(song[0])

dir()

## 7. Local and Global Variables ##

filename= "top100.csv"
def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))
f = read_data(filename)

## 8. Using Programming Paradigms ##

import csv
def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))


def get_data(data):
    list1 = []
    list2 = []
    for x in data[1:]:
        list1.append(int(x[3]))
        list2.append(x[0])
    return list1, list2

def ceil(data):
    ceiling = 0
    for x in data:
        if x > ceiling:
            ceiling = x
        else:
            ceiling
    return ceiling

def average(data):
    total = 0
    for x in data:
        total += x
    return total/len(data)

music = read_data("top100.csv")
stream_numbers,track_names=get_data(music)
average= average (stream_numbers)

## 9. Importing using an Alias ##

import statistics as s
variation = s.stdev(stream_numbers)

## 10. Importing Specific Objects ##

from statistics import mean,stdev,median

average= mean(stream_numbers)
variation = stdev(stream_numbers)
med=median(stream_numbers)
print(average,variation,med)