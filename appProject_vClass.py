# appProject_vClass.py

# this file contains the second version of appProject.py
# with all aspects of the GUI implemented as a class

# imports ===========================================
from tkinter import *
from tkinter import ttk

# classes ===========================================
class FeedbackForm:
	# class constructor
	def __init__(self, master):
		# stuff

# main ==============================================
def main():
	root = Tk()
	feedback = FeedbackForm(root)
	root.mainloop()
	
	print('Done.')

if __name__ == '__main__': main()	