## 1. Reading CSV files with NumPy ##

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv',delimiter=',')
taxi_shape = taxi.shape
print(taxi_shape)

## 2. Reading CSV Files with NumPy Continued ##

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv',delimiter=',',skip_header=1)
taxi_shape = taxi.shape

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])
a_bool = a < 3
b_bool = b == 'blue'
c_bool = c > 100


## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]
total = pickup_month.shape[0]
print(total)
print(february_rides)

## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool,5:14]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[28214,5] = 1
taxi_modified[:,0] = 16
col7 = taxi_modified[:,7] 
taxi_modified[1800:1802,7] = col7.mean()  

## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()
total_amount = taxi_copy[:,13]
total_amount_bool = total_amount < 0
total_amount[total_amount_bool] = 0

## 8. Assignment Using Boolean Arrays Continued ##

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)
taxi_modified[taxi_modified[:,5] == 2 , 15] = 1
taxi_modified[taxi_modified[:,5] == 3 , 15] = 1
taxi_modified[taxi_modified[:,5] == 5 , 15] = 1

## 9. Challenge: Which Is the Most Popular Airport? ##

jfk_bool = taxi[:,6] == 2
jfk = taxi[jfk_bool]
jfk_count = jfk.shape

laguardia_bool = taxi[:,6] == 3
laguardia = taxi[laguardia_bool]
laguardia_count = laguardia.shape

newark_bool = taxi[:,6] == 5
newark = taxi[newark_bool]
newark_count = newark.shape



## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi = taxi[trip_mph < 100]
mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()