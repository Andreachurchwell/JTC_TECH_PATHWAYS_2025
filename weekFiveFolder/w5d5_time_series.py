from datetime import datetime
import pandas as pd

# DateTime Object
dt = datetime(2023, 5, 16, 12, 30)
print(dt)
# Timestamp
ts = pd.Timestamp('2024-01-01 09:00')
print(ts)
# DateTimeIndex
dates = pd.date_range('2024-01-01', periods=4, freq='D')
print(dates)
# Time-based indexing
df = pd.DataFrame({'value': [10, 20, 30, 40]}, index=dates)
selected = df['2024-01-02':'2024-01-03']
print(df)
# Resampling
df_resampled = df.resample('2D').mean()  # Every 2 days
print(df_resampled)