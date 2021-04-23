# %%
#Importing the libraries to be used:
import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
%matplotlib inline
# %%
df = pd.read_csv('creditcard.csv')
print(df.shape)
# %%
df.dropna('columns')
print(df.shape)
# %%
