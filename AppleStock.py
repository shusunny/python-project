# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:09:13 2021

@author: sunny
"""

import pandas as pd
import numpy as np

# import csv dataset
data = pd.read_csv('C:\\Users\\shusu\\WorkSpace\\python-project\\AAPL.csv')

# Create an empty dataframe to hold our results
possible_entry_exit = pd.DataFrame(columns=["entry","exit","profit","days","ProfitRate","preEntryDay"])
