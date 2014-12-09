'''
Created on 2014.12.1

@author: Zhuoran Lyu
'''

from Tkinter import *
import ttk
import ClassPackage.StockClass as SC
import StocksPackage.MultiStockComparision as MSC
import pandas as pd
import datetime
import Utilities.CheckInternet as CI
from Utilities.Exceptions import *
import tkMessageBox

class MultiStocksWindow:
	'''
	Create a class to generate a window to plot the close prices of several stocks.
	'''
	def __init__(self, master):
	
		self.master = master
		self.frame = ttk.Frame(self.master,padding="6 4 100 80")
		self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)

		stock_one_name = StringVar()
		stock_two_name = StringVar()
		stock_three_name = StringVar()
		stock_four_name = StringVar()
		start_date = StringVar()
		end_date = StringVar()

		self.stock_one_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_one_name)
		self.stock_one_name_entry.grid(column=2, row=1, sticky=(W, E))

		self.stock_two_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_two_name)
		self.stock_two_name_entry.grid(column=2, row=2, sticky=(W, E))

		self.stock_three_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_three_name)
		self.stock_three_name_entry.grid(column=2, row=3, sticky=(W, E))

		self.stock_four_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_four_name)
		self.stock_four_name_entry.grid(column=2, row=4, sticky=(W, E))

		self.start_date_entry = ttk.Entry(self.frame, width=7, textvariable=start_date)
		self.start_date_entry.grid(column=4, row=1, sticky=(W, E))

		self.end_date_entry = ttk.Entry(self.frame, width=7, textvariable=end_date)
		self.end_date_entry.grid(column=4, row=2, sticky=(W, E))

		ttk.Label(self.frame, text="please enter the first stock symbol").grid(column=1, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the second stock symbol").grid(column=1, row=2, sticky=W)
		ttk.Label(self.frame, text="please enter the third stock symbol").grid(column=1, row=3, sticky=W)
		ttk.Label(self.frame, text="please enter the fourth stock symbol").grid(column=1, row=4, sticky=W)

		ttk.Label(self.frame, text="please enter the start date").grid(column=3, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the start date").grid(column=3, row=2, sticky=W)
		
		ttk.Label(self.frame, text="stock symbol e.g: 'AAPL'").grid(column=2, row=5, sticky=W)
		ttk.Label(self.frame, text="date e.g: '2010/1/1'").grid(column=4, row=3, sticky=W)

		ttk.Button(self.frame, text="Plot", command=lambda: self.plot\
			([stock_one_name.get(), stock_two_name.get(), stock_three_name.get(), stock_four_name.get()], \
				start_date.get(), end_date.get())).grid(column=3, row=6,sticky=N)
		ttk.Button(self.frame, text="Clear", command=self.clear_entry).grid(column=4, row=6, sticky=N)


		for child in self.frame.winfo_children(): 
			child.grid_configure(padx=10, pady=10)

		self.stock_one_name_entry.focus()
	
	def clear_entry(self):
		self.stock_one_name_entry.delete(0, END)
		self.stock_two_name_entry.delete(0, END)
		self.stock_three_name_entry.delete(0, END)
		self.stock_four_name_entry.delete(0, END)
		self.start_date_entry.delete(0, END)
		self.end_date_entry.delete(0, END)
		
	def plot(self, stock_list, start_date, end_date):
		try:
			CI.IsInternetOn()
			MSC.multistocks_percentchange(stock_list, start_date, end_date)
		except (StockNameInputException,DateInputException,EmptyInputException,ConnectInternetException,DateRangeException) as error:
			tkMessageBox.showinfo(message=error)
		except:
			tkMessageBox.showinfo(message='Please restart the application, sorry about that!')
		
      

