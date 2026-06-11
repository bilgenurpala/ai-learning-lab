# Devlog — AI Learning Lab

A day-by-day record of what I learned, built, and figured out.

---

## Phase 2 — ML & Data Science

---

### 20260611 — DataCamp Courses Completed & Documentation Refactored
**Status:** ✅ Done

**What I did:**
- Completed the remaining advanced topics of **Joining Data with pandas** in [joining_data.ipynb](file:///c:/Programming/Ai%20-%20Engineer/ai-learning-lab/data-analysis/pandas/joining_data.ipynb) (semi/anti-joins, concatenations, validation parameters, ordered/asof merges, and wide-to-long melting).
- Developed 3 highly detailed, interactive Jupyter Notebooks documenting course notes and executable code scripts:
  - [working_with_openai_api.ipynb](file:///c:/Programming/Ai%20-%20Engineer/ai-learning-lab/ai-engineering/llm-apis/working_with_openai_api.ipynb) (Completions API, custom parameter tuning, token counting with `tiktoken`, JSON mode, and Moderation safety checking).
  - [embeddings_openai_api.ipynb](file:///c:/Programming/Ai%20-%20Engineer/ai-learning-lab/ai-engineering/rag/embeddings_openai_api.ipynb) (Vector embedding dimensions pruning, Cosine/Euclidean similarity searches, 2D scatter plotting of t-SNE/PCA projections using Matplotlib, Logistic Regression text classification, and K-Means clustering).
  - [intro_to_data_security.ipynb](file:///c:/Programming/Ai%20-%20Engineer/ai-learning-lab/cybersecurity/datacamp-notes/intro_to_data_security.ipynb) (CIA Triad, GDPR/HIPAA/CCPA compliances, symmetric/asymmetric cryptosystems, password salting/hashing, dynamic data masking, SQLi parameterized query prevention, and SIEM incident monitoring).
- Completed the complete refactoring of the repository documentation (Root and all subfolders) adding clickable tech banners, flat-square shields.io progress badges, detailed LaTeX equations, and vector SVG flowcharts.
- Cleaned up calendar dates and replaced the `fintrack` project references with a placeholder for the upcoming **FlyRank Analytics Platform** corporate integration.

**What I learned:**
- Pre-calculating tokens using `tiktoken` allows for precise API budgeting prior to calling LLM endpoints.
- Dimensionality pruning via the OpenAI `dimensions` parameter preserves semantic similarities while significantly optimizing storage size and search lookup speeds.
- Adding cryptographically secure random salts prevents password cracking from standard dictionary or rainbow table attacks.
- Parameterized database statements ensure user input is parsed strictly as parameters, neutralizing SQL Injection vulnerability vectors.

**What's next:**
- Move forward to the classical Machine Learning modules (Scikit-learn) and NumPy foundations.

---

### 20260505 — Intermediate Python | DataCamp Progress
**Status:** 🔄 In Progress

**What I did:**
- Working through DataCamp Intermediate Python — list comprehensions, lambda functions, NumPy introduction
- Continued Codedex Python challenges — list and dict exercises
- Reviewed Phase 1 Python basics to ensure solid foundation before moving into data science stack

**What I learned:**
- List comprehensions are significantly more Pythonic than equivalent for loops — `[x*2 for x in lst if x > 0]` vs 4 lines of code
- Lambda functions are anonymous, single-expression functions — useful for passing simple operations as arguments
- The `_` convention in `for _ in range(n)` signals that the loop variable is intentionally unused

**What I struggled with:**
- Catching typos like `==` instead of `=` in assignments — need to slow down when writing quickly
- Breaking the habit of always using `for i in range(len(lst))` instead of direct iteration

**What's next:**
- Finish Intermediate Python on DataCamp
- Start Data Manipulation with pandas tomorrow

---

### 20260504 — Introduction to Python Complete | Bootcamp ML-1
**Status:** ✅ Done

**What I did:**
- Completed DataCamp **Introduction to Python** — 100%
- Completed Codedex Python track — all introductory modules finished
- Attended Pupilica Bootcamp session: **Machine Learning Models — 1** (18:00–21:00)
- Bootcamp covered: data preprocessing for ML, Label Encoding, One-Hot Encoding, StandardScaler, MinMaxScaler, train/test split

**What I learned:**
- DataCamp's exercise format forces you to write code, not just watch — much more effective for retention
- `train_test_split()` must always happen before fitting any scaler — fitting on the full dataset causes data leakage, which silently inflates model performance
- Label Encoding assigns integers to categories — fine for tree-based models, but creates false ordering for linear models. One-Hot Encoding is safer by default.

**What I struggled with:**
- The bootcamp moved fast on preprocessing concepts — noted everything down, will revisit with the instructor's notebook this week
- Understanding *why* data leakage is a problem took a concrete example to click: if you scale using the test set's statistics, you've already "seen" the test data

**What's next:**
- Intermediate Python on DataCamp
- Revisit bootcamp notebook on preprocessing

---

### 20260427 — Phase 2 Start | Program Reset & New Direction
**Status:** ✅ Done

Phase 1 is done. 13 days, 14 projects, Python fundamentals covered. Today I'm resetting the structure and committing to a serious push toward AI engineering.

The goal is clear: by September 1, 2026, I want to be job-ready as a junior AI engineer — not just someone who finished a few courses, but someone with real deployed projects, a strong GitHub, and hands-on experience.

**What's lined up:**
- Pupilica AI Bootcamp — 42 hours of live instruction, April 28 – May 22, 2026 (Mon/Wed/Fri + Sat)
- Microsoft Turkey AI Innovators internship — project starting ~late June 2026
- Self-study: ~30 hours/week across all phases

**The full path:**
- Phase 2: Python advanced + full ML stack, running alongside the bootcamp
- Phase 3: Deep learning, NLP, Transformers, LLMs, RAG
- Phase 4: MLOps, deployment, portfolio polish

**Repository structure from here:**
- `ai-learning-lab` — this repo, central hub, detailed devlog
- [`pupilica-ai-bootcamp`](https://github.com/bilgenurpala/pupilica-ai-bootcamp) — bootcamp notes, exercises, assignments
- `flyrank-project` — Future project for the FlyRank institution *(repo coming soon)*
- `microsoft-ai-project` — Context-Aware AI Agent *(repo coming soon)*

The approach stays the same: documentation and code over videos, build things rather than just watch them, commit every day.

---

## Upcoming — 5–14 May 2026 Plan

> This section tracks the detailed plan for the next 10 days. Each day will be marked ✅ when complete.

---

### 20260505 — Intermediate Python | Codedex Python Challenges
- [ ] DataCamp: Intermediate Python — finish
- [ ] Codedex: Python challenges — list, dict, loop
- [ ] ⚠️ No bootcamp today

---

### 20260506 — Data Manipulation with pandas | Bootcamp ML-2
- [ ] DataCamp: Data Manipulation with pandas — start and finish
- [ ] Codedex: Pandas section — start
- [ ] ⚠️ Pupilica Bootcamp: Machine Learning — 2 (18:00–21:00)

---

### 20260507 — Pandas Deep Dive | Instructor Notebook EDA 1–2
- [ ] DataCamp: Data Manipulation with pandas — finish (if not done)
- [ ] Codedex: Pandas section — continue
- [ ] Instructor notebook: Veri Setini Tanıma — rewrite from scratch in Jupyter
- [ ] Instructor notebook: Eksik Veri — rewrite from scratch in Jupyter

---

### 20260508 — Cleaning Data | Bootcamp ML-3 | Midterm Assignment
- [ ] DataCamp: Cleaning Data in Python — start and finish
- [ ] Codedex: Pandas section — finish
- [ ] Instructor notebook: Veri Tipleri + Tutarsız Kayıtlar + Aykırı Değerler — rewrite from scratch
- [ ] Self-study: Midterm assignment (personal practice, no submission required)
- [ ] ⚠️ Pupilica Bootcamp: Machine Learning — 3 (18:00–21:00)

---

### 20260509 — Cleaning Data Finish | Instructor Notebook EDA 3–5
- [ ] DataCamp: Cleaning Data in Python — finish (if not done)
- [ ] Instructor notebook: Veri Tipleri + Tutarsız Kayıtlar + Aykırı Değerler — complete
- [ ] GitHub: commit all work from the week so far

---

### 20260510 — Supervised Learning | Codedex ML Section
- [ ] DataCamp: Supervised Learning with scikit-learn — start
- [ ] Codedex: Machine Learning section — start
- [ ] Instructor notebook: YZA_ML — Decision Trees + Cross Validation — rewrite from scratch
- [ ] Kaggle: browse Titanic starter notebook

---

### 20260511 — Supervised Learning | ⭐ Microsoft Meeting 16:00–17:00
- [ ] DataCamp: Supervised Learning with scikit-learn — continue
- [ ] Instructor notebook: YZA_ML — Cross Validation — complete
- [ ] ⭐ Microsoft Turkey AI Innovators meeting (16:00–17:00)
- [ ] Prepare: be ready to explain the Context-Aware AI Agent project in 2 minutes

> **For the Microsoft meeting:** Answer these 3 questions clearly:
> 1. What is the project? — A context-aware AI agent that stores user goals, notes, and tasks; retrieves relevant history using RAG; and uses an LLM to select and call tools autonomously.
> 2. Why this project? — It demonstrates end-to-end AI engineering: memory, retrieval, tool use, and LLM orchestration in one system.
> 3. How will you build it? — LangChain + ChromaDB for RAG, Claude API for the LLM, custom tool definitions, 4-week build starting late June.

---

### 20260512 — Supervised Learning Finish | Bootcamp ML-4
- [ ] DataCamp: Supervised Learning with scikit-learn — finish
- [ ] Codedex: Machine Learning section — continue
- [ ] Instructor notebook: YZA_ML — K-Means + Hierarchical Clustering — rewrite from scratch
- [ ] GitHub: commit
- [ ] ⚠️ Pupilica Bootcamp: Machine Learning — 4 (18:00–21:00)

---

### 20260513 — Unsupervised Learning | Matplotlib Start | Final Assignment
- [ ] DataCamp: Unsupervised Learning in Python — start and finish
- [ ] DataCamp: Introduction to Data Visualization with Matplotlib — start
- [ ] Codedex: Machine Learning + visualisation sections
- [ ] Instructor notebook: YZA_ML — PCA — rewrite from scratch
- [ ] Self-study: Final assignment (personal practice, no submission required)
- [ ] GitHub: commit all work from the week

---

### 20260514 — Deep Learning Intro | Bootcamp DL-1
- [ ] DataCamp: Introduction to Deep Learning in Python — start
- [ ] Review: scan through all ML notes — identify any gaps before DL begins
- [ ] ⚠️ Pupilica Bootcamp: Deep Learning — 1 (18:00–21:00)

---

## Phase 1 — Python Fundamentals

---

### 20260313 — Debugging

The three error types, print debugging, `pdb`, `try/except/finally`, and rubber duck debugging.

**What I learned:**
- Syntax errors are the easiest — Python tells you exactly where. Logic errors are the hardest — the program runs fine but produces the wrong answer.
- Print debugging is underrated. Adding `print(f"value at step X: {val}")` at each step isolates bugs faster than staring at the code.
- `try/except` is for expected failures (bad user input, missing files) — not for hiding bugs.

**What I struggled with:**
- Logic errors — you have to think about what the program *should* do versus what it *is* doing, and trace the difference.

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

### 20260312 — Scope & Number Guessing Game

Local vs global scope, the `global` keyword, and why avoiding it leads to cleaner code.

**What I learned:**
- Functions can read globals but can't reassign them without `global` — and you almost never want `global`.
- The right pattern: pass values in as parameters, return them out. No hidden state.
- `UPPER_CASE` constants are a convention for values that shouldn't change — not enforced by Python, but respected by other developers.

**What I struggled with:**
- The instinct to reach for `global` when a variable "isn't accessible" — the correct fix is almost always to restructure with parameters and return values.

```python
MAX_LIVES = 10  # constant convention

def next_guess(lives):
    lives -= 1
    return lives  # pass in, return out — no global needed
```

**Project:** Number Guessing Game — difficulty levels, hints, clean scope throughout.

---

### 20260311 — Blackjack Project

The most complex project so far. Multiple functions working together: dealing, scoring, dealer logic, outcome checking. The Ace rule (11 or 1) was the trickiest part.

**What I learned:**
- Breaking a complex problem into small, single-purpose functions makes it manageable — and testable.
- The Ace rule is a good example of state-dependent logic: the same card has different values depending on context.
- Returning `0` for Blackjack as a sentinel value is a clean convention for "special case."

**What I struggled with:**
- The Ace handling edge case — if the score exceeds 21 and there's an Ace counted as 11, swap it to 1. Getting that logic right took a few iterations.

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

### 20260310 — Functions as Outputs & Calculator

Functions as first-class objects, storing functions in dicts, dynamic function calls.

**What I learned:**
- Functions are objects in Python — they can be stored, passed, and returned like any other value.
- Storing operations in a dict and calling them with `operations[op](a, b)` is cleaner than a long `if/elif` chain.

**What I struggled with:**
- Recursion — understanding that each call gets its own stack frame takes time to visualise properly.

```python
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
result = operations[operator](n1, n2)
```

**Project:** Calculator — operations dict, dynamic calls, chained calculations, division-by-zero guard.

---

### 20260309 — Dictionaries & Silent Auction

Full dict CRUD, `.keys()`, `.values()`, `.items()`, nested dicts, and the `max(key=...)` pattern.

**What I learned:**
- Dictionaries are the most important data structure in Python after lists.
- `max(bids, key=bids.get)` finds the key with the highest value in one line.
- Iterating with `.items()` gives both key and value — always prefer it over `.keys()` when you need both.

**What I struggled with:**
- Nested dicts — accessing `data["person"]["age"]` feels verbose at first.

```python
winner = max(bids, key=bids.get)
```

**Project:** Silent Auction — bids in a dict, winner found with `max(key=bids.get)`.

---

### 20260308 — Function Parameters & Caesar Cipher

`*args` and `**kwargs`, positional vs keyword arguments.

**What I learned:**
- `*args` collects extra positional arguments as a tuple; `**kwargs` collects extra keyword arguments as a dict.
- These are used everywhere in Python frameworks — understanding them is non-negotiable.

**What I struggled with:**
- `**kwargs` — the dict-based nature took a bit to feel natural.

```python
def total(*numbers):
    return sum(numbers)

def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
```

**Project:** Caesar Cipher — letter shifting encoder/decoder, handles upper/lowercase, loops until quit.

---

### 20260307 — Hangman Project

First multi-concept project combining lists, loops, functions, and randomisation.

**What I learned:**
- `['_'] * n` is a clean way to initialise a list of repeated values.
- Tracking state across loop iterations requires thinking carefully about what lives inside vs outside the loop.
- ASCII art in a separate file keeps `main.py` clean — first time thinking about file separation.

**What I struggled with:**
- The enumeration replacement pattern — took a moment to see why `enumerate()` was the right tool here instead of `index()`.

```python
display = ['_'] * len(chosen_word)
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess
```

**Project:** Hangman — random word selection, lives system, already-guessed tracking, ASCII art stages.

---

### 20260306 — Functions

`def`, parameters, return values, default parameter values, keyword arguments.

**What I learned:**
- A function should do one thing and do it well.
- Default parameter values make functions flexible without overcomplicating call sites.
- `return` exits the function immediately.

**What I struggled with:**
- The mental shift from "write code once" to "write reusable functions" — you have to think about the interface before the implementation.

```python
def greet(name="stranger"):
    return f"Hello {name}!"
```

---

### 20260305 — Loops

`for` with `range()`, looping over lists and strings, `while`, `break`, `continue`, and `enumerate()`.

**What I learned:**
- `range(start, stop, step)` — `stop` is exclusive, always.
- `enumerate()` eliminates the need for a manual counter.
- `while True` with a `break` condition is a clean pattern for "run until user quits" flows.

**What I struggled with:**
- Knowing when to use `while` vs `for`. Rule of thumb: if you know the number of iterations, use `for`. If you're waiting for a condition, use `while`.

```python
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

for index, char in enumerate("Python"):
    print(f"{index}: {char}")
```

**Project:** Password Generator — loops over character sets, `random.shuffle()` for randomisation.

---

### 20260304 — Lists & Randomisation

Lists: creation, indexing, slicing, core methods. The `random` module.

**What I learned:**
- Negative indexing (`list[-1]`) is a clean way to access the last element without `len()`.
- `random.shuffle()` mutates the list in place — it doesn't return a new one.
- Lists are mutable, which makes them flexible but also easy to accidentally modify.

**What I struggled with:**
- The difference between methods that return a new list vs mutate in place.

```python
import random
choices = ["Rock", "Paper", "Scissors"]
cpu = random.choice(choices)
random.shuffle(choices)  # mutates in place, returns None
```

**Project:** Rock Paper Scissors · Rock Paper Scissors Lizard Spock (extended version).

---

### 20260303 — Control Flow & Operators

`if / elif / else`, comparison and logical operators, nested conditions.

**What I learned:**
- Indentation isn't just style — it defines the logic structure in Python.
- `.lower()` on user input before comparing is essential for robust programs.

**What I struggled with:**
- Keeping track of which `else` belongs to which `if` when nesting gets deep.

**Project:** Treasure Island — text-based adventure, nested conditionals, input normalisation.

---

### 20260302 — Data Types & String Manipulation

Python's four primitive types, type checking, casting, string methods.

**What I learned:**
- `//` (floor division) and `%` (modulus) come up constantly in algorithms.
- String methods don't modify the original — they return a new string.

**What I struggled with:**
- Remembering that strings are immutable — `.upper()` doesn't change the original.

```python
print(10 // 3)   # 3
print(10 % 3)    # 1
print(2 ** 8)    # 256
```

---

### 20260301 — Variables

First day. Covered how Python handles variables, dynamic typing, and the `snake_case` convention.

**What I learned:**
- Python infers types at runtime — no declarations needed.
- f-strings are cleaner and more readable than string concatenation.
- `int(input())` is the standard pattern for numeric user input.

**What I struggled with:**
- Nothing on day one — but dynamic typing will bite later if you're not careful.

```python
name = "Bilge"
age = 25
print(f"Hello {name}, you are {age} years old.")
```

---

*Last updated: 2026-05-05*