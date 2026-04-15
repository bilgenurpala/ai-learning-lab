# Task 1

# 1. Creates a variable called "city"
# 2. Creates a variable called "year"
# 3. Prints this sentence: "I live in ___ and the year is ___."

city = "Belgrade"
year = 2026
# print("I live in " + city + " and the year is " + str(year) + ".")
print(f"I live in {city} and the year is {year}.")

# Task 2

# 1. Asks the user: "What is your name?", "How old are you?"
# 2. Prints this sentence: "Hello ___, you are ___ years old."
# 3. Rules:  Use input(), use f-strings, do NOT use concatenation.

name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are {age} years old.")

# Task 3

# 1. Creates 3 variables: first_name, country, and favorite_language
# 2. Prints this sentence: "My name is ___, I live in ___ and my favorite programming language is ___."
# 3. Rules: Use f-strings, do NOT use concatenation.

first_name = "Bilge"
country = "Turkey"
favorite_language = "Python"
print(f"My name is {first_name}, I live in {country} and my favorite programming language is {favorite_language}.")