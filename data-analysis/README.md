# Data Analysis

This folder contains Jupyter notebooks and datasets from Phase 2 of the AI Learning Lab — the ML Foundations stage. The focus is on data manipulation, transformation, and analysis using pandas.

---

## Structure

```
data-analysis/
├── pandas/
│   ├── data_manipulation.ipynb   ✅ Complete
│   ├── Untitled.ipynb            🔄 In Progress  (Joining Data with Pandas)
│   └── datasets/
├── numpy/                        ⏳ Upcoming
└── visualisation/                ⏳ Upcoming
```

---

## Pandas

### data_manipulation.ipynb ✅

**Topic 1 — Transforming DataFrames**
- Introducing DataFrames — structure, attributes (`.columns`, `.index`, `.shape`)
- Sorting rows — `sort_values()`, multiple columns, ascending/descending
- Subsetting columns — single and multiple column selection
- Subsetting rows — boolean indexing, filtering by text, dates, and multiple conditions
- `.isin()` for filtering on multiple values
- Adding new columns — deriving from existing columns (e.g. height in metres, BMI calculation)

**Topic 2 — Aggregating DataFrames**
- Summary statistics — `sum()`, `mean()`, `min()`, `max()`, `count()`, `nunique()`
- `.agg()` — applying multiple functions at once
- Removing duplicates — `drop_duplicates()`, `subset`, `keep` parameter
- Counting values — `value_counts()`, `normalize=True`, `sort_index()`
- Grouped summaries — `groupby()` with single and multiple columns
- `pivot_table()` — `values`, `index`, `columns`, `aggfunc`, `fill_value`, `margins`

**Topic 3 — Slicing and Indexing DataFrames**
- Setting and removing indexes — `set_index()`, `reset_index()`, `drop=True`
- Multi-level (hierarchical) indexes
- Subsetting with `.loc[]` — by label, by list, by tuple for inner levels
- Subsetting with `.iloc[]` — by row and column number
- Slicing rows and columns simultaneously
- Slicing by date ranges and partial dates
- Sorting indexes — `sort_index()`, `level` and `ascending` arguments
- Working with pivot tables — `.loc[]` + slicing, `axis="index"` vs `axis="columns"`

**Topic 4 — Creating and Visualizing DataFrames**
- Histograms — `.hist()`, `bins` argument
- Bar plots — `groupby` + `.plot(kind="bar")`
- Line plots — `.plot(kind="line")`, `rot` for axis label rotation
- Scatter plots — `.plot(kind="scatter")`
- Layering multiple plots, `alpha` for transparency
- Missing values — `isna()`, `.any()`, `.sum()`, visualising with bar plot
- Removing missing values — `dropna()`
- Filling missing values — `fillna()`
- Creating DataFrames from scratch — list of dictionaries (row by row), dictionary of lists (column by column)
- Reading and writing CSV files — `pd.read_csv()`, `.to_csv()`

---

### Untitled.ipynb 🔄 *(Joining Data with Pandas — in progress)*

**Topic 1 — Data Merging Basics** *(started)*
- Inner join with `merge()` — matching rows on a shared column
- Chicago wards and census data merge example

Topics still to cover: left/right/outer joins, merging on multiple keys, `concat()`, ordered merges, `merge_asof()`

---

## Datasets

| File | Used In | Description |
| --- | --- | --- |
| `new_dogs.csv` | `data_manipulation.ipynb` | Dog records — base dataset |
| `new_dogs_with_bmi.csv` | `data_manipulation.ipynb` | Same dataset after adding a computed BMI column |
| `orders.csv` | `data_manipulation.ipynb` | Sample orders data used for aggregation exercises |
| `Ward_Census.csv` | `Untitled.ipynb` | Chicago ward census data — population by ward (2000 & 2010) |
| `Ward_Offices.csv` | `Untitled.ipynb` | Chicago ward government office data — used in merge exercises |

---

## Status

| Topic | Status |
| --- | --- |
| Data Manipulation with Pandas | ✅ Complete |
| Joining Data with Pandas | 🔄 In Progress |
| NumPy | ⏳ Upcoming |
| Visualisation | ⏳ Upcoming |

---

## Notes

These notebooks are personal study notes — they contain code examples, explanations, and exercises worked through during learning. They reflect the learning process, not polished final projects.
