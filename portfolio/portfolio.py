
# coding: utf-8

# In[365]:

import pandas.io.data as web
import pandas as pd
import datetime
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import pandas as pd
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2014, 1, 27)


# In[210]:

'''get the data online'''
tickers = ['AMZN', 'BP', 'C', 'COF']
#for ticker in tickers:
portfolio_stock_price = web.get_data_yahoo(tickers, start, end)['Adj Close']
portfolio_stock_price.head()


# In[245]:

def describe_stocks(df):
    '''Get descriptic statistics of the stocks'''
    return df.describe()


# In[215]:

def stock_corr(df):
    '''Get stocks correlation'''
    return df.corr()


# In[211]:

trade_amount = [10,10,20,20] #choose the trade amount for each stock


# In[242]:

def portfolio_stock_amount(df,trade_amount):
    '''Mutiply the stock price by the corresponding amount'''
    new_df = df.mul(trade_amount, axis=1)
    return new_df


# In[217]:

def normalized_data(df):
    '''Normalize the data'''
    normprice = df - df.mean()
    normprice = normprice / normprice.std()
    return normprice 


# In[218]:

def add_sum(df):
    '''create a new dataframe that adds the portfolio price each day'''
    new_df= df.copy()
    new_df['Sum']= df.sum(1) #sum of the portfolio each day
    return new_df


# In[275]:

def portfolio_weight(df):
    '''Calculate the weight of each stock in the portfolio each day'''
    new_df = df.div(df['Sum'], axis='index')
    return new_df


# In[276]:

def percentage_change(df):
    '''Caculate the return of the stock/portfolio each day'''
    new_df = df.pct_change()
    return new_df


# In[226]:

#single scatterplot of two stocks
def two_stock_scatterplot(df, stock1, stock2):
    ''' Plot a scatterplot of two stock to see their correlation'''
    daily_rets = percentage_change(df)
    plt.scatter(daily_rets.stock1, daily_rets.stock2, color = 'b', alpha = 0.8)


# In[227]:

def scatter_matrix(df):
    '''create a scatter matrix to examine the correlation among stocks'''
    daily_rets = percentage_change(df)
    pd.scatter_matrix(daily_rets, figsize=(15, 15))


# In[228]:

def heat_map(df):
    '''create a heat map to see the correlation among stocks'''
    stocks_corr = stocks_corr(df)
    plt.imshow(stocks_corr, cmap='Blues', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(stocks_corr)), stocks_corr.columns)
    plt.yticks(range(len(stocks_corr)), stocks_corr.columns)


# In[229]:

def risk_vs_return(df):
    '''create a plot to examine the risk and return tradeoff'''
    daily_return = percentage_change(df)
    plt.scatter(daily_rets.mean(),daily_rets.std())
    plt.xlabel('Expected Return')
    plt.ylabel('Risk')
    for label, x, y in zip(daily_rets.columns, daily_rets.mean(), daily_rets.std()):
        plt.annotate(label, xy = (x, y),xytext = (10, 10),
                     textcoords = 'offset points', 
                     horizontalalignment = 'right', verticalalignment = 'down', 
                     bbox = dict(boxstyle = 'round,pad=0.2', facecolor='red', alpha = 0.2), 
                     arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3'))


# In[306]:

#[20,50,200]
# 50 days moving average
def moving_avg(df,Num):
    '''Allow the user to choose moving average of 20,50 or 200 days, 
    plot a graph comparing the moving average price with the portfolio daily price'''
    moving_average = pd.rolling_mean(df['Sum'],Num,min_periods=Num)
    #df['Moving Average'] = moving_average
    plt.figure(figsize=(12,12))
    plt.plot(df.index,moving_average)
    plt.plot(df.index,df['Sum'])
    plt.ylabel('Price')


# In[344]:

#box plot
df = portfolio_stock_amount(portfolio_stock_price,trade_amount)

def line_plot(df):
    df.plot(kind='line')
    plt.ylabel('Price')


# In[303]:

normal = normalized_data(df)
normal.plot(kind='line')
plt.ylabel('Normalized Close Price')


# In[372]:

perdf = percentage_change(df)
#perdf.plot(kind='line',figsize=(19,8))


# In[347]:

def box_plot(df):
    plt.figure()
    df.boxplot()


# In[374]:

def stocks_return(df):
    return df.ix[-1] / df.ix[0] -1


# In[ ]:



