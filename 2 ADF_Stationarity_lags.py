#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 23:19:29 2023

@author: leongedzo
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


pathExp = '/Users/leongedzo/python_pers/stock_data/'
ExpName = 'NYSE/'

pathImp = '/Users/leongedzo/python_pers/stock_data_cleaned/'
ImpName = 'NYSE_stationary_lags/'

#=======================================================
k = 0
countNS = 0
countS = 0
for file in os.scandir(pathExp + ExpName):
    k += 1
    print(k)
    c = 0
    if file.is_file():
        df = pd.read_csv(pathExp + ExpName + file.name)
        dflcheck = df['Adj Close']
        l = len(dflcheck.replace("",np.nan).dropna())
        la = len(dflcheck)
        #l = len(df.replace("",np.nan).dropna())
        if l >= 100 and l == la:
            #print(file.name)
            dfmod = df[['Date','Adj Close']]
            stationarity = adfuller(dfmod['Adj Close'].dropna())
            if stationarity[0] < stationarity[4]['5%'] and stationarity[1] < 0.05:
                print(f'H1: {file.name} is stationary LV1;', end = " ")
                print('p-value: %f' % stationarity[1])
            else:
                print(f'H0: {file.name} is not stationary LV1', end = " ")   
                print('p-value: %f' % stationarity[1])
                countNS += 1
                dfmod.insert(2,column = 'diff1', value = dfmod['Adj Close'].diff())
                
                stationarity = adfuller(dfmod['diff1'].dropna())
                # =============================================================================
                # print('ADF Statistic: %f' % stationarity[0])
                # print('p-value: %f' % stationarity[1])
                # print('Critical Values:')
                # for key, value in stationarity[4].items():
                #      print('\t%s: %.3f' % (key,value))
                # =============================================================================
                if stationarity[0] > stationarity[4]['5%'] and stationarity[1] > 0.05:
                    print(f'H0: {file.name} is not stationary LV2', end = " ")
                    print('p-value: %f' % stationarity[1])
                else:

                    print(f'H1: {file.name} is now stationary LV2;', end = " ")
                    print('p-value: %f' % stationarity[1])
                    
                    dfmod.insert(3,column = 'diff1lag1', value = dfmod[['diff1']].shift(1))
                    dfmod.insert(4,column = 'diff1lag2', value = dfmod[['diff1']].shift(2))
                    dfmod.insert(5,column = 'diff1lag3', value = dfmod[['diff1']].shift(3))
                    dfmod.insert(6,column = 'diff1lag4', value = dfmod[['diff1']].shift(4))
                        
                    dfmod.round(10).to_csv(pathImp + ImpName + 'S_L4_' + file.name)
                    countS += 1
                        #print(f'{file.name} is now stationary')





print(f'Total was {countNS} non stationary TSs')
print(f'Now there is {countS} stationary TSs')




#plt.plot()




            
