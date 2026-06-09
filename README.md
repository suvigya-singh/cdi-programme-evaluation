# CDI Programme Evaluation — Python Analysis

## Overview
A Python replication of programme evaluation analysis conducted 
professionally at the Childhood Development Initiative (CDI), Dublin. 
This project mirrors the SPSS-based statistical methodology used in 
professional CDI evaluations, rebuilt entirely in Python.

Built as a portfolio project demonstrating applied data analysis 
skills in a real-world research context.

---

## What This Project Does

- Loads and explores a structured pre/post intervention dataset 
  (50 participants, 13 schools, 5 geographic areas across Ireland)
- Calculates descriptive statistics by treatment and control group
- Computes individual score and parental confidence improvements
- Runs non-parametric statistical tests:
  - Wilcoxon Signed-Rank Test (pre vs post, treatment group)
  - Mann-Whitney U Test (treatment vs control)
  - Spearman Correlation (sessions attended vs improvement)
- Breaks down results by geographic area and gender
- Produces four visualisation charts saved as results.png
- Outputs a full evaluation summary to terminal

---

## Key Findings (Dummy Data)

- Treatment group showed statistically significant improvement (p < 0.05)
- Average score improvement in treatment group: ~28 points
- Average score improvement in control group: ~3 points
- Programme completion rate: 52%
- Post-programme parental confidence: 4.4 / 5

---

## Libraries Used

| Library | Purpose |
|---|---|
| pandas | Data loading and manipulation |
| numpy | Numerical operations |
| matplotlib | Data visualisation |
| scipy | Statistical testing |

---

## How to Run

1. Clone this repository
2. Install dependencies:
pip install pandas numpy matplotlib scipy
3. Run the analysis:
python analysis.py

---

## Project Background

This project was built to demonstrate the application of Python 
to real-world programme evaluation methodology from my professional 
research career at the Childhood Development Initiative, Dublin.

The dataset is a realistic dummy dataset modelled on the structure 
of CDI programme evaluations. No real participant data is used.

---

## Author

**Suvigya Singh**  
MSc Applied Research — Trinity College Dublin (First Class Honours)  
BCom — Delhi University (First Class, 82%)  
Dublin, Ireland
