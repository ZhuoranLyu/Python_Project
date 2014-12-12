'''
Created on 2014.12.1

@author: Zhuoran Lyu, Fangyun Sun
'''

from Tkinter import *
import ttk
import ClassPackage.StockClass as SC
import pandas as pd
import datetime
import tkMessageBox
import PortfolioPackage.PortfolioClass as PC
import Utilities.CheckInternet as CI
from Utilities.Exceptions import *


class PortfolioAnalysisWindow:
	'''
	Create a class to generate a window to make the portfolio analysis.
	'''
	def __init__(self, master):
	
		self.master = master
		self.frame = ttk.Frame(self.master,padding="4 6 160 60")
		self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)

		stock_one_name = StringVar()
		stock_one_name.set("IBM")
		stock_two_name = StringVar()
		stock_two_name.set("AAPL")
		stock_three_name = StringVar()
		stock_three_name.set("C")
		stock_four_name = StringVar()
		stock_four_name.set("F")

		stock_one_amount = StringVar()
		stock_two_amount = StringVar()
		stock_three_amount = StringVar()
		stock_four_amount = StringVar()

		stock_one_amount.set('20')
		stock_two_amount.set('10')
		stock_three_amount.set('20')
		stock_four_amount.set('20')

		start_date = StringVar()
		start_date.set("2010/1/1")
		end_date = StringVar()
		end_date.set('2010/5/1')

		self.figure_type = StringVar()
		self.figure_type.set('portfolio performance')
		self.analysis_type = StringVar()
		self.analysis_type.set('statistics of the portfolio')

		self.stock_one_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_one_name)
		self.stock_one_name_entry.grid(column=2, row=1, sticky=(W, E))

		self.stock_two_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_two_name)
		self.stock_two_name_entry.grid(column=2, row=2, sticky=(W, E))

		self.stock_three_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_three_name)
		self.stock_three_name_entry.grid(column=2, row=3, sticky=(W, E))

		self.stock_four_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_four_name)
		self.stock_four_name_entry.grid(column=2, row=4, sticky=(W, E))


		self.stock_one_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_one_amount)
		self.stock_one_amount_entry.grid(column=4, row=1, sticky=(W, E))

		self.stock_two_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_two_amount)
		self.stock_two_amount_entry.grid(column=4, row=2, sticky=(W, E))

		self.stock_three_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_three_amount)
		self.stock_three_amount_entry.grid(column=4, row=3, sticky=(W, E))

		self.stock_four_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_four_amount)
		self.stock_four_amount_entry.grid(column=4, row=4, sticky=(W, E))

		self.start_date_entry = ttk.Entry(self.frame, width=7, textvariable=start_date)
		self.start_date_entry.grid(column=6, row=1, sticky=(W, E))

		self.end_date_entry = ttk.Entry(self.frame, width=7, textvariable=end_date)
		self.end_date_entry.grid(column=6, row=2, sticky=(W, E))

		ttk.Label(self.frame, text="please enter the first stock name").grid(column=1, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the second stock name").grid(column=1, row=2, sticky=W)
		ttk.Label(self.frame, text="please enter the third stock name").grid(column=1, row=3, sticky=W)
		ttk.Label(self.frame, text="please enter the fourth stock name").grid(column=1, row=4, sticky=W)

		ttk.Label(self.frame, text="please enter the first stock amount").grid(column=3, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the second stock amount").grid(column=3, row=2, sticky=W)
		ttk.Label(self.frame, text="please enter the third stock amount").grid(column=3, row=3, sticky=W)
		ttk.Label(self.frame, text="please enter the fourth stock amount").grid(column=3, row=4, sticky=W)


		ttk.Label(self.frame, text="please enter the start date").grid(column=5, row=1, sticky=W)
		ttk.Label(self.frame, text="please enter the start date").grid(column=5, row=2, sticky=W)

		plots = ('portfolio performance', 'portfolio performance with market', 'expected return V.S. risk of stocks', 'Heat map of your portfolio stocks','moving average V.S. portfolio daily price')
		box1 = ttk.Combobox(self.frame, values = plots, state = 'readonly', textvariable = self.figure_type, width = 30).grid(column=5, row=4, sticky=W)

		ttk.Button(self.frame, text="Plot", command=lambda: self.plot\
			([stock_one_name.get(), stock_two_name.get(), stock_three_name.get(), stock_four_name.get()], \
				[stock_one_amount.get(), stock_two_amount.get(), stock_three_amount.get(), stock_four_amount.get()],\
				start_date.get(), end_date.get())).grid(column=6, row=4, sticky=W)

		stat = ('statistics of the portfolio', 'correlation of the stocks changes')
		box2 = ttk.Combobox(self.frame, values = stat, state = 'readonly', textvariable = self.analysis_type, width = 30).grid(column=5, row=3, sticky=W)

		ttk.Button(self.frame, text="Analysis", command=lambda: self.analysis\
			([stock_one_name.get(), stock_two_name.get(), stock_three_name.get(), stock_four_name.get()], \
				[stock_one_amount.get(), stock_two_amount.get(), stock_three_amount.get(), stock_four_amount.get()],\
				start_date.get(), end_date.get())).grid(column=6, row=3, sticky=W)

		ttk.Button(self.frame, text="Clear", command=self.clear_entry).grid(column=7, row=1, sticky=N)


		for child in self.frame.winfo_children(): 
			child.grid_configure(padx=10, pady=10)

		self.stock_one_name_entry.focus()


	def clear_entry(self):
		try:
			self.stock_one_name_entry.delete(0, END)
			self.stock_two_name_entry.delete(0, END)
			self.stock_three_name_entry.delete(0, END)
			self.stock_four_name_entry.delete(0, END)
			
			self.stock_one_amount_entry.delete(0,END)
			self.stock_two_amount_entry.delete(0,END)
			self.stock_three_amount_entry.delete(0,END)
			self.stock_four_amount_entry.delete(0,END)

			self.start_date_entry.delete(0, END)
			self.end_date_entry.delete(0, END)
			self.label1.destroy()
			self.label2.destroy()
			self.label3.destroy()
			self.label4.destroy()
		except:
			pass

	def plot(self, stock_list, amount_list, start_date, end_date):
		try:
			CI.IsInternetOn()
			portfolio = PC.Portfolio(stock_list, start_date, end_date, amount_list)
			if self.figure_type.get() == 'portfolio performance':
				portfolio.plot_portfolio()
			elif self.figure_type.get() == 'portfolio performance with market':
				portfolio.portfolio_value_change_compared_with_market()
			elif self.figure_type.get() == 'expected return V.S. risk of stocks':
				portfolio.return_vs_risk()
			elif self.figure_type.get() == 'moving average V.S. portfolio daily price':
				portfolio.moving_avg_50()
			else:
				portfolio.heat_map()

		except (StockNameInputException,DateInputException,EmptyInputException,ConnectInternetException,DateRangeException, TradeAmountException,EmptyPortfolioException) as error:
			tkMessageBox.showinfo(message=error)
		except:
			tkMessageBox.showinfo(message='Please restart the application, sorry about that!')


	def analysis(self, stock_list, amount_list, start_date, end_date):
		try:
			CI.IsInternetOn()
			portfolio = PC.Portfolio(stock_list, start_date, end_date, amount_list)

			if self.analysis_type.get() == 'statistics of the portfolio':
				try:
					self.label1.destroy()
					self.label2.destroy()
					self.label3.destroy()
					self.label4.destroy()
				except:
					pass
				self.label1 = ttk.Label(self.frame, text="Statistics of the portfolio.")
				self.label1.grid(column=1, row=5, sticky=W)
				text = portfolio.describe_portfolio()
				self.label2 = ttk.Label(self.frame, text=text)
				self.label2.grid(column=1, row=6, sticky=W)
			else:
				try:
					self.label1.destroy()
					self.label2.destroy()
					self.label3.destroy()
					self.label4.destroy()
				except:
					pass
				self.label3 = ttk.Label(self.frame, text="Correlation of the stocks changes.")
				self.label3.grid(column=1, row=5, sticky=W)
				self.label4 = ttk.Label(self.frame, text=portfolio.stocks_value_change_corr())
				self.label4.grid(column=1, row=6, sticky=W)

		except (StockNameInputException,DateInputException,EmptyInputException,ConnectInternetException,DateRangeException, TradeAmountException, EmptyPortfolioException) as error:
			tkMessageBox.showinfo(message=error)
		except:
			tkMessageBox.showinfo(message='Please restart the application, sorry about that!')