# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset from sklearn
iris = load_iris(as_frame=True)
df = iris.frame   # Convert to pandas DataFrame

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check dataset info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean dataset (not really needed here since Iris has no missing values)
df = df.dropna()


# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby("target").mean()
print("\nMean values grouped by species:")
print(grouped)

# Rename target column to species names for clarity
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# Interesting finding example
print("\nObservation: Virginica flowers tend to have the largest petals on average.")


# 1. Line Chart (simulate a trend using index as "time")
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (average petal length by species)
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (sepal length vs petal length)
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()


# Error Handling Example (for CSV file loading)
try:
    # Example: Replace with your own dataset file path if needed
    df_csv = pd.read_csv("non_existing_file.csv")
except FileNotFoundError:
    print("\nError: The dataset file was not found. Please check the path.")
