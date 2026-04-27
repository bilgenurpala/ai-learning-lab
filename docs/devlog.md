# Devlog — AI Learning Lab

A day-by-day record of what I learned, built, and figured out.

---

## Phase 2 — ML & Data Science

---

### Phase 2 Start — Program Reset & New Direction
**Date:** 2026-04-27

Phase 1 is done. 13 days, 14 projects, Python fundamentals covered. Today I'm resetting the structure and committing to a serious push toward AI engineering.

The goal is clear: by September 1, 2025, I want to be job-ready as a junior AI engineer. Not just someone who finished a few courses — someone with real deployed projects, a strong GitHub, and hands-on experience.

**What's lined up:**
- Pupilica AI Bootcamp — 42 hours of live instruction, April 28 – May 22 (Tue/Thu/Sat)
- Microsoft Turkey AI Innovators internship — starting ~June 2025
- Self-study: ~30 hours/week across all phases

**The full path:**
- Phase 2 (now – May 22): Python advanced + full ML stack, running alongside the bootcamp
- Phase 3 (May 23 – Aug 3): Deep learning, NLP, Transformers, LLMs, RAG, FinTrack v2
- Phase 4 (Aug 4 – Sep 1): MLOps, deployment, portfolio polish

**Repository structure from here:**
- `ai-learning-lab` — this repo, central hub, detailed devlog
- `pupilica-bootcamp` — bootcamp notes, exercises, final project
- `fintrack` — v1.5 by end of May, v2 by end of June
- `microsoft-internship` — starting ~June 2025

The approach stays the same: documentation and code over videos, build things rather than just watch things, commit every day.

---

## Phase 1 — Python Fundamentals

---

### 2026-03-01 — Variables

First day. Covered how Python handles variables, dynamic typing, and the `snake_case` convention. Practiced `print()`, `input()`, f-strings, and type conversion.

**Key takeaways:**
- Python infers types at runtime — no declarations needed
- f-strings are cleaner and more readable than string concatenation
- `int(input())` is the standard pattern for numeric user input

**Easy:** The syntax felt natural coming from other languages. **Hard:** Nothing on day one — but dynamic typing will bite later if you're not careful.

```python
name = "Bilge"
age = 25
print(f"Hello {name}, you are {age} years old.")
user_age = int(input("Enter your age: "))
```

---

### 2026-03-02 — Data Types & String Manipulation

Went through Python's four primitive types, type checking with `type()`, casting, and arithmetic operators. String methods covered: `.upper()`, `.lower()`, `.strip()`, `.replace()`.

**Key takeaways:**
- `//` (floor division) and `%` (modulus) come up constantly in algorithms — worth memorising early
- `type()` is useful for debugging, especially with dynamic typing
- String methods don't modify the original — they return a new string

**Easy:** Arithmetic operators. **Hard:** Remembering that strings are immutable — `.upper()` doesn't change the original, it returns a new one.

```python
print(10 // 3)   # 3  — floor division
print(10 % 3)    # 1  — modulus
print(2 ** 8)    # 256 — exponent

text = "  hello  "
print(text.strip().capitalize())  # "Hello"
```

---

### 2026-03-03 — Control Flow & Operators

`if / elif / else`, comparison and logical operators, nested conditions. Built the Treasure Island text adventure.

**Key takeaways:**
- Indentation isn't just style — it defines the logic structure in Python
- `.lower()` on user input before comparing is essential for robust programs
- Nested conditionals get hard to follow quickly — keep them shallow when possible

**Easy:** The logic itself. **Hard:** Keeping track of which `else` belongs to which `if` when nesting gets deep.

```python
age = 20
if age >= 18 and age < 65:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    print("Minor")
```

**Project:** Treasure Island — text-based adventure, nested conditionals, input normalization with `.lower()`.

---

### 2026-03-04 — Lists & Randomisation

Lists: creation, indexing, negative indexing, slicing, and core methods. The `random` module: `random.choice()`, `random.shuffle()`, `random.randint()`.

**Key takeaways:**
- Negative indexing (`list[-1]`) is a clean way to access the last element without `len()`
- `random.shuffle()` mutates the list in place — it doesn't return a new one
- Lists are mutable, which makes them flexible but also easy to accidentally modify

**Easy:** Indexing and slicing — intuitive. **Hard:** The difference between methods that return a new list vs mutate in place. Took a few mistakes to get that instinct.

```python
import random
choices = ["Rock", "Paper", "Scissors"]
print(choices[-1])        # "Scissors"
cpu = random.choice(choices)
random.shuffle(choices)   # mutates in place, returns None
```

**Project:** Rock Paper Scissors — `random.choice()`, all outcomes covered.

**Bonus:** Extended to Rock Paper Scissors Lizard Spock — 5 choices, 10 win conditions.

---

### 2026-03-05 — Loops

`for` with `range()`, looping over lists and strings, `while`, `break`, `continue`, `pass`, and `enumerate()`.

**Key takeaways:**
- `range(start, stop, step)` — `stop` is exclusive, always
- `enumerate()` eliminates the need for a manual counter — use it by default in `for` loops
- `while True` with a `break` condition is a clean pattern for "run until user quits" flows

**Easy:** `for` loops over lists. **Hard:** Knowing when to use `while` vs `for`. Rule of thumb: if you know the number of iterations, use `for`. If you're waiting for a condition, use `while`.

```python
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

for index, char in enumerate("Python"):
    print(f"{index}: {char}")
```

**Project:** Password Generator — loops over character sets, `random.shuffle()` for randomization.

---

### 2026-03-06 — Functions

`def`, parameters, return values, default parameter values, keyword arguments.

**Key takeaways:**
- A function should do one thing and do it well — if you can't describe it in one sentence, split it
- Default parameter values make functions flexible without overcomplicating call sites
- `return` exits the function immediately — anything after it in that branch won't run

**Easy:** Basic function syntax. **Hard:** The mental shift from "write code once" to "write reusable functions" — you have to think about the interface before the implementation.

```python
def greet(name="stranger"):
    return f"Hello {name}!"

print(greet())              # Hello stranger!
print(greet(name="Bilge"))  # Hello Bilge!
```

---

### 2026-03-07 — Hangman Project

First multi-concept project. The key technique: build a `['_'] * len(word)` display list, then use `enumerate()` to replace underscores at the correct index when a letter is guessed.

**Key takeaways:**
- `['_'] * n` is a clean way to initialise a list of repeated values
- Tracking state across loop iterations (guessed letters, lives remaining) requires thinking carefully about what lives inside vs outside the loop
- ASCII art in a separate file keeps `main.py` clean — first time thinking about file separation

**Easy:** The core loop logic. **Hard:** The enumeration replacement pattern — took a moment to see why `enumerate()` was the right tool here instead of `index()`.

```python
display = ['_'] * len(chosen_word)
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess
```

**Project:** Hangman — random word selection, lives system, already-guessed tracking, ASCII art stages.

---

### 2026-03-08 — Function Parameters & Caesar Cipher

`*args` and `**kwargs`, positional vs keyword arguments, and how Python handles argument passing internally.

**Key takeaways:**
- `*args` collects extra positional arguments as a tuple; `**kwargs` collects extra keyword arguments as a dict
- These are used everywhere in Python frameworks — understanding them is non-negotiable
- The Caesar Cipher is a good reminder that even simple programs need edge case handling (uppercase, wrapping past `z`)

**Easy:** The concept of `*args`. **Hard:** `**kwargs` — the dict-based nature took a bit to feel natural.

```python
def total(*numbers):
    return sum(numbers)  # numbers is a tuple

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")  # info is a dict
```

**Project:** Caesar Cipher — letter shifting encoder/decoder, handles upper/lowercase, loops until quit.

---

### 2026-03-09 — Dictionaries & Silent Auction

Full dict CRUD, `.keys()`, `.values()`, `.items()`, nested dicts, and the `max(key=...)` pattern.

**Key takeaways:**
- Dictionaries are the most important data structure in Python after lists — they're everywhere
- `max(bids, key=bids.get)` is a pattern worth memorising: find the key with the highest value in one line
- Iterating with `.items()` gives both key and value — always prefer it over `.keys()` when you need both

**Easy:** Basic CRUD operations. **Hard:** Nested dicts — accessing `data["person"]["age"]` feels verbose at first, but it's the standard pattern for structured data.

```python
winner = max(bids, key=bids.get)

# Nested dict access
person = {"name": "Bilge", "scores": {"math": 90, "eng": 85}}
print(person["scores"]["math"])  # 90
```

**Project:** Silent Auction — bids in a dict, winner found with `max(key=bids.get)`.

---

### 2026-03-10 — Functions as Outputs & Calculator

Functions as first-class objects, storing functions in dicts, dynamic function calls, and recursive functions.

**Key takeaways:**
- Functions are objects in Python — they can be stored, passed, and returned like any other value
- Storing operations in a dict and calling them with `operations[op](a, b)` is cleaner than a long `if/elif` chain
- Recursion is elegant but has a depth limit — for most practical cases, iteration is safer

**Easy:** Storing functions in a dict — clicked immediately. **Hard:** Recursion — understanding that each call gets its own stack frame takes time to visualise properly.

```python
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
result = operations[operator](n1, n2)
```

**Project:** Calculator — operations dict, dynamic calls, chained calculations, division-by-zero guard.

---

### 2026-03-11 — Blackjack Project

The most complex project so far. Multiple functions working together: dealing, scoring, dealer logic, outcome checking. The Ace rule (11 or 1) was the trickiest part.

**Key takeaways:**
- Breaking a complex problem into small, single-purpose functions makes it manageable — and testable
- The Ace rule is a good example of state-dependent logic: the same card has different values depending on context
- Returning `0` for Blackjack as a sentinel value is a clean convention for "special case"

**Easy:** The overall game structure — the flow was clear. **Hard:** The Ace handling edge case. If the score exceeds 21 and there's an Ace counted as 11, swap it to 1 — getting that logic right took a few iterations.

```python
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack — sentinel value
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
```

**Project:** Blackjack — dealer logic, dynamic Ace handling, all game outcomes covered.

---

### 2026-03-12 — Scope & Number Guessing Game

Local vs global scope, the `global` keyword, and why avoiding it leads to cleaner code.

**Key takeaways:**
- Functions can read globals but can't reassign them without `global` — and you almost never want `global`
- The right pattern: pass values in as parameters, return them out. No hidden state.
- `UPPER_CASE` constants are a convention for values that shouldn't change — not enforced by Python, but respected by other developers

**Easy:** Understanding the concept of scope. **Hard:** The instinct to reach for `global` when a variable "isn't accessible" — the correct fix is almost always to restructure with parameters and return values.

```python
MAX_LIVES = 10  # constant convention

def next_guess(lives):
    lives -= 1
    return lives  # pass in, return out — no global needed
```

**Project:** Number Guessing Game — difficulty levels, hints, clean scope throughout.

---

### 2026-03-13 — Debugging

The three error types, print debugging, `pdb`, `try/except/finally`, and rubber duck debugging.

**Key takeaways:**
- Syntax errors are the easiest — Python tells you exactly where. Logic errors are the hardest — the program runs fine but produces the wrong answer.
- Print debugging is underrated. Adding `print(f"value at step X: {val}")` at each step isolates bugs faster than staring at the code.
- `try/except` is for expected failures (bad user input, missing files) — not for hiding bugs

**Easy:** Identifying syntax and runtime errors. **Hard:** Logic errors — you have to think about what the program *should* do versus what it *is* doing, and trace the difference.

```python
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
finally:
    print("Done.")
```

**Project:** Debugging Challenge — three buggy functions (FizzBuzz, Celsius converter, average calculator), each identified and fixed.

---

### 2026-04-20 — Higher or Lower Project

A game built around a real-world dataset: 45 Instagram accounts with follower counts. Two accounts are shown, the player guesses which has more followers. Correct = score up and continue; wrong = game over.

**Key takeaways:**
- The "carry forward" pattern: `account_b` becomes the new `account_a` each round instead of picking two fresh accounts. Keeps the game flowing and avoids repetition.
- Multi-file architecture for the first time — `main.py`, `game_data.py`, `art.py` separated by responsibility. Much cleaner than one giant file.
- Pure functions with no side effects: `format_account()` and `check_answer()` only take inputs and return outputs — nothing hidden.

**Easy:** The overall game logic. **Hard:** The duplicate guard — if `account_a` and `account_b` are the same, the round is meaningless. A `while` loop re-picks until they differ.

```python
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Carry forward pattern
account_a = account_b
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)
```

**Project:** Higher or Lower — follower count guessing game, multi-file architecture, score tracking, duplicate guard.

---

*Last updated: 2026-04-27*