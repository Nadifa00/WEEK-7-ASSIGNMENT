# Python Data Analysis Assignment

## Objective
- Load and analyze a dataset using the pandas library in Python.
- Create simple plots and charts with matplotlib for data visualization.

## Dataset
- **Dataset used:** Iris dataset (loaded from sklearn)
- **Format:** Pandas DataFrame

## Steps Performed

### 1. Data Loading & Exploration
- Loaded the Iris dataset using `sklearn.datasets.load_iris()`.
- Displayed the first few rows with `.head()`.
- Checked dataset info and data types using `.info()`.
- Checked for missing values and cleaned the dataset by dropping any missing rows (if present).

### 2. Basic Data Analysis
- Computed basic statistics of numerical columns using `.describe()`.
- Grouped data by the categorical column `species` and computed mean values.
- Observed that Virginica flowers tend to have the largest petals on average.

### 3. Data Visualization
- **Line Chart:** Sepal length trend over sample index.
- **Bar Chart:** Average petal length per species.
- **Histogram:** Distribution of sepal width.
- **Scatter Plot:** Relationship between sepal length and petal length.
- All plots are labeled with titles, axes, and legends.

### 4. Error Handling
- Example of handling file read errors using try-except for CSV files.

## Libraries Used
- pandas
- matplotlib
- seaborn
- scikit-learn
