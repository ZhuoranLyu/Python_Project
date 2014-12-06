from Tkinter import *
import ttk
import SingleStockWindow as SSW
import ComparisonWithMarketWindow as CWMW
import MultiStocksWindow as MSW
import PortfolioAnalysisWindow as PAW
import tkMessageBox
from PIL import Image, ImageTk

class MainWindow:
	  
	def __init__(self, master):
		self.master = master
		self.frame = ttk.Frame(self.master, padding="3 2 120 100")
		self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)
		
		#image = ImageTk.PhotoImage(Image.open('/home/zhuoran/Desktop/1.jpg'))
		#ttk.Label(master, image=image)

		self.button1 = ttk.Button(self.frame, text = "Show price of one stock", width = 25, command = self.new_window1).grid(column=1, row=1, sticky=W)
		self.button2= ttk.Button(self.frame, text = "Compare prices of several stocks", width = 25, command = self.new_window2).grid(column=2, row=1, sticky=W)
		self.button3 = ttk.Button(self.frame, text = "Compare a stock with market", width = 25, command = self.new_window3).grid(column=1, row=2, sticky=W)
		self.button4 = ttk.Button(self.frame, text = "Portfolio analysis", width = 25, command = self.new_window4).grid(column=2, row=2, sticky=W)
		self.button5 = ttk.Button(self.frame, text = "About", width = 25, command = lambda:\
						tkMessageBox.showinfo(message='This is a stock analysis project made by cici, Fangyun and Zhuoran. Thank you for your interest!')).\
						grid(column=1, row=3, sticky=W)

		for child in self.frame.winfo_children(): 
			child.grid_configure(padx=10, pady=10)

	def new_window1(self):
		self.newWindow = Toplevel(self.master)
		self.newWindow.title("lalala")
		self.app = SSW.SingleStockWindow(self.newWindow)

	def new_window2(self):
		self.newWindow = Toplevel(self.master)
		self.app = MSW.MultiStocksWindow(self.newWindow)

	def new_window3(self):
		self.newWindow = Toplevel(self.master)
		self.app = CWMW.ComparisonWithMarketWindow(self.newWindow)

	def new_window4(self):
		self.newWindow = Toplevel(self.master)
		self.app = PAW.PortfolioAnalysisWindow(self.newWindow)
