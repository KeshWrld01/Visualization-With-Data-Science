# Visualization to Check Relation between Variables

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Seaborn's built-in Penguins dataset
# (Alternatively, you can upload and read your downloaded CSV file:
#  df = pd.read_csv('penguins.csv'))
df = sns.load_dataset("penguins")

# Display the first few rows of the dataset
print("Penguin Dataset:")
print(df.head())

# Drop missing values to ensure clean plots
df_clean = df.dropna(
    subset=["bill_length_mm", "bill_depth_mm", "body_mass_g"]
).sort_values("bill_length_mm")

# -------------------------------------------------------------
# 1. Scatter Plot: Culmen (Bill) Length vs. Body Mass
# -------------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(
    df_clean["bill_length_mm"],
    df_clean["body_mass_g"],
    c="blue",
    alpha=0.7,
    edgecolors="black",
)
plt.title("Scatter Plot: Culmen Length vs. Body Mass")
plt.xlabel("Culmen (Bill) Length (mm)")
plt.ylabel("Body Mass (g)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# -------------------------------------------------------------
# 2. Scatter Plot: Culmen (Bill) Depth vs. Body Mass
# -------------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(
    df_clean["bill_depth_mm"],
    df_clean["body_mass_g"],
    c="orange",
    alpha=0.7,
    edgecolors="black",
)
plt.title("Scatter Plot: Culmen Depth vs. Body Mass")
plt.xlabel("Culmen (Bill) Depth (mm)")
plt.ylabel("Body Mass (g)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# -------------------------------------------------------------
# 3. Pair Plot: Relationships Across All Features
# -------------------------------------------------------------
# Using hue to differentiate species across the pair plot matrix
sns.pairplot(df, hue="species", diag_kind="hist")
plt.show()

# -------------------------------------------------------------
# 4. Area Graph: Culmen Length vs. Body Mass
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.fill_between(
    df_clean["bill_length_mm"],
    df_clean["body_mass_g"],
    color="skyblue",
    alpha=0.4,
)
plt.plot(
    df_clean["bill_length_mm"],
    df_clean["body_mass_g"],
    color="Slateblue",
    linewidth=2,
)
plt.title("Area Graph: Culmen Length vs. Body Mass")
plt.xlabel("Culmen (Bill) Length (mm)")
plt.ylabel("Body Mass (g)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()