from Tkinter import *
import ttk
import tkMessageBox
import mypackage.StockClass as SC
import pandas as pd
import datetime
import mypackage.Check_Internet as CI
from mypackage.Exceptions import *

class SingleStockWindow:
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

		stock_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_name)
		stock_name_entry.grid(column=2, row=1, sticky=(W, E))

		start_date_entry = ttk.Entry(self.frame, width=7, textvariable=start_date)
		start_date_entry.grid(column=2, row=2, sticky=(W, E))

		end_date_entry = ttk.Entry(self.frame, width=7, textvariable=end_date)
		end_date_entry.grid(column=2, row=3, sticky=(W, E))

		ttk.Button(self.frame, text="Plot", command=lambda: self.plot(stock_name.get(), start_date.get(), end_date.get())).grid(column=2, row=4, sticky=W)

		ttk.Label(self.frame, text="please enter the stock name").grid(column=1, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the start date").grid(column=1, row=2, sticky=W)
		ttk.Label(self.frame, text="please enter the start date").grid(column=1, row=3, sticky=W)

		for child in self.frame.winfo_children(): 
			child.grid_configure(padx=10, pady=10)

		stock_name_entry.focus()


	def plot(self, stock_name, start_date, end_date):
		try:
			CI.IsInternetOn()
			stock = SC.Stock(stock_name, start_date, end_date)
			stock.plot_close_price()
		except (StockNameInputException,DateInputException,EmptyInputException,ConnectInternetException,DateRangeException) as error:
			tkMessageBox.showinfo(message=error)
		except:
			tkMessageBox.showinfo(message='Please restart the application, sorry about that!')

