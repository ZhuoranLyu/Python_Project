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
		self.analysis_type = StringVar()

		stock_one_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_one_name)
		stock_one_name_entry.grid(column=2, row=1, sticky=(W, E))

		stock_two_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_two_name)
		stock_two_name_entry.grid(column=2, row=2, sticky=(W, E))

		stock_three_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_three_name)
		stock_three_name_entry.grid(column=2, row=3, sticky=(W, E))

		stock_four_name_entry = ttk.Entry(self.frame, width=7, textvariable=stock_four_name)
		stock_four_name_entry.grid(column=2, row=4, sticky=(W, E))


		stock_one_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_one_amount)
		stock_one_amount_entry.grid(column=4, row=1, sticky=(W, E))

		stock_two_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_two_amount)
		stock_two_amount_entry.grid(column=4, row=2, sticky=(W, E))

		stock_three_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_three_amount)
		stock_three_amount_entry.grid(column=4, row=3, sticky=(W, E))

		stock_four_amount_entry = ttk.Entry(self.frame, width=7, textvariable=stock_four_amount)
		stock_four_amount_entry.grid(column=4, row=4, sticky=(W, E))

		start_date_entry = ttk.Entry(self.frame, width=7, textvariable=start_date)
		start_date_entry.grid(column=6, row=1, sticky=(W, E))

		end_date_entry = ttk.Entry(self.frame, width=7, textvariable=end_date)
		end_date_entry.grid(column=6, row=2, sticky=(W, E))

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

		plots = ('portfolio performance', 'portfolio performance with market', 'risk and return of each stock position', 'Heat map of your portfolio stocks')
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


		for child in self.frame.winfo_children(): 
			child.grid_configure(padx=10, pady=10)

		stock_one_name_entry.focus()


	def plot(self, stock_list, amount_list, start_date, end_date):
		try:
			CI.IsInternetOn()
			portfolio = PC.Portfolio(stock_list, start_date, end_date, amount_list)
			if self.figure_type.get() == 'portfolio performance':
				portfolio.plot_portfolio()
			elif self.figure_type.get() == 'portfolio performance with market':
				portfolio.portfolio_value_change_compared_with_market()
			elif self.figure_type.get() == 'risk and return of each stock position':
				portfolio.risk_vs_return()
			else:
				portfolio.heat_map()

		except (StockNameInputException,DateInputException,EmptyInputException,ConnectInternetException,DateRangeException, TradeAmountException) as error:
			tkMessageBox.showinfo(message=error)
		except:
			tkMessageBox.showinfo(message='Please restart the application, sorry about that!')


	def analysis(self, stock_list, amount_list, start_date, end_date):
		try:
			CI.IsInternetOn()
			portfolio = PC.Portfolio(stock_list, start_date, end_date, amount_list)
			try:
				label1.destroy()
				label2.destroy()
			except:
				pass
				
			if self.analysis_type.get() == 'statistics of the portfolio':
				label1 = ttk.Label(self.frame, text="Statistics of the portfolio.").grid(column=1, row=5, sticky=W)
				label2 = ttk.Label(self.frame, text=portfolio.describe_portfolio()).grid(column=1, row=6, sticky=W)
			else:
				label1 = ttk.Label(self.frame, text="Correlation of the stocks changes.").grid(column=1, row=5, sticky=W)
				label2 = ttk.Label(self.frame, text=portfolio.stocks_value_change_corr()).grid(column=1, row=6, sticky=W)

		except (StockNameInputException,DateInputException,EmptyInputException,ConnectInternetException,DateRangeException, TradeAmountException) as error:
			tkMessageBox.showinfo(message=error)
		except:
			tkMessageBox.showinfo(message='Please restart the application, sorry about that!')