# Comprehensive Pandas Quick Reference Guide
*From Beginner to Intermediate - A Complete Learning Path*

## Table of Contents
1. [Installation and Imports](#installation-and-imports)
2. [Creating DataFrames](#creating-dataframes)
3. [Basic DataFrame Information](#basic-dataframe-information)
4. [Data Selection and Indexing](#data-selection-and-indexing)
5. [Data Filtering](#data-filtering)
6. [Data Manipulation](#data-manipulation)
7. [Grouping and Aggregation](#grouping-and-aggregation)
8. [Handling Missing Data](#handling-missing-data)
9. [Data Types and Conversion](#data-types-and-conversion)
10. [Merging and Joining](#merging-and-joining)
11. [Input/Output Operations](#inputoutput-operations)
12. [Time Series Data](#time-series-data)
13. [Common Methods Reference](#common-methods-reference)
14. [Best Practices](#best-practices)

---

## Installation and Imports

```python
# Install pandas (run in terminal/command prompt)
# pip install pandas

# Essential imports for data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # For plotting

# Display options for better output formatting
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Don't wrap output
pd.set_option('display.max_colwidth', 50)   # Limit column width
```

---

## Creating DataFrames

### From Dictionary
```python
# Create DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary': [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)
print(df)
```

### From Lists
```python
# Create DataFrame from list of lists
data = [
    ['Alice', 25, 'New York', 50000],
    ['Bob', 30, 'London', 60000],
    ['Charlie', 35, 'Tokyo', 70000],
    ['Diana', 28, 'Paris', 55000]
]
columns = ['Name', 'Age', 'City', 'Salary']
df = pd.DataFrame(data, columns=columns)
```

### From CSV/Excel Files
```python
# Read from CSV file
df = pd.read_csv('data.csv')

# Read from Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Read with specific parameters
df = pd.read_csv('data.csv', 
                 sep=';',           # Custom separator
                 encoding='utf-8',   # Encoding
                 na_values=['N/A', 'NULL'])  # Custom missing values
```

---

## Basic DataFrame Information

```python
# Basic information about the DataFrame
print(df.shape)        # (rows, columns)
print(df.info())       # Data types and memory usage
print(df.describe())   # Statistical summary for numeric columns
print(df.head())       # First 5 rows (default)
print(df.head(10))     # First 10 rows
print(df.tail())       # Last 5 rows
print(df.columns)      # Column names
print(df.index)        # Row indices
print(df.dtypes)       # Data types of each column

# Check for missing values
print(df.isnull().sum())    # Count of missing values per column
print(df.isna().sum())      # Same as isnull()

# Memory usage
print(df.memory_usage(deep=True))
```

---

## Data Selection and Indexing

### Column Selection
```python
# Select single column (returns Series)
ages = df['Age']
print(type(ages))  # pandas.core.series.Series

# Select single column as DataFrame
ages_df = df[['Age']]
print(type(ages_df))  # pandas.core.frame.DataFrame

# Select multiple columns
subset = df[['Name', 'Age', 'Salary']]

# Select columns by position
first_two_cols = df.iloc[:, 0:2]  # First two columns

# Select columns by condition
numeric_cols = df.select_dtypes(include=[np.number])
text_cols = df.select_dtypes(include=['object'])
```

### Row Selection
```python
# Select by position (iloc - integer location)
first_row = df.iloc[0]           # First row as Series
first_three = df.iloc[0:3]       # First three rows
last_row = df.iloc[-1]           # Last row

# Select by label (loc - label location)
# If index is default numeric, loc and iloc behave similarly
row_by_label = df.loc[0]

# Select specific rows and columns
subset = df.iloc[0:3, 1:3]       # First 3 rows, columns 1-2
subset = df.loc[0:2, 'Age':'City']  # By labels

# Boolean indexing (most common for filtering)
young_people = df[df['Age'] < 30]
high_earners = df[df['Salary'] > 55000]
```

### Advanced Selection
```python
# Select with multiple conditions
young_high_earners = df[(df['Age'] < 30) & (df['Salary'] > 50000)]
europe_or_young = df[(df['City'].isin(['London', 'Paris'])) | (df['Age'] < 30)]

# Query method (alternative to boolean indexing)
result = df.query('Age < 30 and Salary > 50000')
result = df.query('City in ["London", "Paris"]')

# Sample random rows
random_sample = df.sample(n=2)      # 2 random rows
random_percent = df.sample(frac=0.5) # 50% of rows
```

---

## Data Filtering

### Basic Filtering
```python
# Numerical comparisons
young = df[df['Age'] < 30]
high_salary = df[df['Salary'] >= 60000]
age_range = df[(df['Age'] >= 25) & (df['Age'] <= 32)]

# String operations
new_yorkers = df[df['City'] == 'New York']
name_starts_with_a = df[df['Name'].str.startswith('A')]
name_contains = df[df['Name'].str.contains('li', case=False)]

# Using isin() for multiple values
cities_of_interest = df[df['City'].isin(['London', 'Tokyo'])]
```

### Advanced Filtering
```python
# Filter using string methods
# Case-insensitive filtering
london_case_insensitive = df[df['City'].str.lower() == 'london']

# Regular expressions
pattern_match = df[df['Name'].str.match(r'^[A-C]')]  # Names starting with A, B, or C

# Filter based on index
recent_entries = df[df.index > 1]

# Filter with custom functions
def is_high_earner(row):
    return row['Salary'] > row['Age'] * 2000

high_earner_ratio = df[df.apply(is_high_earner, axis=1)]
```

---

## Data Manipulation

### Adding and Modifying Columns
```python
# Add new column with fixed value
df['Country'] = 'Unknown'

# Add column based on calculation
df['Salary_K'] = df['Salary'] / 1000  # Salary in thousands

# Add column based on condition
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Mature')

# Using np.where for conditional assignment
df['High_Earner'] = np.where(df['Salary'] > 55000, 'Yes', 'No')

# Multiple conditions with np.select
conditions = [
    df['Age'] < 25,
    (df['Age'] >= 25) & (df['Age'] < 35),
    df['Age'] >= 35
]
choices = ['Young', 'Middle', 'Senior']
df['Age_Category'] = np.select(conditions, choices, default='Unknown')

# Modify existing column
df['Name'] = df['Name'].str.upper()  # Convert to uppercase
df['Salary'] = df['Salary'] * 1.1    # 10% salary increase
```

### Dropping Data
```python
# Drop columns
df_no_salary = df.drop('Salary', axis=1)           # Drop single column
df_subset = df.drop(['Age', 'City'], axis=1)       # Drop multiple columns

# Drop rows
df_no_first = df.drop(0, axis=0)                   # Drop first row
df_no_first_last = df.drop([0, df.index[-1]], axis=0)  # Drop first and last

# Drop based on condition
df_filtered = df.drop(df[df['Age'] < 30].index)    # Drop rows where Age < 30

# Drop duplicates
df_unique = df.drop_duplicates()                   # Drop all duplicate rows
df_unique_names = df.drop_duplicates(subset=['Name'])  # Drop based on Name column
```

### Sorting and Ranking
```python
# Sort by single column
df_sorted = df.sort_values('Age')                  # Ascending (default)
df_sorted_desc = df.sort_values('Age', ascending=False)  # Descending

# Sort by multiple columns
df_multi_sort = df.sort_values(['City', 'Age'])    # First by City, then by Age

# Sort index
df_sorted_index = df.sort_index()

# Ranking
df['Age_Rank'] = df['Age'].rank()                  # Rank ages
df['Salary_Rank'] = df['Salary'].rank(ascending=False)  # Highest salary = rank 1
```

### Reshaping Data
```python
# Reset index (makes index a regular column)
df_reset = df.reset_index()

# Set column as index
df_name_index = df.set_index('Name')

# Transpose
df_transposed = df.T  # or df.transpose()

# Melt (wide to long format)
df_melted = pd.melt(df, 
                   id_vars=['Name'], 
                   value_vars=['Age', 'Salary'],
                   var_name='Attribute', 
                   value_name='Value')

# Pivot (long to wide format)
# First create a long format dataframe
long_df = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob'],
    'Metric': ['Age', 'Salary', 'Age', 'Salary'],
    'Value': [25, 50000, 30, 60000]
})
pivot_df = long_df.pivot(index='Name', columns='Metric', values='Value')
```

---

## Grouping and Aggregation

### Basic Grouping
```python
# Group by single column
city_groups = df.groupby('City')

# Basic aggregations
city_avg_age = df.groupby('City')['Age'].mean()
city_total_salary = df.groupby('City')['Salary'].sum()
city_stats = df.groupby('City').agg({
    'Age': ['mean', 'min', 'max'],
    'Salary': ['sum', 'mean', 'count']
})

# Multiple aggregations on same column
age_stats = df.groupby('City')['Age'].agg(['count', 'mean', 'std', 'min', 'max'])
```

### Advanced Grouping
```python
# Group by multiple columns
# First, let's add more categorical data
df['Department'] = ['IT', 'HR', 'IT', 'Finance']
multi_group = df.groupby(['City', 'Department'])['Salary'].mean()

# Custom aggregation functions
def salary_range(series):
    return series.max() - series.min()

custom_agg = df.groupby('City')['Salary'].agg([
    'mean',              # Built-in function
    salary_range,        # Custom function
    lambda x: x.std()    # Lambda function
])

# Apply custom function to groups
def group_summary(group):
    return pd.Series({
        'count': len(group),
        'avg_age': group['Age'].mean(),
        'total_salary': group['Salary'].sum(),
        'age_salary_ratio': group['Age'].mean() / (group['Salary'].mean() / 1000)
    })

group_summaries = df.groupby('City').apply(group_summary)

# Transform (returns same shape as original)
df['Age_Centered'] = df.groupby('City')['Age'].transform(lambda x: x - x.mean())
df['Salary_Rank_Within_City'] = df.groupby('City')['Salary'].rank(ascending=False)
```

### Pivot Tables
```python
# Create pivot table
pivot = pd.pivot_table(df, 
                      values=['Age', 'Salary'], 
                      index='City', 
                      aggfunc='mean')

# Pivot table with multiple aggregation functions
pivot_multi = pd.pivot_table(df,
                           values='Salary',
                           index='City',
                           aggfunc=['mean', 'sum', 'count'])

# Cross-tabulation
# First add another categorical column
df['Experience'] = ['Junior', 'Senior', 'Senior', 'Mid']
crosstab = pd.crosstab(df['City'], df['Experience'])
```

---

## Handling Missing Data

### Detecting Missing Data
```python
# Create sample data with missing values
df_missing = df.copy()
df_missing.loc[1, 'Age'] = np.nan
df_missing.loc[2, 'Salary'] = np.nan

# Check for missing values
print(df_missing.isnull())           # Boolean mask
print(df_missing.isnull().sum())     # Count per column
print(df_missing.isnull().any())     # Any missing values per column
print(df_missing.isnull().all())     # All missing values per column

# Info about missing data
print(df_missing.info())             # Shows non-null count
```

### Handling Missing Data
```python
# Drop missing values
df_no_na = df_missing.dropna()              # Drop any row with missing values
df_no_na_age = df_missing.dropna(subset=['Age'])  # Drop only rows with missing Age

# Fill missing values
df_filled = df_missing.fillna(0)            # Fill all NaN with 0
df_filled = df_missing.fillna({             # Fill different columns with different values
    'Age': df_missing['Age'].mean(),
    'Salary': df_missing['Salary'].median()
})

# Forward fill and backward fill
df_ffill = df_missing.fillna(method='ffill')  # Forward fill
df_bfill = df_missing.fillna(method='bfill')  # Backward fill

# Interpolation for numerical data
df_interpolated = df_missing.interpolate()

# Fill with group-specific values
df_missing['Age_Filled'] = df_missing.groupby('City')['Age'].transform(
    lambda x: x.fillna(x.mean())
)
```

---

## Data Types and Conversion

### Viewing and Converting Data Types
```python
# Check current data types
print(df.dtypes)
print(df['Age'].dtype)

# Convert data types
df['Age'] = df['Age'].astype('float64')     # Convert to float
df['Name'] = df['Name'].astype('string')    # Convert to string (pandas string type)

# Convert multiple columns at once
df = df.astype({
    'Age': 'int32',
    'Salary': 'float64'
})

# Categorical data (memory efficient for repeated values)
df['City'] = df['City'].astype('category')
print(df['City'].cat.categories)            # View categories

# DateTime conversion
dates = ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']
df['Join_Date'] = pd.to_datetime(dates)

# Numeric conversion with error handling
df['Salary_Safe'] = pd.to_numeric(df['Salary'], errors='coerce')  # NaN for errors
```

### Working with Strings
```python
# String methods (use .str accessor)
df['Name_Lower'] = df['Name'].str.lower()
df['Name_Length'] = df['Name'].str.len()
df['First_Letter'] = df['Name'].str[0]

# String splitting
df['First_Name'] = df['Name'].str.split().str[0]  # First word

# String replacement
df['City_Clean'] = df['City'].str.replace(' ', '_')

# String contains
df['Has_A'] = df['Name'].str.contains('a', case=False)
```

---

## Merging and Joining

### Sample DataFrames for Merging
```python
# Create additional dataframes for merging examples
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'dept_id': [1, 2, 1, 3]
})

departments = pd.DataFrame({
    'dept_id': [1, 2, 3, 4],
    'dept_name': ['IT', 'HR', 'Finance', 'Marketing'],
    'location': ['NY', 'London', 'Tokyo', 'Paris']
})

salaries = pd.DataFrame({
    'emp_id': [1, 2, 3, 5],  # Note: emp_id 5 doesn't exist in employees
    'salary': [50000, 60000, 70000, 55000]
})
```

### Different Types of Joins
```python
# Inner join (default) - only matching records
inner_join = pd.merge(employees, departments, on='dept_id')

# Left join - all records from left DataFrame
left_join = pd.merge(employees, departments, on='dept_id', how='left')

# Right join - all records from right DataFrame
right_join = pd.merge(employees, departments, on='dept_id', how='right')

# Outer join - all records from both DataFrames
outer_join = pd.merge(employees, departments, on='dept_id', how='outer')

# Join on different column names
emp_sal = pd.merge(employees, salaries, on='emp_id')

# Join on index
employees_indexed = employees.set_index('emp_id')
salaries_indexed = salaries.set_index('emp_id')
index_join = employees_indexed.join(salaries_indexed, how='inner')
```

### Concatenation
```python
# Concatenate vertically (stack DataFrames)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
vertical_concat = pd.concat([df1, df2], ignore_index=True)

# Concatenate horizontally
horizontal_concat = pd.concat([df1, df2], axis=1)

# Concatenate with keys
keyed_concat = pd.concat([df1, df2], keys=['first', 'second'])
```

---

## Input/Output Operations

### Reading Data
```python
# CSV files
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', 
                sep=';',                    # Custom separator
                header=0,                   # Header row
                names=['col1', 'col2'],     # Custom column names
                skiprows=1,                 # Skip first row
                nrows=1000,                # Read only first 1000 rows
                encoding='utf-8',          # Encoding
                na_values=['N/A', ''])     # Custom NA values

# Excel files
df = pd.read_excel('data.xlsx')
df = pd.read_excel('data.xlsx', 
                  sheet_name='Sheet2',      # Specific sheet
                  usecols='A:D',           # Specific columns
                  skiprows=2)              # Skip rows

# JSON files
df = pd.read_json('data.json')
df = pd.read_json('data.json', orient='records')  # For array of objects

# SQL databases (requires sqlalchemy)
# import sqlalchemy
# engine = sqlalchemy.create_engine('sqlite:///database.db')
# df = pd.read_sql('SELECT * FROM table_name', engine)
```

### Writing Data
```python
# CSV files
df.to_csv('output.csv', index=False)        # Don't include index
df.to_csv('output.csv', 
         sep=';',                           # Custom separator
         columns=['Name', 'Age'],           # Specific columns
         header=False)                      # No header

# Excel files
df.to_excel('output.xlsx', index=False)
df.to_excel('output.xlsx', 
           sheet_name='Data',               # Custom sheet name
           startrow=1,                      # Start at row 1
           startcol=1)                      # Start at column 1

# JSON files
df.to_json('output.json', orient='records', indent=2)

# Multiple sheets in Excel
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    df.head().to_excel(writer, sheet_name='Sheet2', index=False)
```

---

## Time Series Data

### Creating DateTime Data
```python
# Create date range
dates = pd.date_range('2023-01-01', periods=100, freq='D')  # Daily
dates = pd.date_range('2023-01-01', '2023-12-31', freq='W')  # Weekly

# Convert string to datetime
df['date_str'] = ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']
df['date'] = pd.to_datetime(df['date_str'])

# Create time series DataFrame
ts_data = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=365, freq='D'),
    'value': np.random.randn(365).cumsum()
})
ts_data.set_index('date', inplace=True)
```

### Time Series Operations
```python
# Extract date components
ts_data['year'] = ts_data.index.year
ts_data['month'] = ts_data.index.month
ts_data['day_of_week'] = ts_data.index.day_name()

# Resampling (aggregating by time periods)
monthly_avg = ts_data.resample('M').mean()      # Monthly average
weekly_sum = ts_data.resample('W').sum()        # Weekly sum
quarterly_std = ts_data.resample('Q').std()     # Quarterly standard deviation

# Time-based selection
jan_data = ts_data['2023-01']                   # All January data
q1_data = ts_data['2023-01':'2023-03']         # Q1 data
recent_data = ts_data.last('30D')              # Last 30 days

# Rolling windows
ts_data['rolling_mean'] = ts_data['value'].rolling(window=7).mean()    # 7-day moving average
ts_data['rolling_std'] = ts_data['value'].rolling(window=30).std()     # 30-day rolling std

# Lag and lead
ts_data['value_lag1'] = ts_data['value'].shift(1)    # Previous day's value
ts_data['value_lead1'] = ts_data['value'].shift(-1)  # Next day's value
```

---

## Common Methods Reference

### DataFrame Methods
| Method | Description | Example |
|--------|-------------|---------|
| `head(n)` | First n rows | `df.head(10)` |
| `tail(n)` | Last n rows | `df.tail(5)` |
| `info()` | DataFrame info | `df.info()` |
| `describe()` | Statistical summary | `df.describe()` |
| `shape` | Dimensions | `df.shape` |
| `columns` | Column names | `df.columns` |
| `index` | Row indices | `df.index` |
| `dtypes` | Data types | `df.dtypes` |
| `memory_usage()` | Memory usage | `df.memory_usage(deep=True)` |
| `sample(n)` | Random sample | `df.sample(5)` |
| `copy()` | Deep copy | `df_copy = df.copy()` |

### Selection Methods
| Method | Description | Example |
|--------|-------------|---------|
| `loc[]` | Label-based selection | `df.loc[0:2, 'Name':'Age']` |
| `iloc[]` | Position-based selection | `df.iloc[0:3, 1:3]` |
| `at[]` | Single value by label | `df.at[0, 'Name']` |
| `iat[]` | Single value by position | `df.iat[0, 1]` |
| `query()` | SQL-like filtering | `df.query('Age > 25')` |
| `where()` | Conditional selection | `df.where(df['Age'] > 25)` |
| `mask()` | Inverse of where | `df.mask(df['Age'] < 25)` |

### Aggregation Methods
| Method | Description | Example |
|--------|-------------|---------|
| `sum()` | Sum values | `df['Age'].sum()` |
| `mean()` | Average | `df['Age'].mean()` |
| `median()` | Median | `df['Age'].median()` |
| `std()` | Standard deviation | `df['Age'].std()` |
| `var()` | Variance | `df['Age'].var()` |
| `min()` | Minimum | `df['Age'].min()` |
| `max()` | Maximum | `df['Age'].max()` |
| `count()` | Non-null count | `df['Age'].count()` |
| `nunique()` | Unique count | `df['City'].nunique()` |
| `value_counts()` | Value frequencies | `df['City'].value_counts()` |

### String Methods (use with .str)
| Method | Description | Example |
|--------|-------------|---------|
| `lower()` | Lowercase | `df['Name'].str.lower()` |
| `upper()` | Uppercase | `df['Name'].str.upper()` |
| `title()` | Title case | `df['Name'].str.title()` |
| `len()` | String length | `df['Name'].str.len()` |
| `contains()` | Contains pattern | `df['Name'].str.contains('A')` |
| `startswith()` | Starts with | `df['Name'].str.startswith('A')` |
| `endswith()` | Ends with | `df['Name'].str.endswith('e')` |
| `replace()` | Replace text | `df['Name'].str.replace('A', 'a')` |
| `split()` | Split string | `df['Name'].str.split(' ')` |
| `strip()` | Remove whitespace | `df['Name'].str.strip()` |

---

## Best Practices

### Performance Tips
```python
# 1. Use vectorized operations instead of loops
# Bad
result = []
for index, row in df.iterrows():
    result.append(row['Age'] * 2)
df['Age_Doubled_Slow'] = result

# Good
df['Age_Doubled_Fast'] = df['Age'] * 2

# 2. Use categorical data for repeated strings
df['City'] = df['City'].astype('category')

# 3. Use appropriate data types
df['Age'] = df['Age'].astype('int32')  # Instead of int64 if values fit

# 4. Chain operations efficiently
result = (df
          .query('Age > 25')
          .groupby('City')['Salary']
          .mean()
          .sort_values(ascending=False))

# 5. Use copy() when needed to avoid SettingWithCopyWarning
df_subset = df[df['Age'] > 25].copy()
df_subset['New_Column'] = 'value'
```

### Code Organization
```python
# 1. Use meaningful variable names
employee_data = pd.read_csv('employees.csv')
high_performers = employee_data[employee_data['performance_score'] > 8]

# 2. Break complex operations into steps
# Instead of one long chain, break it down
filtered_data = df[df['Age'] > 25]
grouped_data = filtered_data.groupby('City')
summary_stats = grouped_data.agg({
    'Age': 'mean',
    'Salary': ['sum', 'count']
})

# 3. Use functions for repeated operations
def calculate_age_groups(df, age_col='Age'):
    """Categorize ages into groups."""
    conditions = [
        df[age_col] < 25,
        (df[age_col] >= 25) & (df[age_col] < 35),
        df[age_col] >= 35
    ]
    choices = ['Young', 'Middle', 'Senior']
    return np.select(conditions, choices, default='Unknown')

df['Age_Group'] = calculate_age_groups(df)
```

### Common Pitfalls to Avoid
```python
# 1. Avoid chained assignment (SettingWithCopyWarning)
# Bad
df[df['Age'] > 25]['New_Column'] = 'value'  # Warning!

# Good
mask = df['Age'] > 25
df.loc[mask, 'New_Column'] = 'value'

# 2. Be careful with inplace operations
df.dropna(inplace=True)  # Modifies original DataFrame
df_clean = df.dropna()   # Creates new DataFrame (safer)

# 3. Remember that some operations return Series, others DataFrame
ages_series = df['Age']      # Series
ages_df = df[['Age']]        # DataFrame

# 4. Use appropriate join types
# Make sure you understand the difference between inner, left, right, outer joins

# 5. Handle missing data explicitly
# Don't assume data is clean - always check for and handle NaN values
```

### Debugging Tips
```python
# 1. Use info() to understand your data structure
print(df.info())

# 2. Check for unexpected data types
print(df.dtypes)

# 3. Look for missing values
print(df.isnull().sum())

# 4. Examine unique values in categorical columns
print(df['City'].value_counts())

# 5. Use head() and tail() to spot-check results
print(result.head())

# 6. Use assert statements to validate assumptions
assert df['Age'].min() >= 0, "Age cannot be negative"
assert df['Age'].max() <= 150, "Age seems unrealistic"
```

---

## Conclusion

This guide covers the essential Pandas operations from basic DataFrame creation to advanced data manipulation. Remember that Pandas is incredibly powerful and flexible - there are often multiple ways to accomplish the same task. As you become more comfortable with these basics, you'll develop your own preferred patterns and discover more advanced features.

### Next Steps for Learning
1. Practice with real datasets from sources like Kaggle
2. Learn about advanced indexing with MultiIndex
3. Explore time series analysis in more depth
4. Study performance optimization techniques
5. Learn integration with other libraries (NumPy, Matplotlib, Scikit-learn)

### Useful Resources
- Official Pandas Documentation