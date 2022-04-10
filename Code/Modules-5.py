## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)
print(root)
print(flr)

## 2. Importing Using An Alias ##

import math as m
root = m.sqrt(33)
print(root)

## 3. Importing A Specific Object ##

from math import *
root = math.sqrt(1001)

## 4. Variables Within Modules ##

import math
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)
print(math.pi)
print(a)
print(b)
print(c)

## 5. The CSV Module ##

import csv
f = open("nfl.csv")
data = csv.reader(f)
nfl = list(data) 

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))
patriots_wins = 0
for li in nfl:
    if li[2] == "New England Patriots":
        patriots_wins = patriots_wins + 1

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.

def nfl_wins(team):
    count = 0
    for li in nfl:
        if team == li[2]:
            count = count + 1
    return count
cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")
print(cowboys_wins)
print(falcons_wins)