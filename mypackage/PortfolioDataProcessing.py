import pandas as pd
import matplotlib.pyplot as plt

#trade_amount = [10,10,20,20] #choose the trade amount for each stock
def portfolio_stock_amount(df,trade_amount):
    '''Multiply the stock price by the corresponding amount'''
    new_df = df.mul(trade_amount, axis=1)
    return new_df

def normalized_data(df):
    '''Normalize the data'''
    normprice = df - df.mean()
    normprice = normprice / normprice.std()
    return normprice 


def add_sum(df):
    '''create a new dataframe that adds the portfolio price each day'''
    new_df= df.copy()
    new_df['Sum']= df.sum(1) #sum of the portfolio each day
    return new_df


def portfolio_weight(df):
    '''Calculate the weight of each stock in the portfolio each day'''
    new_df = df.div(df['Sum'], axis='index')
    return new_df


def percentage_change(df):
    '''Calculate the return of the stock/portfolio each day'''
    new_df = df.pct_change()
    return new_df