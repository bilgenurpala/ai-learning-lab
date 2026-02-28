# 🐍 Python Interview Training

> A structured day-by-day Python learning journey — from beginner to advanced, focused on writing clean, readable, and interview-ready code.

![Progress](https://img.shields.io/badge/Progress-Day%2013%20of%20100-orange)
![Level](https://img.shields.io/badge/Level-Beginner-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-blue?logo=visualstudiocode)

---

## 📌 About This Repository

This repository documents my **100 Days of Python** journey. Each day covers a specific topic with hands-on practice, algorithm challenges, and mini projects. The goal is to build a strong foundation from beginner fundamentals all the way to advanced Python concepts — while developing the habits of a professional developer.

---

## 📁 Repository Structure

```
python-interview-training/
│
├── beginner-python/
│   ├── day01_variables.py
│   ├── day02_data_types.py
│   ├── day03_control_flow_operators.py
│   ├── day04_lists.py
│   ├── day05_loops.py
│   ├── day06_functions.py
│   ├── day07_hangman/
│   │   ├── hangman_game.py
│   │   └── pic/
│   ├── day08_function_parametres.py
│   ├── day09_dictionaries.py
│   ├── day10_functions_outputs.py
│   ├── day11_the_blackjack_project/
│   │   └── blackjack.py
│   ├── day12_scope_and_numberGuessing_project/
│   │   └── guessing-game.py
│   └── day13_debugging.py
│
└── README.md
```

---

## 📅 Progress Log

---

### ✅ Day 1 – Variables

**Topics Covered:**
- `print()` function and basic output
- Variables and dynamic typing — Python infers types at runtime
- Variable naming rules and `snake_case` convention
- Basic data types: `str`, `int`
- String formatting with f-strings (Python 3.6+)
- `input()` function and type conversion with `int()`

**Key Concepts:**
```python
name = "Bilge"
age = 25
print(f"Hello {name}, you are {age} years old.")

user_age = int(input("Enter your age: "))  # type casting
```

---

### ✅ Day 2 – Data Types & String Manipulation

**Topics Covered:**
- Primitive data types: `int`, `float`, `str`, `bool`
- Checking types with `type()`
- Type conversion (casting) between types
- Mathematical operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- String manipulation basics

**Key Concepts:**
```python
print(type(3.14))       # <class 'float'>
print(10 // 3)          # 3 — floor division
print(10 % 3)           # 1 — modulus
print(2 ** 8)           # 256 — exponent
```

---

### ✅ Day 3 – Control Flow & Operators

**Topics Covered:**
- Conditional statements: `if`, `elif`, `else`
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical operators: `and`, `or`, `not`
- Nested conditions

**Key Concepts:**
```python
age = 20
if age >= 18 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior.")
else:
    print("You are a minor.")
```

**🎮 Project: Treasure Island Game**
> A text-based adventure game where the player makes choices at each step. Wrong choices end the game with unique messages. Built with nested `if/elif/else` statements and `.lower()` for input normalization.

---

### ✅ Day 4 – Lists & Randomisation

**Topics Covered:**
- List creation, indexing, and negative indexing
- Slicing: `list[start:end]`
- Methods: `append()`, `remove()`, `len()`
- Looping through lists with `for`
- `random` module: `random.choice()`, `random.shuffle()`

**Key Concepts:**
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits[-1])             # last item

import random
print(random.choice(fruits))  # random item
random.shuffle(fruits)        # shuffle in place
```

**🎮 Project: Rock Paper Scissors**
> The computer picks randomly from a list using `random.choice()`. The player's input is normalized with `.capitalize()` and all win/lose/draw outcomes are handled.

---

### ✅ Day 5 – Loops

**Topics Covered:**
- `for` loop with `range(start, stop, step)`
- Looping through lists and strings
- Building strings character by character in a loop
- `while` loop with condition
- Loop control: `break`, `continue`, `pass`
- `enumerate()` for index + value iteration

**Key Concepts:**
```python
for i in range(1, 10, 2):      # 1, 3, 5, 7, 9
    print(i)

for index, char in enumerate("Python"):
    print(index, char)
```

**🎮 Project: Password Generator**
> Asks the user for the number of letters, symbols, and numbers. Uses `for` loops to randomly pick characters from predefined sets, then shuffles the result with `random.shuffle()` for a secure, randomized password.

---

### ✅ Day 6 – Functions

**Topics Covered:**
- Defining and calling functions with `def`
- Parameters and arguments
- `return` statement and return values
- Default parameter values
- Keyword arguments

**Key Concepts:**
```python
def greet(name="stranger"):
    return f"Hello {name}!"

print(greet())              # Hello stranger!
print(greet(name="Bilge"))  # keyword argument
```

---

### ✅ Day 7 – Hangman Project

**Topics Covered:**
- Combining loops, lists, functions, and randomisation
- Dynamic list generation with `['_'] * len(word)`
- `enumerate()` for index-based replacement
- Tracking game state across loop iterations
- Already-guessed letter tracking

**🎮 Project: Hangman Game**
> A fully functional Hangman game. A random word is selected from a word list and displayed as blanks. The player guesses letters one by one — correct guesses reveal the letter in all matching positions, wrong guesses cost a life.

```python
display = ['_'] * len(chosen_word)
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess
```

---

### ✅ Day 8 – Function Parameters & Caesar Cipher

**Topics Covered:**
- Positional vs keyword arguments
- Default parameter values
- `*args` — unlimited positional arguments
- `**kwargs` — unlimited keyword arguments

**Key Concepts:**
```python
def total(*numbers):
    return sum(numbers)

total(1, 2, 3, 4)  # 10

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
```

**🎮 Project: Caesar Cipher**
> An encoder/decoder that shifts each letter in a message by a given number. Supports both uppercase and lowercase letters while leaving symbols and numbers unchanged. Runs in a loop until the user chooses to quit.

---

### ✅ Day 9 – Dictionaries & Silent Auction

**Topics Covered:**
- Dictionary creation, accessing, updating, and deleting keys
- `.keys()`, `.values()`, `.items()` methods
- Looping through dictionaries with `for`
- Nested dictionaries
- `max()` with `key=dict.get`

**Key Concepts:**
```python
person = {"name": "Bilge", "age": 25}
person["city"] = "Istanbul"    # add key
del person["city"]             # delete key

for key, value in person.items():
    print(f"{key}: {value}")

winner = max(bids, key=bids.get)  # find key with highest value
```

**🎮 Project: Silent Auction**
> Multiple bidders enter their name and bid amount. All bids are stored in a dictionary. After all bids are collected, the program finds and announces the highest bidder using `max()` with `key=bids.get`.

---

### ✅ Day 10 – Functions as Outputs & Calculator

**Topics Covered:**
- Functions as first-class objects
- Storing functions inside dictionaries
- Calling functions dynamically
- Recursive functions

**Key Concepts:**
```python
def add(a, b): return a + b
def subtract(a, b): return a - b

operations = {"+": add, "-": subtract}
operations["+"](3, 5)   # 8 — dynamic function call
```

**🎮 Project: Calculator**
> A fully functional calculator that stores operations in a dictionary and calls them dynamically. Supports chained calculations where the result becomes the next first number. Handles division by zero gracefully.

---

### ✅ Day 11 – Blackjack Project

**Topics Covered:**
- Combining all beginner concepts in a complex project
- Multiple functions working together
- Game state management across loop iterations
- Edge case handling (Blackjack, Bust, Ace switching)

**🎮 Project: Blackjack Game**
> A fully functional Blackjack card game. Handles Ace as 11 or 1 dynamically, dealer draws until 17, all win/lose/draw/blackjack/bust scenarios are covered.

```python
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0   # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)  # Ace switches from 11 to 1
    return sum(hand)
```

---

### ✅ Day 12 – Scope & Number Guessing Game

**Topics Covered:**
- Local vs global scope
- `global` keyword
- Constants convention (`UPPER_CASE`)
- Keeping functions pure — no global variables

**Key Concepts:**
```python
x = 10  # global scope

def my_func():
    y = 5   # local scope
    print(x)  # can access global ✅

print(y)  # ❌ NameError — not accessible outside
```

**🎮 Project: Number Guessing Game**
> The computer picks a random number between 1 and 100. The player chooses a difficulty (easy: 10 lives, hard: 5 lives) and guesses the number with "Too high" / "Too low" hints. No global variables used — scope is kept clean throughout.

---

### ✅ Day 13 – Debugging

**Topics Covered:**
- 3 types of errors: Syntax, Runtime, Logic
- Print debugging technique
- Python debugger (`pdb`)
- `try` / `except` for error handling
- Rubber duck debugging

**Key Concepts:**
```python
# Syntax Error — caught before running
if x == 10    # ❌ missing colon

# Runtime Error — caught while running
result = 10 / 0   # ❌ ZeroDivisionError

# Logic Error — hardest to catch
return total / len(numbers) + 1  # ❌ wrong result

# try / except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**🐛 Project: Debugging Challenge**
> A set of three buggy functions covering all three error types — FizzBuzz (syntax), Celsius converter (runtime), and average calculator (logic). Each bug is identified, fixed, and explained.

---

## 🗺️ Roadmap

| Phase | Days | Status |
|---|---|---|
| 🟢 Beginner | Day 1 – Day 14 | ✅ Almost Complete |
| 🟡 Intermediate | Day 15 – Day 60 | ⏳ Upcoming |
| 🔴 Advanced | Day 61 – Day 100 | ⏳ Upcoming |

---

## 🎯 Goals

- Build a solid foundation in Python from beginner to advanced
- Practice writing clean, readable, interview-ready code
- Complete daily algorithm challenges and mini projects
- Document every step for portfolio and future review

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-blue?logo=visualstudiocode)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)

---

## 👩‍💻 About

This repo is part of my personal journey to master Python and prepare for technical interviews. I'm working through the **100 Days of Code: Python** curriculum, adding my own algorithm exercises and project extensions along the way.

> *"The best way to learn programming is to write a lot of programs."* — Brian Kernighan
