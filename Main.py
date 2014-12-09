'''
Created on 2014.12.1

@author: Zhuoran Lyu
'''
from Tkinter import *
import ttk
from WindowPackage.MainWindow import MainWindow
#from PIL import Image, ImageTk

def main():
	root = Tk()
	root.title("Stock Analysis")
	app = MainWindow(root)
	root.mainloop()

if __name__ == '__main__':
	main()
