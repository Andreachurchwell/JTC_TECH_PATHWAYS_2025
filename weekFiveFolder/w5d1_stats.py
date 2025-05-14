import statistics
import math
from scipy import stats

# Sample dataset
data = [10, 12, 12, 15, 18, 18, 18, 21, 24, 30, 100]  # includes an outlier

# 1. Central Tendency
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

# 2. Dispersion
data_range = max(data) - min(data)
variance = statistics.variance(data)
std_dev = statistics.stdev(data)

# 3. Quartiles and IQR
q1 = statistics.quantiles(data, n=4)[0]
q3 = statistics.quantiles(data, n=4)[2]
iqr = q3 - q1

# Outliers (using 1.5 * IQR rule)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = [x for x in data if x < lower_bound or x > upper_bound]

# 4. Z-scores
z_scores = [(x - mean) / std_dev for x in data]

# 5. Skewness and Kurtosis
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# Display results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Outliers:", outliers)
print("Z-scores:", z_scores)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
