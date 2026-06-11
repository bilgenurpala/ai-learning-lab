[![Data Science & Analysis](../assets/data_analysis_banner.png)](../README.md)

# Data Science & Analysis

> This space tracks my Phase 2 journey focusing on ML foundations: manipulating, clean-structuring, joining, and analyzing data using NumPy, Pandas, and Matplotlib/Seaborn.

[![Library](https://img.shields.io/badge/Stack-Pandas--NumPy--Matplotlib-blue?logo=pandas&logoColor=white&style=flat-square)](../README.md)
[![Status](https://img.shields.io/badge/Status-In_Progress-orange?style=flat-square)](../README.md)

---

## 📂 What's in this folder

| File / Subfolder | Type / Access Badge | Description | Status |
| :--- | :--- | :--- | :--- |
| `pandas/data_manipulation.ipynb` | [![Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue?logo=jupyter&style=flat-square)](pandas/data_manipulation.ipynb) | Sorting, slicing, boolean filtering, group aggregation, and pivot table modeling. | ✅ Complete |
| `pandas/joining_data.ipynb` | [![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&style=flat-square)](pandas/joining_data.ipynb) | Inner/Left/Right/Outer merging, index-based concatenation, and ordered/asof joins. | ✅ Complete |
| `pandas/new_dogs.csv` | [![Raw Dataset](https://img.shields.io/badge/CSV-Raw-lightgrey?logo=pandas&style=flat-square)](pandas/new_dogs.csv) | Baseline dog records used in pandas manipulation exercises. | — |
| `pandas/new_dogs_with_bmi.csv` | [![Raw Dataset](https://img.shields.io/badge/CSV-Raw-lightgrey?logo=pandas&style=flat-square)](pandas/new_dogs_with_bmi.csv) | Derived dataset containing programmatically calculated BMI vectors. | — |
| `pandas/orders.csv` | [![Raw Dataset](https://img.shields.io/badge/CSV-Raw-lightgrey?logo=pandas&style=flat-square)](pandas/orders.csv) | Sample order list used for multi-variable groupby aggregations. | — |
| `pandas/Ward_Census.csv` | [![Raw Dataset](https://img.shields.io/badge/CSV-Raw-lightgrey?logo=pandas&style=flat-square)](pandas/Ward_Census.csv) | Chicago census data (population metrics by ward). | — |
| `pandas/Ward_Offices.csv` | [![Raw Dataset](https://img.shields.io/badge/CSV-Raw-lightgrey?logo=pandas&style=flat-square)](pandas/Ward_Offices.csv) | Chicago ward office details used for complex merging practice. | — |

---

## 🧮 Theoretical & Mathematical Foundations

Data preparation and preprocessing are critical. Here are the core mathematical concepts and formulas implemented in this module.

### 1. Interquartile Range (IQR) for Outlier Detection
We use the IQR to establish bounds outside of which data points are flagged as anomalies.
*   **IQR Calculation:**
    $$IQR = Q_3 - Q_1$$
    Where $Q_1$ is the $25^{\text{th}}$ percentile (first quartile) and $Q_3$ is the $75^{\text{th}}$ percentile (third quartile).
*   **Outlier Threshold Fences:**
    $$\text{Lower Fence} = Q_1 - 1.5 \times IQR$$
    $$\text{Upper Fence} = Q_3 + 1.5 \times IQR$$
    Any data point $x_i < \text{Lower Fence}$ or $x_i > \text{Upper Fence}$ is treated as an outlier.

---

### 2. Pearson Correlation Coefficient ($r$)
Measures the linear correlation between two variables $X$ and $Y$, outputting values in the interval $[-1, 1]$.
$$r_{xy} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 \sum_{i=1}^n (y_i - \bar{y})^2}}$$
Where $\bar{x}$ and $\bar{y}$ are the sample means of $X$ and $Y$ respectively.

---

### 3. Data Rescaling & Standardization
To prevent features with larger scales from dominating optimization steps during model training, we apply mathematical scaling techniques.

*   **Z-score Standardization:**
    Transforms data to have a mean of 0 ($\mu = 0$) and standard deviation of 1 ($\sigma = 1$):
    $$z = \frac{x - \mu}{\sigma}$$
*   **Min-Max Scaling:**
    Binds feature values strictly within the range $[0, 1]$:
    $$x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}$$

---

### 4. Relational Database Joins (Set Mappings)
Given two datasets $R$ and $S$ containing common key elements $k$:

*   **Inner Join ($R \bowtie S$):** Returns records that have matching values in both tables:
    $$R \bowtie S = \{ (r, s) \in R \times S \mid r.k = s.k \}$$
*   **Left Outer Join ($R \rtimes S$):** Returns all records from the left table $R$, and the matched records from the right table $S$:
    $$R \rtimes S = (R \bowtie S) \cup \{ (r, \text{null}) \mid r \in R, \, \forall s \in S : r.k \neq s.k \}$$
*   **Full Outer Join ($R \cup_{\text{join}} S$):** Retains all records from both tables, populating null values for missing keys.

---

## 🎯 Navigation

`[← Python Fundamentals](../python/) | [Next: Machine Learning →](../machine-learning/)`
