## 1. The Time Module ##

import time
current_time=time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime(year=2019,month=1,day=1)
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime
kirks_birthday = datetime.datetime(year=2233,month=3,day=22)
diff = datetime.timedelta(weeks=15)
before_kirk = kirks_birthday-diff

## 5. Formatting Dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime 
mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string,"%I:%M%p on %A %B %d, %Y")
print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime
for post in posts:
    tt = datetime.datetime.fromtimestamp(float(post[2]))
    post[2] = tt

## 9. Counting Posts from March ##

march_count = 0
for post in posts:
    if post[2].month == 3:
        march_count=march_count+1

## 10. Counting Posts from Any Month ##

def postcount(n):
    count_posts_in_month=0
    for post in posts:
        if post[2].month == n:
            count_posts_in_month=count_posts_in_month+1
    return count_posts_in_month

feb_count = postcount(2)
aug_count = postcount(8)