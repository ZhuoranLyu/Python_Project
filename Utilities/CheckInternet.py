'''
Created on 2014.12.1

@author: Fangyun Sun
'''

import requests
from Exceptions import *

def IsInternetOn():
    """
    Check whether the Internet is connected. We need to obtain data from yahoo finance through the Internet.
    74.125.228.100 is one of the IP-addresses for google.com.
    """
    try:
        _ = requests.get('http://www.google.com/', timeout=5)
        return True
    except requests.ConnectionError: 
        raise ConnectInternetException()
    return False

if __name__ == '__main__':
    print IsInternetOn()