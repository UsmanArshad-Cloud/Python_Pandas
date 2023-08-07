# Python Pandas
import pandas as pd
import numpy as np

dict1 = {
    "Name": ['Usman','Ali'],
    "Age": [30, 50]
}
df = pd.DataFrame(dict1)
df.to_csv('dict1.csv')     # index=false for saving in such a way that no index column will be present
print(df)                  # df.head(), df.tail() for getting first or last rows
print(df.describe())
file = pd.read_csv('dict1.csv')
#file['Age'][0]=70
file.loc[0, 'Age'] = 70
print(file)