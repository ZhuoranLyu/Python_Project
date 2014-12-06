import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from ClassPackage.StockClass import *
from PortfolioPackage.PortfolioDataProcessing import *
from PortfolioPackage.PortfolioFunctions import *
from StocksPackage.MultiStockComparision import *
from collections import defaultdict


stock_company_list = ['c','AAPL','C']
amount_list = [30,20,20]
start_date = "2011/11/21"
end_date = "2012/3/21"

def merge_same_stock(stock_company_list, amount_list):
    trade_amount_list = []
    for item in amount_list:
        if IsValidNum(item):
            trade_amount_list.append(ParseValidNum(item)) #get validated trade amount list
    
    dictionary = dict(zip(stock_company_list, trade_amount_list)) #add the trade amount together if two stocks are the same.
    new_dictionary = defaultdict(int)
    for stock, amount in dictionary.iteritems():
        new_dictionary[stock.upper()] += amount
    
    unique_stock_company_list = new_dictionary.keys() #get a list of unique stock names
    trade_amount = new_dictionary.values() #get a list of trade amount corresponding to the stock names.
    return unique_stock_company_list, trade_amount


def portfolio_analysis(stock_company_list, start_date, end_date, amount_list):
    """
    Take a list of stock companies, date range and trade amount of each stock,
    return a dataframe showing each stock and total portfolio performance
    """
    stock_company_list, amount_list = merge_same_stock(stock_company_list, amount_list)
    stock_class_dict = {stock:Stock(stock,start_date,end_date) for stock in stock_company_list} #get validated stocks list
    
    pricecols = {stock:stock_class.close_price for stock, stock_class in stock_class_dict.iteritems()}
    closed_price_df = pd.DataFrame(data=pricecols, columns=stock_company_list)
    portfolio = portfolio_stock_amount(closed_price_df,amount_list)
    portfolio_add_sum = add_sum (portfolio)
    line_plot(portfolio_add_sum["Sum"])
    #return portfolio_add_sum

#portfolio performance within the date range, return a number
#stocks_return(portfolio_add_sum['Sum'])

#boxplot of each stock performance
#box_plot(portfolio_add_sum[:-1])

#line plot showing the stock performance
#line_plot(portfolio_add_sum[:-1])

#scatter matrix
#scatter_matrix(portfolio_add_sum[:-1])

# heat map
#heat_map(portfolio_add_sum[:-1])

# risk and return
#risk_vs_return(portfolio_add_sum[:-1])
    
#moving average, allow the user to choose a number of days, plot a graph comparing the portfolio performance with the moving average price
#moving_avg(portfolio_add_sum,Num)