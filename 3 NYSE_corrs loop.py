#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:27:25 2023

@author: leongedzo
"""
#----------------------------------------------------------------------
#Step 1: Importing libraries

import os
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#----------------------------------------------------------------------
#Step 2: Identifying paths and functions

pathExp = '/Users/leongedzo/python_pers/stock_data_cleaned/'
ExpName = 'NYSE_stationary_lags/' #'Test 10/'

pathImp = '/Users/leongedzo/python_pers/stock_data_cleaned/'
ImpName = 'NYSE correlations 0.7/'

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def left(s, amount):
    return s[:amount]

#----------------------------------------------------------------------
#Step 3: For every stock perform correlation analysis with every other stock data (with original data and 4 lags). Save results to a folder.

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
                filelist.append(fileA.name)
                
                dfa = pd.read_csv(pathExp + ExpName + fileA.name)
                NlenA = len(dfa['Adj Close'].dropna())
                
                if NlenA >= 100:
            
                    #Na = dfa['Adj Close'].iloc[0:NlenA]
                    D1a = dfa['diff1'].iloc[1:NlenA]
                    L1a = dfa['diff1lag1'].iloc[2:NlenA]
                    L2a = dfa['diff1lag2'].iloc[3:NlenA]
                    L3a = dfa['diff1lag3'].iloc[4:NlenA]
                    L4a = dfa['diff1lag4'].iloc[5:NlenA]
            
                    DL1ab = dfa['diff1'].iloc[2:NlenA]
                    DL2ab = dfa['diff1'].iloc[3:NlenA]
                    DL3ab = dfa['diff1'].iloc[4:NlenA]
                    DL4ab = dfa['diff1'].iloc[5:NlenA]
                    
                    d = 0
                    # ----------------------------------------------------------------------
                    for fileB in os.scandir(pathExp + ExpName):
                        try:
                            if fileB.name != '.DS_Store':
                                c = 0
                                if fileB.is_file():   
                                    for i in filelist:
                                        if fileB.name == i:
                                            c += 1
                                    if c == 0:
                                        
                                        dfb = pd.read_csv(pathExp + ExpName + fileB.name)
                                        NlenB = len(dfb['Adj Close'].dropna())
                                        if NlenB == NlenA:
                                
                                            D1b = dfb['diff1'].iloc[1:NlenA]
                                            L1b = dfb['diff1lag1'].iloc[2:NlenA]
                                            L2b = dfb['diff1lag2'].iloc[3:NlenA]
                                            L3b = dfb['diff1lag3'].iloc[4:NlenA]
                                            L4b = dfb['diff1lag4'].iloc[5:NlenA]
                                    
                                            DL1ba = dfb['diff1'].iloc[2:NlenA]
                                            DL2ba = dfb['diff1'].iloc[3:NlenA]
                                            DL3ba = dfb['diff1'].iloc[4:NlenA]
                                            DL4ba = dfb['diff1'].iloc[5:NlenA]
                                    
                                            # ----------------------------------------------------------------------
                                            corlista = [D1a,DL1ab,DL2ab,DL3ab,DL4ab]
                                            corlistab = [D1b,L1b,L2b,L3b,L4b]
                                    
                                            corlistb = [D1b,DL1ba,DL2ba,DL3ba,DL4ba]
                                            corlistba = [D1a,L1a,L2a,L3a,L4a]
                                            
                                            Names = []
                                            Corr = []
                                            Pval = []
                                            
                                            t = 0
                                            for a in corlista:
                                                Names.append(namestr(a,globals())[0]) 
                                                Corr.append(round(sp.stats.pearsonr(a,corlistab[t])[0],5)) 
                                                Pval.append(round(sp.stats.pearsonr(a,corlistab[t])[1],5))
                                                t += 1
                                                
                                            t = 0
                                            for b in corlistb:
                                                Names.append(namestr(b,globals())[0]) 
                                                Corr.append(round(sp.stats.pearsonr(b,corlistba[t])[0],5)) 
                                                Pval.append(round(sp.stats.pearsonr(b,corlistba[t])[1],5))
                                                t += 1
                                                
                                    
                                    
                                            List_of_tuples = list(zip(Names,Corr,Pval))
                                            #print(data) 
                                    
                                            table = pd.DataFrame(List_of_tuples,columns = ['Names', 'Corr', 'Pval'])
                                            table.insert(0,column = 'Files', value = (left(fileA.name,-4)) + "/" + left(fileB.name,-4))
                                            #print(table.sort_values('Corr',key = abs, ascending = False))
                                            p = 0
                                            for i in table['Corr']:
                                                if abs(i) > 0.7:
                                                    p += 1
                                            if p > 0:
                                                
                                                d += 1
                                                finalt = table.sort_values('Corr',key = abs, ascending = False)
                                                finalt.to_csv(pathImp + ImpName + left(fileA.name,-4) + '&' + left(fileB.name,-4) + '.csv')
                                                #print(table)
                        except:
                            print(f'{left(fileA.name,-4)} has problems with {left(fileB.name,-4)}')
            print(f'{left(fileA.name,-4)} correlations are prepared (file = {k} got {d} corrs >0.7)')
                                
        
                                
                                
                        
                                #table.to_csv(pathImp + ImpName + ArithmeticError


    
