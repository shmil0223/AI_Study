import pandas as pd
import numpy as np
data = pd.read_csv('employees.csv')
print(data) 
data.to_excel('employees.xlsx')