#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:42:46 2023

@author: ali
"""

import pandas as pd

# for plotting
import matplotlib.pyplot as plt
import seaborn as sns

#%%

# load dataset
data = pd.read_csv('train.csv', index_col = 0)

#%%

# rows and columns of the data
print(data.shape)

#%%
# Find each column % of missing values, sort them, and then plot

data.isnull().mean().loc[lambda x : x > 0].sort_values(ascending = True).plot.barh()

