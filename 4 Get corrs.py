#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:19:28 2023

@author: leongedzo
"""

import os
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


pathExp = '/Users/leongedzo/python_pers/stock_data_cleaned/'
ExpName = 'NYSE correlations 0.7/'#'NYSE_stationary_lags/' #'Test 10/'

# =============================================================================
# pathImp = '/Users/leongedzo/python_pers/stock_data_cleaned/'
# ImpName = 'NYSE correlations 0.7/'
# =============================================================================

# ----------------------------------------------------------------------

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def left(s, amount):
    return s[:amount]

insides = []

k = 0
filelist = []
f = 0
for fileA in os.scandir(pathExp + ExpName):
    f += 1
    if f > 0:
        if fileA.name != '.DS_Store':
            k += 1
            #print(f'{k} ===============================')
            if fileA.is_file():
                #filelist.append(fileA.name)
                
                dfa = pd.read_csv(pathExp + ExpName + fileA.name)
                cols = ['Files','Names','Corr']
                #NlenA = len(dfa['Adj Close'].dropna())
                v = -1
                #print(dfa)
                for i in dfa['Names']:
                    v += 1
                    #if i != 'D1a' and i != 'D1b':
                    if dfa.iloc[v,3] <= -0.6:
                        insides.append(dfa.iloc[v,1])
                        print(dfa.loc[[dfa.index[v]]])
                        #print(dfa.iloc())
  
print(insides)
print(len(insides))
                
                
                
                
