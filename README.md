# AI Learning Lab

> A structured, day-by-day learning journey from Python fundamentals to Machine Learning and AI engineering — documented with code, projects, and a detailed devlog.

![Progress](https://img.shields.io/badge/Python_Basics-Day%2013%20of%20100-orange)
![Phase](https://img.shields.io/badge/Phase-1%20Python%20Fundamentals-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-blue?logo=visualstudiocode)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)

---

## About This Repository

This repository documents a structured learning path from beginner Python to applied AI engineering. Each phase builds on the previous one, combining theory, hands-on exercises, and real projects. Progress is tracked daily in the [devlog](docs/devlog.md).

The full path:

1. **Python Fundamentals** — syntax, data structures, OOP, algorithms in Python
2. **DSA** — classic data structures and algorithm patterns
3. **Math Foundations** — linear algebra and probability
4. **Data Analysis** — NumPy and Pandas
5. **Machine Learning** — supervised/unsupervised learning, model evaluation
6. **AI & LLM Applications** — building production-grade AI systems with LLMs

---

## Repository Structure

```
ai-learning-lab/
│
├── python/
│   ├── basics/                          # Phase 1 — Python Fundamentals (Day 1–100)
│   │   ├── day01_variables.py
│   │   ├── day02_data_types.py
│   │   ├── day03_control_flow_operators.py
│   │   ├── day04_lists.py
│   │   ├── day05_loops.py
│   │   ├── day06_functions.py
│   │   ├── day07_hangman/
│   │   ├── day08_function_parametres.py
│   │   ├── day09_dictionaries.py
│   │   ├── day10_functions_outputs.py
│   │   ├── day11_the_blackjack_project/
│   │   ├── day12_scope_and_numberGuessing_project/
│   │   ├── day13_debugging.py
│   │   └── lizard_spock.py              # Bonus — Extended RPS project
│   ├── intermediate/                    # Coming soon
│   └── advanced/                        # Coming soon
│
├── dsa/                                 # Phase 2 — Data Structures & Algorithms
├── math/                                # Phase 2 — Linear Algebra & Probability
├── data-analysis/                       # Phase 2 — NumPy & Pandas
├── machine-learning/                    # Phase 3 — Machine Learning
├── ai-applications/                     # Phase 4 — AI & LLM Applications
│
└── docs/
    └── devlog.md                        # Day-by-day learning log (EN + TR)
```

---

## Roadmap

| Phase | Track | Topics | Status |
|---|---|---|---|
| 1 | Python Fundamentals | Variables, data types, control flow, functions, OOP, modules | In Progress |
| 2 | Data Structures & Algorithms | Arrays, linked lists, trees, graphs, sorting, searching | Upcoming |
| 2 | Linear Algebra | Vectors, matrices, transformations, eigenvalues | Upcoming |
| 2 | Probability & Statistics | Distributions, Bayes, hypothesis testing | Upcoming |
| 2 | NumPy & Pandas | Array ops, DataFrames, data wrangling, EDA | Upcoming |
| 3 | Machine Learning | Regression, classification, clustering, model evaluation | Upcoming |
| 4 | AI & LLM Applications | Prompt engineering, RAG, agents, fine-tuning | Upcoming |

---

## Python Fundamentals — Progress Log

### Day 1 — Variables

- `print()` and basic output
- Variables and dynamic typing
- `snake_case` naming convention
- Data types: `str`, `int`
- f-strings and `input()` with type casting

```python
name = "Bilge"
age = 25
print(f"Hello {name}, you are {age} years old.")
user_age = int(input("Enter your age: "))
```

---

### Day 2 — Data Types & String Manipulation

- Primitive types: `int`, `float`, `str`, `bool`
- `type()` and type casting
- Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- String methods and manipulation

```python
print(type(3.14))   # <class 'float'>
print(10 // 3)      # 3  — floor division
print(2 ** 8)       # 256 — exponent
```

---

### Day 3 — Control Flow & Operators

- `if`, `elif`, `else`
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical operators: `and`, `or`, `not`
- Nested conditions

**Project: Treasure Island** — text-based adventure game built with nested conditionals.

---

### Day 4 — Lists & Randomisation

- List creation, indexing, negative indexing, slicing
- `append()`, `remove()`, `len()`
- `for` loop over lists
- `random.choice()`, `random.shuffle()`

**Project: Rock Paper Scissors** — computer picks randomly, all win/lose/draw outcomes handled.

---

### Day 5 — Loops

- `for` with `range(start, stop, step)`
- `while` loop
- `break`, `continue`, `pass`
- `enumerate()` for index + value

**Project: Password Generator** — random characters from letter/symbol/number sets, shuffled for security.

---

### Day 6 — Functions

- `def`, parameters, arguments
- `return` statement
- Default parameter values
- Keyword arguments

```python
def greet(name="stranger"):
    return f"Hello {name}!"
```

---

### Day 7 — Hangman Project

- Combining loops, lists, functions, and randomisation
- Dynamic list generation: `['_'] * len(word)`
- `enumerate()` for index-based replacement
- Game state tracking across loop iterations

**Project: Hangman** — fully functional word-guessing game with lives, letter tracking, and ASCII art.

---

### Day 8 — Function Parameters & Caesar Cipher

- Positional vs keyword arguments
- Default values
- `*args` — unlimited positional arguments
- `**kwargs` — unlimited keyword arguments

**Project: Caesar Cipher** — encoder/decoder with letter shifting, runs in a loop until quit.

---

### Day 9 — Dictionaries & Silent Auction

- Dictionary CRUD: create, access, update, delete
- `.keys()`, `.values()`, `.items()`
- Looping through dictionaries
- Nested dictionaries
- `max()` with `key=dict.get`

**Project: Silent Auction** — multiple bidders stored in a dict, winner found with `max()`.

---

### Day 10 — Functions as Outputs & Calculator

- Functions as first-class objects
- Storing functions in dictionaries
- Dynamic function calls
- Recursive functions

**Project: Calculator** — operations stored in a dict, chained calculations, division-by-zero guard.

---

### Day 11 — Blackjack Project

- Multi-function architecture
- Game state management across iterations
- Edge case handling: Blackjack, Bust, Ace (11 or 1)

**Project: Blackjack** — full card game with dealer logic, dynamic Ace handling, all win/lose/draw/bust scenarios.

---

### Day 12 — Scope & Number Guessing Game

- Local vs global scope
- `global` keyword
- `UPPER_CASE` constants convention
- Pure functions with no global state

**Project: Number Guessing Game** — difficulty levels (easy/hard), hints, clean scope throughout.

---

### Day 13 — Debugging

- 3 error types: Syntax, Runtime, Logic
- Print debugging
- Python debugger (`pdb`)
- `try` / `except` error handling
- Rubber duck debugging

**Project: Debugging Challenge** — three buggy functions covering all three error types, each identified and fixed.

---

### Bonus — Rock Paper Scissors Lizard Spock

Extension of the Day 4 RPS project. Two new choices added (Lizard, Spock), 10 win conditions handled with nested conditionals and emoji input.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-coming_soon-lightgrey?logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-coming_soon-lightgrey?logo=pandas)
![scikit-learn](https://img.shields.io/badge/scikit--learn-coming_soon-lightgrey?logo=scikit-learn)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-blue?logo=visualstudiocode)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)

---

## Goals

- Build a strong Python foundation with clean, readable code
- Develop algorithmic thinking through DSA practice
- Understand the math behind machine learning (linear algebra, probability)
- Apply data analysis skills with NumPy and Pandas
- Build and ship real Machine Learning and AI/LLM projects
- Document every step publicly for accountability and portfolio

---

> *"An investment in knowledge pays the best interest."* — Benjamin Franklin
