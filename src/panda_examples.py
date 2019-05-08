import pandas as pd
import numpy as np

# There are three datastructures in panda
# 1. Series ==> They are a 1-D Matrix
# 2. DataFrame ==> They are a 2-D Matrix
# 3. Panel ==> They are a 3-D Matrix


# Creating a Series Datastructure
a = [1, 2, 3, 4, 5]
series = pd.Series(a)
print(series)

# Creating the Dataframe Datastructure
b = [['Ashika', 24], ['Tanu', 23], ['Ashwin', 22],['Mohith', 16], ['Sourabh', 10]]
dataframe = pd.DataFrame(b, columns= ['Name', 'Age'], dtype= int)
print(dataframe)

# Creating the Panel Datastructure
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p.minor_xs(1))

