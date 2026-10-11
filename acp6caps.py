# M15 Lesson 6 – Capstone Project: Penguin Dataset Analysis

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from google.colab import files

# Suppress warnings for clean output
import warnings

warnings.filterwarnings("ignore")

# ---------------------------------
# Upload and Load the Dataset
# ---------------------------------
# Upload your penguins.csv file using the prompt below
uploaded = files.upload()

# Read the CSV file (update filename if needed)
df = pd.read_csv("penguins.csv")

# ---------------------------------
# Task 1 & 2: Check and Visualize Null Values
# ---------------------------------
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

print("\n--- Visualizing Missing Values ---")
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap in Penguins Dataset")
plt.xlabel("Columns")
plt.ylabel("Records")
plt.show()

# ---------------------------------
# Task 3: Handle Numerical & Categorical Null Values
# ---------------------------------
# Handle categorical columns by filling with the mode (most common value)
categorical_columns = ["species", "island", "sex"]
for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])

# Handle numerical columns using interpolation and filling remaining gaps
numerical_columns = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]
existing_num_cols = [col for col in numerical_columns if col in df.columns]

if existing_num_cols:
    df[existing_num_cols] = df[existing_num_cols].interpolate()
    df[existing_num_cols] = df[existing_num_cols].bfill().ffill()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# ---------------------------------
# Task 4: Pair Plot for Numerical Features
# ---------------------------------
print("\n--- Generating Pair Plot ---")
sns.pairplot(df, hue="species" if "species" in df.columns else None)
plt.show()

# ---------------------------------
# Task 5: Correlation Heatmap
# ---------------------------------
print("\n--- Generating Correlation Heatmap ---")
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

# ---------------------------------
# Task 6: Box Plot for Numerical Features
# ---------------------------------
print("\n--- Generating Box Plots ---")
if existing_num_cols:
    df[existing_num_cols].plot(
        kind="box", subplots=True, layout=(2, 2), figsize=(10, 8)
    )
    plt.suptitle("Box Plots for Numerical Features", fontsize=14)
    plt.show()

# ---------------------------------
# Task 7: Count Plot for Gender (Sex)
# ---------------------------------
print("\n--- Generating Count Plot for Gender ---")
if "sex" in df.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="sex", palette="Set2")
    plt.title("Count Plot of Penguin Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()