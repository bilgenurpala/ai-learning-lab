# 🐍 Python Interview Training

> A structured day-by-day Python learning journey — from beginner to advanced, focused on writing clean, readable, and interview-ready code.

![Progress](https://img.shields.io/badge/Progress-Day%208%20of%20100-orange)
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
│   │   └── pic/                  # Flowchart diagrams
│   ├── day08_function_parametres.py
│   └── caesar_cipher.py
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
name = "Bilge"           # str
age = 25                 # int
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
print(type(3.14))        # <class 'float'>
print(type(True))        # <class 'bool'>

print(10 / 3)            # 3.3333 — float division
print(10 // 3)           # 3      — floor division
print(10 % 3)            # 1      — modulus
print(2 ** 8)            # 256    — exponent
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
> A text-based adventure game where the player makes choices at each step. Wrong choices end the game with unique messages. Built entirely with nested `if/elif/else` statements and `.lower()` for input normalization.

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
fruits.append("mango")       # add to end
fruits.remove("banana")      # remove by value
print(fruits[-1])             # last item: "cherry"

import random
print(random.choice(fruits))  # random item
random.shuffle(fruits)        # shuffle in place
```

**🎮 Project: Rock Paper Scissors**
> A classic game where the computer picks randomly from a list using `random.choice()`. The player's input is normalized with `.capitalize()` and all win/lose/draw outcomes are handled.

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
    print(index, char)         # 0 P, 1 y, 2 t ...

count = 0
while count < 5:
    count += 1
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

print(greet())            # Hello stranger!
print(greet("Bilge"))     # Hello Bilge!
print(greet(name="Bilge"))  # keyword argument
```

---

### ✅ Day 7 – Hangman Project

**Topics Covered:**
- Combining loops, lists, functions, and randomisation
- Dynamic list generation with `['_'] * len(word)`
- `enumerate()` for index-based replacement
- Tracking game state across loop iterations

**🎮 Project: Hangman Game**
> A fully functional Hangman game. A random word is selected from a word list, displayed as blanks. The player guesses letters one by one — correct guesses reveal the letter in all matching positions, wrong guesses cost a life. The game tracks already-guessed letters and ends on win or game over.

```python
display = ['_'] * len(chosen_word)   # generate blanks
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess       # reveal letter
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

total(1, 2, 3, 4)    # 10 — any number of args

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe(name="Bilge", age=25)
```

**🎮 Project: Caesar Cipher**
> An encoder/decoder that shifts each letter in a message by a given number. Supports both uppercase and lowercase letters while leaving symbols and numbers unchanged. Runs in a loop until the user chooses to quit.

```python
def caesar(text, shift, direction):
    # shift each letter, preserve non-alpha characters
    # supports encode and decode directions
```

---

## 🗺️ Roadmap

| Phase | Days | Status |
|---|---|---|
| 🟢 Beginner | Day 1 – Day 14 | 🔄 In Progress |
| 🟡 Intermediate | Day 15 – Day 60 | ⏳ Upcoming |
| 🔴 Advanced | Day 61 – Day 100 | ⏳ Upcoming |

---

## 🎯 Goals

- Build a solid foundation in Python from beginner to advanced
- Practice writing clean, readable, interview-ready code
- Complete daily algorithm challenges and mini projects
- Document every step for portfolio and future review

---

## 👩‍💻 About

This repo is part of my personal journey to master Python and prepare for technical interviews. I'm working through the **100 Days of Code: Python** curriculum, adding my own algorithm exercises and project extensions along the way.

> *"The best way to learn programming is to write a lot of programs."* — Brian Kernighan
