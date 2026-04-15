# Leap Year

## Rules:

## Create a function called is_leap_year(year) that takes a year as parameter
## A year is a leap year if:

## It is divisible by 4 and
## If divisible by 100, it must also be divisible by 400

##Return True or False
## Ask the user to enter a year and print whether it is a leap year or not

## Examples:
## 2000 → Leap year ✅
## 1900 → Not a leap year ❌
## 2024 → Leap year ✅

def is_leap_year(year):
    # if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    #     return True
    # else:
    #     return False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year_input = int(input("Enter a year: "))
if is_leap_year(year_input):
    print(f"{year_input} is a leap year.")
else:   
    print(f"{year_input} is not a leap year.")


