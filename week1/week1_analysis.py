"""
Week 1 Task - Data Acquisition, Cleaning and Exploratory Analysis
Name: Hiya Saini
Enrollment No.: A2305224345

Dataset: Breast Cancer Wisconsin (Diagnostic)
Source: UCI Machine Learning Repository
DOI: https://doi.org/10.24432/C5DW2B
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# -------------------------
# Data acquisition
# -------------------------
# UCI provides the official dataset and an API-style Python import through
# ucimlrepo (dataset id 17). The sklearn loader below is used as a
# reproducible local representation of the same public WDBC dataset.
#
# Alternative direct UCI acquisition:
# from ucimlrepo import fetch_ucirepo
# breast_cancer = fetch_ucirepo(id=17)
# X = breast_cancer.data.features
# y = breast_cancer.data.targets

data = load_breast_cancer(as_frame=True)
df = data.frame.copy()
df["diagnosis"] = df["target"].map({0: "malignant", 1: "benign"})
df.drop(columns=["target"], inplace=True)

print("Initial shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())

# -------------------------
# Controlled cleaning demo
# -------------------------
# For this Week 1 simulation, a working copy can be used to demonstrate
# missing-value and duplicate handling without changing the source data.
working = df.copy()

rng = np.random.default_rng(42)
for col, n in [("mean radius", 6), ("mean texture", 6), ("mean area", 5)]:
    idx = rng.choice(working.index, size=n, replace=False)
    working.loc[idx, col] = np.nan

working = pd.concat([working, working.iloc[rng.choice(working.index, 5)]],
                    ignore_index=True)

print("Missing values before cleaning:")
print(working.isna().sum())
print("Duplicates before cleaning:", working.duplicated().sum())

# Remove duplicates.
working = working.drop_duplicates().reset_index(drop=True)

# Median imputation for numerical missing values.
numeric_cols = working.select_dtypes(include=np.number).columns
for col in numeric_cols:
    if working[col].isna().any():
        working[col] = working[col].fillna(working[col].median())

working["diagnosis"] = working["diagnosis"].astype("category")

print("Missing values after cleaning:")
print(working.isna().sum())
print("Duplicates after cleaning:", working.duplicated().sum())

# -------------------------
# EDA
# -------------------------
print(working.describe())
print(working["diagnosis"].value_counts())

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(working["mean radius"], bins=25)
plt.title("Distribution of Mean Radius")
plt.xlabel("Mean Radius")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
for label in ["benign", "malignant"]:
    sub = working[working["diagnosis"] == label]
    plt.scatter(sub["mean radius"], sub["mean perimeter"],
                alpha=0.55, label=label)
plt.xlabel("Mean Radius")
plt.ylabel("Mean Perimeter")
plt.title("Mean Radius vs Mean Perimeter")
plt.legend()
plt.show()

# Correlation
corr = working.select_dtypes(include=np.number).corr()
print(corr["mean radius"].sort_values(ascending=False).head(10))
