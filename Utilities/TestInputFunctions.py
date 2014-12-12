'''
Created on Dec 8, 2014

@author: Yunshi Li
'''
import unittest
from Utilities.Inputfunctions import *
from Utilities.Exceptions import *

class TestUtilitiesInputFunctionsIsValidStockName(unittest.TestCase):
    """
    Test the IsValidStockName functions in Utilities package.
    """

    def setUp(self):
        """
        set up the test data
        """
        self.stock1 = "IBM"
        self.stock2 = "C"
        self.stock3 = "huabanxie"
        self.stock4 = "TkNIMEI"

    def tearDown(self):
        print "test stock names."


    def testValidStockName(self):
        """
        Test if the stock names are valid.
        """
        self.assertTrue(IsValidStockName(self.stock1))
        self.assertTrue(IsValidStockName(self.stock2))
        
    def testInvalidStockName(self):
        
        """
        Test if the stock names are invalid.
        """
        self.assertFalse(IsValidStockName(self.stock3))
        self.assertFalse(IsValidStockName(self.stock4))


class TestUtilitiesInputFunctionsIsValidDate(unittest.TestCase):
    """
    Test the IsValidDate functions in Utilities package.
    """

    def setUp(self):
        """
        set up the test data.
        """
        self.date1 = "2011/12/11"
        self.date2 = "2014/2/2"
        #self.date3 = "2015/1/2"
        self.date4 = "2013/13/2"
        self.date5 = "MoMoDa"

    def tearDown(self):
        print "test dates."


    def testValidDate(self):
        """
        Test if the dates are valid.
        """
        self.assertTrue(IsValidDate(self.date1))
        self.assertTrue(IsValidDate(self.date2))
        
    def testInvalidDate(self):
        
        """
        Test if the dates are invalid.
        """
        #self.assertFalse(IsValidDate(self.date3))
        self.assertFalse(IsValidDate(self.date4))
        self.assertFalse(IsValidDate(self.date5))


class TestUtilitiesInputFunctionsIsEmptyInput(unittest.TestCase):
    """
    Test the IsEmptyInput functions in Utilities package.
    """

    def setUp(self):
        """
        set up the test data.
        """
        self.input1 = ""
        self.input2 = "F"
        self.input3 = "2011/12/11"
        self.input4 = "2012/12/11"

    def tearDown(self):
        print "test empty inputs."


    def testEmptyInput(self):
        """
        Test if at lest one input is empty.
        """
        self.assertTrue(IsEmptyInput(self.input1, self.input2, self.input3))
        self.assertTrue(IsEmptyInput(self.input1, self.input1, self.input3))
        self.assertTrue(IsEmptyInput(self.input1, self.input1, self.input1))
        
    def testNotEmptyInput(self):
        
        """
        Test if no inputs are empty.
        """
        self.assertFalse(IsEmptyInput(self.input2,self.input3,self.input4))


class TestUtilitiesInputFunctionsIsValidDateRange(unittest.TestCase):
    """
    Test the IsValidDateRange functions in Utilities package.
    """

    def setUp(self):
        """
        set up the test data.
        """
        self.date1 = "2011/12/11"
        self.date2 = "2014/2/2"


    def tearDown(self):
        print "test date range."


    def testValidDateRange(self):
        """
        Test if the date range is valid.
        """
        self.assertTrue(IsValidDateRange(self.date1,self.date2))

        
    def testInvalidDateRange(self):
        
        """
        Test if the date range is invalid.
        """
        self.assertFalse(IsValidDateRange(self.date2,self.date1))


class TestUtilitiesInputFunctionsIsValidNum(unittest.TestCase):
    """
    Test the IsValidNum functions in Utilities package.
    """

    def setUp(self):
        """
        set up the test data
        """
        self.num1 = "2"
        self.num2 = "4"
        self.num3 = "huabanxie"
        self.num4 = "C"

    def tearDown(self):
        print "test numbers."


    def testValidNum(self):
        """
        Test if the numbers are valid.
        """
        self.assertTrue(IsValidNum(self.num1))
        self.assertTrue(IsValidNum(self.num2))
        
    def testInvalidNum(self):
        
        """
        Test if the stock names are invalid.
        """
        self.assertFalse(IsValidNum(self.num3))
        self.assertFalse(IsValidNum(self.num4))
  
        
class TestUtilitiesInputFunctionsParseValidNum(unittest.TestCase):
    """
    Test the IsValidNum functions in Utilities package.
    """

    def setUp(self):
        """
        set up the test data
        """
        self.num1 = "2"
        self.num2 = "4"
        self.num3 = "huabanxie"
        self.num4 = "C"

    def tearDown(self):
        print "parse numbers."


    def testParseValidNum(self):
        """
        Parse the valid numbers.
        """
        self.assertEqual(ParseValidNum(self.num1),2)
        self.assertEqual(ParseValidNum(self.num2),4)
        
    def testInvalidNum(self):
        
        """
        raise exceptions for the invalid numbers.
        """
        self.assertRaises(TradeAmountException,ParseValidNum, self.num3)
        self.assertRaises(TradeAmountException,ParseValidNum, self.num4)


class TestUtilitiesInputFunctionsIsEmptyPortfolio(unittest.TestCase):
    """
    Test the IsEmptyPortfolio functions in Utilities package.
    """

    def setUp(self):
        """
        set up the test data
        """
        self.dict1 = {2:3}
        self.dict2 = {"C":3}
        self.dict3 = {}
        self.dict4 = {"c":""}

    def tearDown(self):
        print "test empty dictionary."


    def testEmptyPortfolio(self):
        """
        test empty dictionary
        """
        self.assertTrue(IsEmptyPortfolio(self.dict3))
        
    def testNotAllEmptyportfolio(self):
        
        """
        test dictionaries that are not empty
        """
        self.assertFalse(IsEmptyPortfolio(self.dict1))
        self.assertFalse(IsEmptyPortfolio(self.dict2))
        self.assertFalse(IsEmptyPortfolio(self.dict4))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()