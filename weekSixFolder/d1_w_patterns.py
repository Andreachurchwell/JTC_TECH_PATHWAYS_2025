# 📊 STATISTICS CHEAT SHEET (Python Basics for Class)

# 🔹 MEAN (Average)
nums = [1, 2, 3, 4]
mean = sum(nums) / len(nums)

# 🔹 MEDIAN (Middle Value)
nums = [3, 1, 4, 2]
sorted_nums = sorted(nums)
mid = len(nums) // 2
if len(nums) % 2 == 0:
    median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
else:
    median = sorted_nums[mid]

# 🔹 MODE (Most Frequent Value)
from statistics import mode
mode([1, 2, 2, 3, 3, 3])  # Output: 3

# 🔹 VARIANCE (Spread of the data)
import statistics
variance = statistics.variance([1, 2, 3, 4, 5])
print('variance===',variance)
# 🔹 STANDARD DEVIATION (How far values are from the mean)
std_dev = statistics.stdev([1, 2, 3, 4, 5])
print('std_dev==',std_dev)
# 🔹 ROLLING MEAN (Moving average over a window)
def rolling_mean(nums, window):
    result = []
    for i in range(len(nums) - window + 1):
        window_avg = sum(nums[i:i+window]) / window
        result.append(round(window_avg, 2))
    return result

print(rolling_mean([1, 2, 3, 4, 5], 3))  # Output: [2.0, 3.0, 4.0]