'''
Created on 2014.12.1

@author: Fangyun Sun
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ClassPackage.StockClass import *
import matplotlib.cm as cm
from Utilities.Exceptions import *

def check_stock_names(stock_name_list):
    stock_name_list = [x.upper() for x in stock_name_list]
    unique_names = list(set(stock_name_list))
    if len(unique_names) == 1 and '' in unique_names:
        raise EmptyInputException()
    else:
        return [x for x in unique_names if x]
    
def multistocks_percentchange(stock_name_list,start,end):
    unique_stocks = check_stock_names(stock_name_list)
    length = len(unique_stocks)
    colors=cm.rainbow(np.linspace(0,1,length))
    stock_class_list = [Stock(stock,start,end) for stock in unique_stocks]
    i=0
    for item in stock_class_list:
        item.change_price_precent().plot(color =colors[i], label = item.stock)
        i = i+1
    plt.xticks(rotation=45)
    plt.legend()
    plt.xlabel('Date Time')
    plt.ylabel('Percent Change of Close Price')
    plt.title('The Percent Change Comparison between stocks')
    plt.show()
