## 2. Introduction to the Data ##

import csv
f=open("nfl_suspensions_data.csv","r")
csvread=csv.reader(f)
nfl_suspensions = list(csvread)
nfl_suspensions = nfl_suspensions[1:len(nfl_suspensions)]

years={}
for each in nfl_suspensions:
    year = each[5]
    if year in years:
        years[year]=years[year]+1
    else:
        years[year]=1
print(years)

## 3. Unique Values ##

teams= [each[1] for each in nfl_suspensions ]
unique_teams = set(teams)
games= [each[2] for each in nfl_suspensions]
unique_games=set(games)
unique_teams
unique_games

## 4. Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name=row[0]
        self.team=row[1]
        self.games=row[2]
        self.year=row[5]
third_suspension= Suspension(nfl_suspensions[2])

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)

missing_year = Suspension(nfl_suspensions[22])

twenty_third_year = missing_year.get_year()