## 2. Sets ##

gender = []
for row in legislators:
    gender.append(row[3])
gender = set(gender)
print(gender)

    

## 3. Exploring the Dataset ##

party = []
for row in legislators:
    party.append(row[6])
party = set(party)
print(party)
print(legislators)

## 4. Missing Values ##

for row in legislators:
    if row[3] == "":
        row[3] = "M"

## 5. Parsing Birth Years ##

birth_years = []
for row in legislators:
    dob = row[2]
    parts = dob.split("-")
    birth_years.append(parts[0])
    

## 6. Try/except Blocks ##

try:
    float(hello)
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except Exception:
        pass

## 9. Convert Birth Years to Integers ##


for row in legislators:
    dob = row[2]
    parts = dob.split("-")
    try:
        birth_year = int(parts[0])  
    except Exception:
        birth_year = 0
    row.append(birth_year)
        

        

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7]=last_value
    else: 
        last_value =row[7]
    