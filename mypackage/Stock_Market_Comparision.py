'''
Created on 2014.12.1

@author: apple
'''

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from StockClass import *
from MarketClass import *

#
def main():
    start = pd.datetime(2011,11,21)
    end = pd.datetime(2013,3,21)
    stock = Stock('IBM',start,end)
    stock.plot_changeprice_comparison()

def test():
    start = pd.datetime(2011,11,21)
    end = pd.datetime(2013,3,21)
    stock = Stock('IBM',start,end)
    stock.plot_close_price() 
if __name__ == '__main__':
    test()