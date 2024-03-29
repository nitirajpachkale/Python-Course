## 1. Overview ##

f = open("movie_metadata.csv","r")
data = f.read()
rows = data.split("\n")
movie_data = []
for row in rows:
    dt = row.split(",")
    movie_data.append(dt)
print(movie_data[0:5])    

## 3. Writing Our Own Functions ##

def movie_names_fun(movie_data_l):
    mname = []
    for md in movie_data_l:
        mn = md[0]
        mname.append(mn)
    return mname  
movie_names = movie_names_fun(movie_data)
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
def is_usa(data_l):
    if data_l[6] == "USA":
        return True
    else:
        return False

wonder_woman_usa = is_usa(wonder_woman)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
def index_equals_str(i_list,i_index,i_str):
    if i_list[i_index] == i_str:
        return True
    else:
        return False
wonder_woman_in = index_equals_str(i_list=wonder_woman,i_str="USA",i_index=6)
wonder_woman_in_color = index_equals_str(wonder_woman,6,"USA")    

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt
def feature_counter(d_list,d_index,d_str,d_header=False):
    count = 0
    if d_header == True:
        d_list = d_list[1:len(d_list)] 
    for md in d_list:
        if md[d_index] == d_str:
            count = count + 1
    return count  
num_of_us_movies = feature_counter(movie_data,6,"USA",True)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt
def summary_statistics(d_list):
    num_japan_films = feature_counter(d_list,6,"Japan",True)
    num_color_films = feature_counter(d_list,2,"Color",True)
    num_films_in_english = feature_counter(d_list,5,"English",True)
    count_data = {"japan_films":num_japan_films,                 "color_films":num_color_films, "films_in_english":num_films_in_english}
    return count_data

summary = summary_statistics(movie_data)

    