import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from StockClass import *
from DataProcessing import *
from StockAnalysis import *

stock_company_list = ['IBM','AAPL','C']
amount_list = [10,20,20]
start_date = pd.datetime(2011,11,21)
end_date = pd.datetime(2012,3,21)

def portfolio_analysis(stock_company_list, amount_list, start_date, end_date):   
    stock_class_list = {stock: Stock(stock,start_date,end_date) for stock in stock_company_list}
    pricecols = {stock:stock_class.closeprice for stock,stock_class in stock_class_list.iteritems()}
    closed_price_df = pd.DataFrame(pricecols)
    portfolio = add_sum (closed_price_df)
    portfolio_percentage_change = percentage_change(portfolio)
    #print "The portfolio performance is:"
    #print stocks_return(portfolio)
    line_plot(portfolio_percentage_change['Sum'])

#portfolio_analysis(stock_company_list, amount_list, start_date, end_date)
    

