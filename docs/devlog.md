# Devlog — AI Learning Lab

A day-by-day record of what I learned, built, and figured out.

---

## Phase 2 — ML & Data Science

---

### Phase 2 Start — Program Reset & New Direction
**Date:** 2026-04-27

Phase 1 (Python Fundamentals, Days 1–13) is complete. Today marks the beginning of a new, structured push toward AI engineering.

**What's changing:**
- Joined Pupilica's 42-hour AI bootcamp (starts April 28, runs Tue/Thu/Sat through May 22)
- Starting Microsoft Turkey AI Innovators internship (~June 2025)
- Rebuilt the full learning program from scratch: Python Advanced → ML → Deep Learning → LLM/AI Engineering → MLOps
- Target: job-ready as a junior AI engineer by September 1, 2025

**Program structure:**
- ~30 hours/week self-study
- Bootcamp days (Tue/Thu/Sat): 10:00–13:00 personal study + 18:00–21:00 bootcamp + 21:00–22:00 review
- Free days (Mon/Wed/Fri): 5 hours personal plan
- Sunday: rest, no studying

**Repository structure going forward:**
- `ai-learning-lab` (this repo) — central hub, detailed devlog, all phases
- `pupilica-bootcamp` — bootcamp notes, exercises, final project
- `fintrack` — evolving project: v1.5 (May) → v2 (June)
- `microsoft-internship` — starting ~June 2025

**Phase 2 focus (Apr 27 – May 22):**
- Week 1: Python advanced (OOP, file I/O, comprehensions, error handling)
- Week 2: NumPy, Pandas, visualisation
- Week 3: Supervised ML with Scikit-learn
- Week 4: Unsupervised ML, math foundations, end-to-end pipeline

---

## Phase 1 — Python Fundamentals

---

### 2026-03-01 — Variables

First day of the journey. Covered the absolute basics: how Python handles variables, how dynamic typing works (Python figures out the type at runtime, no declarations needed), and the `snake_case` naming convention. Practiced `print()`, `input()`, f-strings, and type conversion with `int()`. The key insight today was that f-strings are cleaner than concatenation — they make the intent readable at a glance.

```python
name = "Bilge"
age = 25
print(f"Hello {name}, you are {age} years old.")
user_age = int(input("Enter your age: "))
```

---

### 2026-03-02 — Data Types & String Manipulation

Went deeper into Python's type system. Learned the four primitive types (`int`, `float`, `str`, `bool`), how to check types with `type()`, and how to cast between them. Arithmetic operators felt familiar, but `//` (floor division) and `%` (modulus) are ones to remember — they come up constantly. String methods like `.upper()`, `.lower()`, `.strip()` were also covered.

```python
print(10 // 3)   # 3  — floor division
print(10 % 3)    # 1  — modulus
print(2 ** 8)    # 256 — exponent
```

---

### 2026-03-03 — Control Flow & Operators

Conditionals today. `if / elif / else` with comparison and logical operators. Nested conditions are where it gets interesting — the indentation-based structure forces you to think clearly about the logic tree. Built the Treasure Island text game, which was a good exercise in branching: every wrong path ends differently.

```python
age = 20
if age >= 18 and age < 65:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    print("Minor")
```

**Project:** Treasure Island — text-based adventure, nested conditionals, `.lower()` for input normalization.

---

### 2026-03-04 — Lists & Randomisation

Lists are Python's workhorse. Covered creation, indexing (including negative), slicing, and the key methods: `append()`, `remove()`, `len()`. The `random` module — `random.choice()` and `random.shuffle()` — opens up a lot of possibilities. Built a Rock Paper Scissors game where the computer picks randomly.

```python
import random
choices = ["Rock", "Paper", "Scissors"]
cpu = random.choice(choices)
random.shuffle(choices)
```

**Project:** Rock Paper Scissors — `random.choice()`, all outcomes covered.

**Bonus:** Rock Paper Scissors Lizard Spock — extended to 5 choices and 10 win conditions.

---

### 2026-03-05 — Loops

Loops are the backbone of most programs. Covered `for` with `range(start, stop, step)`, looping through lists and strings, and `while`. The control flow keywords `break`, `continue`, `pass` add real power. `enumerate()` is a clean way to get both index and value without maintaining a counter manually.

```python
for i in range(1, 10, 2):     # 1, 3, 5, 7, 9
    print(i)

for index, char in enumerate("Python"):
    print(index, char)
```

**Project:** Password Generator — loops over letter/symbol/number sets, `random.shuffle()` for final randomization.

---

### 2026-03-06 — Functions

Functions are the foundation of reusable code. Learned `def`, parameters, return values, default parameter values, and keyword arguments. The main takeaway: a function should do one thing and do it well.

```python
def greet(name="stranger"):
    return f"Hello {name}!"

print(greet())              # Hello stranger!
print(greet(name="Bilge"))  # Hello Bilge!
```

---

### 2026-03-07 — Hangman Project

First major project that combines everything learned so far. The key technique: start with a list of underscores `['_'] * len(word)`, then use `enumerate()` to replace at the correct index when a letter is guessed correctly.

```python
display = ['_'] * len(chosen_word)
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess
```

**Project:** Hangman — random word selection, lives system, already-guessed tracking, ASCII art stages.

---

### 2026-03-08 — Function Parameters & Caesar Cipher

Went deeper into how Python handles function arguments. `*args` lets a function accept any number of positional arguments as a tuple; `**kwargs` does the same for keyword arguments as a dict. These are used everywhere in Python's standard library and frameworks.

```python
def total(*numbers):
    return sum(numbers)

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
```

**Project:** Caesar Cipher — letter shifting encoder/decoder, handles upper/lowercase, runs in loop until quit.

---

### 2026-03-09 — Dictionaries & Silent Auction

Dictionaries are the most important data structure in Python after lists. Covered full CRUD, the three iteration methods (`.keys()`, `.values()`, `.items()`), and nested dictionaries. The `max()` function with `key=dict.get` is a pattern worth memorising.

```python
winner = max(bids, key=bids.get)
```

**Project:** Silent Auction — bids stored in a dict, highest bidder found with `max(key=bids.get)`.

---

### 2026-03-10 — Functions as Outputs & Calculator

Functions in Python are first-class objects — they can be stored in variables, passed as arguments, and returned from other functions. Storing operations in a dictionary and calling them dynamically is a key pattern.

```python
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
result = operations[operator](n1, n2)
```

**Project:** Calculator — operations in a dict, dynamic calls, chained calculations, division-by-zero guard.

---

### 2026-03-11 — Blackjack Project

The most complex project so far. The Ace rule (11 or 1 depending on the total score) is the trickiest part. The game needed multiple functions working together: dealing, scoring, the dealer's turn, and outcome checking.

```python
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0   # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
```

**Project:** Blackjack — dealer logic, dynamic Ace handling, all game outcomes covered.

---

### 2026-03-12 — Scope & Number Guessing Game

Scope is one of those concepts that seems simple but causes real bugs if misunderstood. Python's rule: a function can read a global variable but cannot reassign it without the `global` keyword. The real lesson: avoid needing `global` at all — pass values through parameters and return them.

```python
x = 10  # global

def my_func():
    y = 5   # local
    print(x)  # can read global ✅

# print(y)  # ❌ NameError outside function
```

**Project:** Number Guessing Game — difficulty levels (easy: 10 lives, hard: 5), hints, clean scope throughout.

---

### 2026-03-13 — Debugging

Debugging is a skill, not just a reflex. Three error types: Syntax (caught before run), Runtime (during execution), Logic (program runs but wrong answer — hardest). Most useful technique: isolate the bug with `print()` at each step to trace actual values.

```python
def find_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # ✅ fixed
```

**Project:** Debugging Challenge — three buggy functions (FizzBuzz, Celsius converter, average calculator), each identified and fixed.

---

---

### 2026-04-20 — Higher or Lower Project

A game built around a real-world dataset: 45 Instagram accounts with follower counts. Two accounts are shown, the player guesses which has more followers. Correct guess = score increases and the game continues; wrong guess = game over.

The interesting design decision here: `account_b` becomes the new `account_a` on the next round instead of picking two fresh accounts each time. This keeps the game flowing naturally and avoids repetition. A `while` guard handles the edge case where both accounts are the same.

Multi-file structure used for the first time — `main.py`, `game_data.py`, `art.py` separated cleanly. `format_account()` and `check_answer()` kept as pure functions with no side effects.

```python
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
```

**Project:** Higher or Lower — follower count guessing game, multi-file architecture, score tracking, duplicate account guard.

---

*Last updated: 2026-04-27*