# Import the os library
import os

# Import the pandas library as pd
import pandas as pd

# Import the array_split method, from the numpy library
import numpy as np


my_list = ['one', 'two', 'Three']
results = np.array_split(my_list, 3)

for result in results:
    print( result)