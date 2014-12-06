import pandas as pd
import matplotlib.pyplot as plt


def describe_portfolio(df):
    '''Get descriptic statistics of the stocks'''
    return df.describe()


def stock_corr(df):
    '''Get stocks correlation'''
    return df.corr()

def stocks_return(df):
    '''return the performance of the portfolio'''
    return df.ix[-1] / df.ix[0] -1


def line_plot(df):
    '''plot a gragh showing the performance of the portfolio'''
    plt.figure()
    df.plot(kind='line')
    plt.ylabel('Price')
    plt.title('Portfolio performance')
    plt.legend()
    plt.show()


def box_plot(df):
    '''plot a boxplot showing the performance of each stock'''
    plt.figure()
    df.boxplot()
    plt.ylabel('Price')
    plt.title('Boxplot for performance of each stock')
    plt.legend()
    plt.show()
    

#single scatterplot of two stocks
def two_stock_scatterplot(df, stock1, stock2):
    ''' Plot a scatterplot of two stock to see their correlation'''
    #daily_rets = percentage_change(df)
    plt.figure()
    plt.scatter(daily_rets.stock1, daily_rets.stock2, color = 'b', alpha = 0.8)
    plt.title('Scatterplot of the selected stocks')
    plt.show()


def scatter_matrix(df):
    '''create a scatter matrix to examine the correlation among stocks'''
    #daily_rets = percentage_change(df)
    plt.figure()
    pd.scatter_matrix(daily_rets, figsize=(15, 15))
    plt.title('Scatter matrix of your portfolio')
    plt.show()


def heat_map(df):
    '''create a heat map to see the correlation among stocks'''
    stocks_corr = stocks_corr(df)
    plt.imshow(stocks_corr, cmap='Blues', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(stocks_corr)), stocks_corr.columns)
    plt.yticks(range(len(stocks_corr)), stocks_corr.columns)
    plt.title('Heat map of your portfolio stocks')
    plt.show()


def risk_vs_return(df):
    '''create a plot to examine the risk and return tradeoff'''
    #daily_return = percentage_change(df)
    plt.figure()
    plt.scatter(daily_rets.mean(),daily_rets.std())
    plt.xlabel('Expected Return')
    plt.ylabel('Risk')
    for label, x, y in zip(daily_rets.columns, daily_rets.mean(), daily_rets.std()):
        plt.annotate(label, xy = (x, y),xytext = (10, 10),
                     textcoords = 'offset points', 
                     horizontalalignment = 'right', verticalalignment = 'down', 
                     bbox = dict(boxstyle = 'round,pad=0.2', facecolor='red', alpha = 0.2), 
                     arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3'))
    plt.title('Risk and Return of each stock position')
    plt.show()


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
    plt.title('Moving average of {} days V.S. portfolio price'. format(Num))
    plt.lengend()
    plt.show()

