import pandas as pd
import numpy as np


# ser = pd.Series()

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Do some math with it
print("Mean:", np.mean(arr))
print("Squared:", arr ** 2)

data = {
    'name': ['andrea'],
    'city': ['selmer']
}
df = pd.DataFrame(data)
print(df[['name', 'city']])