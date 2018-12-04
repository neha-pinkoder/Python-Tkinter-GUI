# appProject_vClass_v2.py

# this file contains the second version of appProject.py
# with all aspects of the GUI implemented as a class

# v2
# added class functions

# imports ===========================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# classes ===========================================
class FeedbackForm:
	# class constructor -----------------------------
	def __init__(self, master):
		# frame widgets
		self.bannerFrame = ttk.Frame(master)
		self.logoFrame = ttk.Frame(self.bannerFrame)
		self.titleFrame = ttk.Frame(self.bannerFrame)
		self.thanksFrame = ttk.Frame(master)
		self.submitForm = ttk.Frame(master)
		self.nameFrame = ttk.Frame(self.submitForm)
		self.emailFrame = ttk.Frame(self.submitForm)
		self.commentsFrame = ttk.Frame(self.submitForm)
		self.commentsFieldFrame = ttk.Frame(self.commentsFrame)
		self.buttonsFrame = ttk.Frame(self.submitForm)
		
		# label widgets
		self.logoLabel = ttk.Label(self.logoFrame)
		self.exploreLabel = ttk.Label(self.titleFrame)
		self.caliLabel = ttk.Label(self.titleFrame)
		self.thanksLabel = ttk.Label(self.thanksFrame)
		self.nameLabel = ttk.Label(self.nameFrame)
		self.emailLabel = ttk.Label(self.emailFrame)
		self.commentsLabel = ttk.Label(self.commentsFrame)

		# entry widgets
		self.nameField = ttk.Entry(self.nameFrame)
		self.emailField = ttk.Entry(self.emailFrame)
		
		# text widgets
		self.commentsField = Text(self.commentsFieldFrame)
		
		# pics, strings, scrollbars, buttons
		self.logo = PhotoImage(file = 'tour_logo.gif')
		self.thanksStr = '\n'# + getThanksStr()
		self.yscroll = ttk.Scrollbar(self.commentsFieldFrame)
		self.submitButton = ttk.Button(self.buttonsFrame)
		self.clearButton = ttk.Button(self.buttonsFrame)
		
	# class methods ---------------------------------
	# print contents of submit form to the console
	def printToConsole(self):
		nameStr = self.nameField.get()
		emailStr = self.emailField.get()
		feedbackStr = self.commentsField.get('1.0', 'end')
		print('Name: ', nameStr)
		print('Email: ', emailStr)
		print('Feedback: ', feedbackStr)
		
	# clear the submit form
	def clearFields(self):
		self.commentsField.delete('1.0', 'end')
		self.nameField.delete(0, END)
		self.emailField.delete(0, END)
		
	# provide user with popup confirmation that form was submitted
	def confirmSubmission(self):
		messagebox.showinfo(title = 'Success!',
							message = 'Thanks! Your form has been submitted!')
		
	# clear submit form, confirm submission, and print contents to console
	def submitInfo(self):
		self.printToConsole()
		self.clearFields()
		self.confirmSubmission()

	# read 'thanks' text from external file and return to caller
	def getThanksStr(self):
		infile = open('thanks.txt', 'r')
		textStr = infile.read().strip()
		infile.close()
		return textStr
	
# main ==============================================
def main():
	root = Tk()
	root.title('Feedback Form')
	root.geometry('640x480')
	feedback = FeedbackForm(root)
	root.mainloop()
	
	print('Done.')

if __name__ == '__main__': main()	