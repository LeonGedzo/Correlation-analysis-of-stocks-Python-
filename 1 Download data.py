import pandas as pd
import time as ti
import datetime as dt
import csv

#Preparing data and setting variables

pathExp = '/Users/leongedzo/python_pers/req_data_external/' #pathExp - for csv of tickers' names
ExpName = 'NYSE tickers.csv'

pathImp = '/Users/leongedzo/python_pers/stock_data/' #pathImp - for saving stocks' data into specific folder
ImpName = 'NYSE/'

ImpTickerFile = open(pathExp + ExpName, 'r')
tickers = list(csv.reader(ImpTickerFile, delimiter=','))
ImpTickerFile.close()
    
period1 = int(ti.mktime(dt.datetime(2010,1,1,00,1).timetuple()))
period2 = int(ti.mktime(dt.datetime(2023,10,31,23,59).timetuple()))
freq = '1wk' #1d 1m

#Going though the list and saving data for every ticker
s = 1
for t in tickers[3000:3299]:
    try:
        tic = t[0]
        #print(tic)
        query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{tic}?period1={period1}&period2={period2}&interval={freq}&events=history&includeAdjustedClose=true'
        df = pd.read_csv(query_string)
        df.to_csv(pathImp + ImpName + tic + '.csv', index=False)
        print(f'{s} {tic} file is created')
        s += 1
    except: 
        print(f'---------{s} {tic} data is unavailable----------')
        s += 1
        
        
