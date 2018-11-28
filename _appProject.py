# _appProject.py
'''
PURPOSE:
Create a feedback form for Explore California website (explorecalifornia.org)
to allow guests who have completed the 'From Desert to Sea' tour
to leave comments about their experience

REQUIREMENTS:
1 Form will display a logo and instructions to the user
2 Form will have input fields for:
    Name
	Email address
	Multiline comment field
	Submit button
	Clear button
3 Submit button will:
    Print contents of input fields (to the console)
	Empty content of input field
	Notify the user that comments were submitted
4 Clear button will:
    Empty the input fields
'''
# imports ===========================================
from tkinter import *
from tkinter import ttk

# globals ===========================================

# classes ===========================================
class Feedback:
	def __init__(self, master):
		
	
# functions =========================================

# tkinter ===========================================
root = Tk()
feedback = Feedback(root)

# ttk main loop
root.mainloop()

# main ==============================================
def main():
	print('Done')

if __name__ == '__main__': main()