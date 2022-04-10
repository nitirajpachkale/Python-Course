## 1. Introduction to the Data ##

f500_head = f500.head(10)
print(f500.info())

## 2. Vectorized Operations ##

r = f500.loc[:,"rank"]
p = f500.loc[:,"previous_rank"]
rank_change = p - r 

## 3. Series Data Exploration Methods ##

rank_change =  f500["previous_rank"] - f500["rank"]
rank_change_max = rank_change.max()
rank_change_min = rank_change.min()

## 4. Series Describe Method ##

rank = f500.loc[:,"rank"]
rank_desc = rank.describe()
prev_rank = f500.loc[:,"previous_rank"]
prev_rank_desc = prev_rank.describe()

## 5. Method Chaining ##

previous_rank_count = f500.loc[:,"previous_rank"].value_counts()
print(previous_rank_count)
zero_previous_rank = previous_rank_count.loc[0]

## 6. Dataframe Exploration Methods ##

max_f500 = f500.max(axis=0,numeric_only = True)
print(max_f500)

## 7. Dataframe Describe Method ##

f500_desc = f500.describe()

## 8. Assignment with pandas ##

f500.loc["Dow Chemical","ceo"] = "Jim Fitterling" 

## 9. Using Boolean Indexing with pandas Objects ##

motor_bool = f500["industry"] == "Motor Vehicles and Parts"
motor_countries = f500.loc[motor_bool,"country"]


## 10. Using Boolean Arrays to Assign Values ##

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
prev_bool = f500["previous_rank"] == 0
f500.loc[prev_bool,"previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()

## 11. Creating New Columns ##

rank = f500.loc[:,"rank"]
previous_rank = f500.loc[:,"previous_rank"]
f500["rank_change"] = previous_rank - rank
rank_change_desc = f500.loc[:,"rank_change"].describe()

## 12. Challenge: Top Performers by Country ##

top_3_countries = f500["country"].value_counts().head(3)
industry_usa = f500["industry"][f500["country"] == "USA"].value_counts().head(2)
sector_china = f500["sector"][f500["country"] == "China"].value_counts().head(3)
mean_employees_japan = f500["employees"][f500["country"] == "Japan"].mean()

## 12. Challenge: Top Performers by Country ##

top_3_countries = f500["country"].value_counts().head(3)
industry_usa = f500["industry"][f500["country"] == "USA"].value_counts().head(2)
sector_china = f500["sector"][f500["country"] == "China"].value_counts().head(3)
mean_employees_japan = f500["employees"][f500["country"] == "Japan"].mean()