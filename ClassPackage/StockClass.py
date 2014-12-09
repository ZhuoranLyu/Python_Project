'''
Created on 2014.12.1

@author: Fangyun Sun
'''

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from ClassPackage.MarketClass import *
from Utilities.Exceptions import *
from Utilities.Inputfunctions import *

#

class Stock():
    '''
    Generate a class describe the stock containing several attributes and functions.
    
    '''

    def __init__(self, stock,start,end):
        '''
        Constructor:
        
        Input:
            stock(string): the name of stock, can be read into pandas.io.data.DataReader
            start(string): the start time of date range from user input
            end(string): the end time of date range from user input
        
        Attributes:
            stock(string): the name of stock
            start(pandas.datatime): the start time of date range 
            end(pandas.datatime): the end time of date range 
            dataframe(pandas.dataframe): extract the data from the yahoo financial
            close_price(pandas.series): the column 'Adj Close' in the dataframe
            period_ret(float) : the return between this date range
        '''
        
        if IsEmptyInput(stock,start,end):
            raise EmptyInputException()
        else:
            if IsValidStockName(stock):
                self.stock = ParseStockName(stock).upper()
            else:
                raise StockNameInputException()
            if IsValidDate(start) and IsValidDate(end):
                if IsValidDateRange(start,end): 
                    pass
                else:
                    raise DateRangeException()
                self.starttime = ParseDate(start)
                self.endtime = ParseDate(end)
                
            else:
                raise DateInputException()       
        self.dataframe = web.DataReader(stock,'yahoo',start,end)
        self.close_price = self.dataframe['Adj Close']
        self.period_ret = (self.close_price[-1]-self.close_price[0])/self.close_price[0]
    
    def change_price_precent(self):
        """
        Generate the percent change of daily close price.
        """
        stock_firstday = self.close_price[0]
        self.dataframe['stock_%chg'] = (self.close_price - stock_firstday)/stock_firstday
        change_price_precent = self.dataframe['stock_%chg']
        return change_price_precent
    
    def plot_close_price(self):
        
        fig = plt.figure()
        self.close_price.plot(color = 'b',label = self.stock)
        plt.legend()
        plt.xticks(rotation=45)
        plt.title('The Close Price of {} '.format(self.stock))
        plt.xlabel('Date Time')
        plt.ylabel('Close Price')
        plt.show()
    

    def plot_changeprice_comparison(self):
        """
        Compare and plot the percent change of the stock close price and that of the actual market over time.
        """
        fig = plt.figure()
        self.change_price_precent().plot(color = 'b',label = self.stock)
        market = Market(self.starttime,self.endtime)
        market.change_price_precent().plot(color = 'r',label = 'S&P 500')
        plt.legend()
        plt.xticks(rotation=45)
        plt.title('The Comparison between {} and S&P 500 close price '.format(self.stock))
        plt.xlabel('Date Time')
        plt.ylabel('Percent Change of Close Price')
        plt.show()
        
    def close_price_describe(self):
        return self.close_price.describe()
    
if __name__ == '__main__':
    start = '2011/1/1'
    end = '2012/1/1'
    stock = Stock('IBM',start,end)         