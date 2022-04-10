## 3. Read the File Into a String ##

f = open("dq_unisex_names.csv","r")
names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = []
first_five.append(names_list[0])
first_five.append(names_list[1])
first_five.append(names_list[2])
first_five.append(names_list[3])
first_five.append(names_list[4])
for ft in first_five:
    print(ft)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for nm in names_list:
    comma_list = nm.split(",")
    nested_list.append(comma_list)
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(nested_list[3])
print(nested_list[4])
    

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for nl in nested_list:
    na = nl[0]
    nm = float(nl[1])
    flist = [na , nm]
    numerical_list.append(flist)
print(numerical_list[0:5])
    

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for nl in numerical_list:
    if nl[1] >= 1000:
        thousand_or_greater.append(nl[0])
print(thousand_or_greater[0:10])