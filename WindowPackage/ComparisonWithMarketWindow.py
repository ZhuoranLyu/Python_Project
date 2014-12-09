'''
Created on 2014.12.1

@author: Zhuoran Lyu
'''
from Tkinter import *
import ttk
import tkMessageBox
import ClassPackage.StockClass as SC
import pandas as pd
import datetime
import Utilities.CheckInternet as CI
from Utilities.Exceptions import *

class ComparisonWithMarketWindow:
	'''
	Create a class to generate a window to plot a stock close price with market price.
	'''
	def __init__(self, master):
	
		self.master = master
		self.frame = ttk.Frame(self.master,padding="4 4 50 50")
		self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)

		stock_name = StringVar()
		stock_name.set("IBM")
		start_date = StringVar()
		start_date.set("2010/1/1")
		end_date = StringVar()
		end_date.set("2010/5/1")

		self.stock_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_name)
		self.stock_name_entry.grid(column=2, row=1, sticky=(W, E))

		self.start_date_entry = ttk.Entry(self.frame, width=7, textvariable=start_date)
		self.start_date_entry.grid(column=2, row=2, sticky=(W, E))

		self.end_date_entry = ttk.Entry(self.frame, width=7, textvariable=end_date)
		self.end_date_entry.grid(column=2, row=3, sticky=(W, E))

		ttk.Button(self.frame, text="Analysis", command=lambda: self.plot(stock_name.get(), start_date.get(), end_date.get())).grid(column=1, row=4, sticky=W)
		ttk.Button(self.frame, text="Clear", command=self.clear_entry).grid(column=2, row=4, sticky=W)


		ttk.Label(self.frame, text="please enter the stock symbol").grid(column=1, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the start date").grid(column=1, row=2, sticky=W)
		ttk.Label(self.frame, text="please enter the start date").grid(column=1, row=3, sticky=W)

		ttk.Label(self.frame, text="e.g: 'AAPL'").grid(column=3, row=1, sticky=W)
		ttk.Label(self.frame, text="e.g: '2010/1/1'").grid(column=3, row=2, sticky=W)
		ttk.Label(self.frame, text="e.g: '2010/5/1'").grid(column=3, row=3, sticky=W)


		for child in self.frame.winfo_children(): 
			child.grid_configure(padx=10, pady=10)

		self.stock_name_entry.focus()

	def clear_entry(self):
		self.stock_name_entry.delete(0, END)
		self.start_date_entry.delete(0, END)
		self.end_date_entry.delete(0, END)


	def plot(self, stock_name, start_date, end_date):
		try:
			CI.IsInternetOn()
			stock = SC.Stock(stock_name, start_date, end_date)
			stock.plot_changeprice_comparison()
		except (StockNameInputException,DateInputException,EmptyInputException,ConnectInternetException,DateRangeException) as error:
			tkMessageBox.showinfo(message=error)
		except:
			tkMessageBox.showinfo(message='Please restart the application, sorry about that!')
