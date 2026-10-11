# Visualization Using Histogram

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Seaborn's built-in Penguins dataset
# (Note: You can also load your CSV file using pd.read_csv('path_to_file.csv'))
df = sns.load_dataset("penguins")

# Display the first few rows of the dataset
print("Penguin Dataset:")
print(df.head())

# Set up the figure for subplots to display all histograms clearly
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle(
    "Penguin Features Distribution (Histograms)", fontsize=16, fontweight="bold"
)

# ---------------------------------
# 1. Culmen Length (Bill Length) Histogram
# ---------------------------------
axes[0, 0].hist(
    df["bill_length_mm"].dropna(),
    bins=15,
    color="skyblue",
    edgecolor="black",
    rwidth=0.85,
)
axes[0, 0].set_title("Culmen (Bill) Length Distribution")
axes[0, 0].set_xlabel("Bill Length (mm)")
axes[0, 0].set_ylabel("Frequency")

# ---------------------------------
# 2. Culmen Depth (Bill Depth) Histogram
# ---------------------------------
axes[0, 1].hist(
    df["bill_depth_mm"].dropna(),
    bins=12,
    color="salmon",
    edgecolor="black",
    rwidth=0.85,
)
axes[0, 1].set_title("Culmen (Bill) Depth Distribution")
axes[0, 1].set_xlabel("Bill Depth (mm)")
axes[0, 1].set_ylabel("Frequency")

# ---------------------------------
# 3. Flipper Length Histogram
# ---------------------------------
axes[1, 0].hist(
    df["flipper_length_mm"].dropna(),
    bins=15,
    color="lightgreen",
    edgecolor="black",
    rwidth=0.85,
)
axes[1, 0].set_title("Flipper Length Distribution")
axes[1, 0].set_xlabel("Flipper Length (mm)")
axes[1, 0].set_ylabel("Frequency")

# ---------------------------------
# 4. Body Mass Histogram
# ---------------------------------
axes[1, 1].hist(
    df["body_mass_g"].dropna(),
    bins=20,
    color="orange",
    edgecolor="black",
    rwidth=0.85,
)
axes[1, 1].set_title("Body Mass Distribution")
axes[1, 1].set_xlabel("Body Mass (g)")
axes[1, 1].set_ylabel("Frequency")

# Adjust layout and display the plots
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()