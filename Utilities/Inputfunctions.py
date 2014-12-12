'''
Created on 2014.12.1

@author: Fangyun Sun, Yunshi Li
'''
import re
import pandas.io.data as web
import datetime
from Exceptions import *

def IsValidStockName(stock_name):
    """
    Check whether the input is a valid stock name.
    """
    if isinstance(stock_name, str):
        #Check whether input of list has a valid form
        try:
            df =web.DataReader(stock_name,'yahoo')

        except:
            return False
        else:
            return True
    else:
        return False
def ParseStockName(stock_name):
    """
    Parse stock name when the input is a valid stock name.
    """
    if IsValidStockName(stock_name):
        return stock_name

def IsValidDate(date_string):
    """
    Check whether the input is a valid date.
    """
    if isinstance(date_string, str):
        #Check whether input of list has a valid form
        try:
            datetime.datetime.strptime(date_string, '%Y/%m/%d')
            return True
        except ValueError:
            return False
    else:
        return False

def ParseDate(date_string):
    """
    Parse when the input is a valid date.
    """
    if IsValidDate(date_string):
        return datetime.datetime.strptime(date_string, '%Y/%m/%d')
        

def IsEmptyInput(stock_name,start_date,end_date):
    """
    Check whether the input is null or not.
    """
    if stock_name == '' or start_date == '' or end_date == '':
        return True
    else:
        return False

def IsValidDateRange(start, end):
    """
    Check whether the end_date is more than start_date
    """
    start_date = ParseDate(start)
    end_date = ParseDate(end)
    if end_date > start_date:
        return True
    else:
        return False



def IsValidNum(num_string):
    """
    Check whether the trade amount is positive integer.
    """
    try:
        num = int(num_string)
    except:
        return False
    if num < 0:
        return False
    else:
        return True

def ParseValidNum(num_string):
    """
    Parse when the trade amount input is valid.
    """
    if IsValidNum(num_string):
        return int(num_string)
    else:
        raise TradeAmountException()       

def IsEmptyPortfolio(dictionary):
    """
    Check whether the portfolio is empty.
    """
    if dictionary == {}:
        return True
    else:
        return False


#print IsValidStockName('cba')