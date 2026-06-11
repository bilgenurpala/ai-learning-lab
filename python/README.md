[![Python Fundamentals](../assets/python_banner.png)](../README.md)

# Python Fundamentals

> This space documents my Phase 1 journey, laying a robust algorithmic and programming foundation in Python. It includes structural exercises, data collections, OOP patterns, and intermediate functional programming.

[![Language](https://img.shields.io/badge/Language-Python_3.10+-blue?logo=python&logoColor=white&style=flat-square)](https://www.python.org)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)](../README.md)

---

## 📂 What's in this folder

| File | Type / Access Badge | Description | Status |
| :--- | :--- | :--- | :--- |
| `python_basics.ipynb` | [![Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue?logo=jupyter&style=flat-square)](python_basics.ipynb) | Variables, control flow, loops, collections, scope, and basic modules. | ✅ Complete |
| `python_intermediate.ipynb` | [![Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue?logo=jupyter&style=flat-square)](python_intermediate.ipynb) | Python ecosystem, parameter passing (`*args`, `**kwargs`), and lambdas. | ✅ Complete |
| `sales.csv` | [![Raw Dataset](https://img.shields.io/badge/CSV-Raw-lightgrey?logo=pandas&style=flat-square)](sales.csv) | Sample orders dataset generated programmatically for pandas practice. | — |

---

## 🧮 Theoretical & Mathematical Foundations

To build scalable AI and data pipelines, we must master Python's functional paradigms and algorithmic efficiencies.

### 1. Functional Paradigms & Mapping
Functional programming treats computation as the evaluation of mathematical functions, avoiding state changes and mutable data.

*   **Lambda Abstraction ($\lambda$-Calculus):** 
    An anonymous, inline function mapping an input variable $x$ to an expression $f(x)$. Mathematically represented as:
    $$\lambda x. f(x)$$
    In Python: `lambda x: f(x)`

*   **Element-wise Mapping:**
    Given a function $f: X \to Y$ and a sequence $X = [x_1, x_2, \dots, x_n]$, the mapping operator applies $f$ to each element:
    $$\text{map}(f, X) = [f(x_1), f(x_2), \dots, f(x_n)]$$

*   **Predicate Filtering:**
    Given a predicate function $p: X \to \{\text{True}, \text{False}\}$, the filter operator retains only elements matching the predicate:
    $$\text{filter}(p, X) = [x \mid x \in X \text{ and } p(x) \text{ is True}]$$

---

### 2. Algorithmic Complexity ($O$ Notation)
We evaluate the performance of algorithms using Big-O notation, representing the upper bound of execution time or memory footprint relative to the input size $n$.

*   **Constant Time $O(1)$:** Index lookup in a list or key-value retrieval in a hash map (dictionary).
*   **Logarithmic Time $O(\log n)$:** Binary search tree lookups.
*   **Linear Time $O(n)$:** Iterating through a collection of size $n$ via `for` loops.
*   **Quadratic Time $O(n^2)$:** Nested loops (e.g., sorting algorithms like bubble sort).

---

## 📔 Notebook Core Focus

### `python_basics.ipynb`
Built a solid procedural and OOP Python foundation topic by topic. Each concept is reinforced with a practical mini-project or exercise.
- **Variables & Data Types:** Type inference, casting, and primitive operations.
- **Control Flow & Collections:** List indexing, indexing slices, and conditional nesting (`if/elif/else`).
- **Control Loops:** `for`, `while`, and index-tracking iteration using `enumerate()`.
- **Scope Resolution:** Understanding the LEGB rule (Local, Enclosing, Global, Built-in) to prevent scope pollution.
- **Projects Built:** Hangman · Blackjack · Caesar Cipher · Calculator · Password Generator · Silent Auction · Higher or Lower

---

### `python_intermediate.ipynb`
Covers advanced structures, packages, robust error handling, and parameter unpacking.
- **Chapter 1 — The Python Ecosystem:** Operating system tools (`os`), standard math and string libraries, and standard package management (`pip`).
- **Chapter 2 — Argument Unpacking:** Passing a variable number of positional arguments via `*args` (tuple unpacking) and keyword arguments via `**kwargs` (dictionary unpacking).
- **Chapter 3 — Lambdas & Exception Guards:** Using `try/except/finally` structures to construct fail-safe runtime pathways, and raising custom errors using `raise`.

---

## 🎯 Navigation

`[← Main Hub](../README.md) | [Next: Data Analysis →](../data-analysis/)`
