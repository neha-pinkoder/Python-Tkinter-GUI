# appProject_vClass_v3.py

# this file contains the second version of appProject.py
# with all aspects of the GUI implemented as a class

# v2
# added class functions

# v3
# added configurations and geometry management

# imports ===========================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# classes ===========================================
class FeedbackForm:
	# class constructor -----------------------------
	def __init__(self, master):
		# create widgets ----------------------------
		# frame widgets
		self.bannerFrame = ttk.Frame(master)
		self.logoFrame = ttk.Frame(self.bannerFrame)
		self.titleFrame = ttk.Frame(self.bannerFrame)
		self.thanksFrame = ttk.Frame(master)
		self.submitForm = Frame(master)
		self.nameFrame = Frame(self.submitForm)
		self.emailFrame = Frame(self.submitForm)
		self.commentsFrame = Frame(self.submitForm)
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
		self.thanksStr = '\n' #+ self.getThanksStr()
		self.yscroll = ttk.Scrollbar(self.commentsFieldFrame)
		self.submitButton = ttk.Button(self.buttonsFrame)
		self.clearButton = ttk.Button(self.buttonsFrame)
		
		# configure widgets -----------------------------
		# frame widgets
		self.bannerFrame.configure(height = 75)
		self.logoFrame
		self.titleFrame
		self.thanksFrame
		self.submitForm.configure(pady = 20)
		self.nameFrame.configure(pady = 10)
		self.emailFrame.configure(pady = 10)
		self.commentsFrame.configure(pady = 10)
		self.commentsFieldFrame
		self.buttonsFrame
		
		# label widgets
		self.logoLabel.configure(image = self.logo, border = 0)
		self.exploreLabel.configure(
			text = 'EXPLORE',
			background = '#5DBCD2',
			foreground = '#723724',
			border = 0,
			width = 40,
			font = ('Arial Bold', 18)
		)
		self.caliLabel.configure(
			text = 'CALIFORNIA',
			background = '#723724',
			foreground = '#FFFFFF',
			border = 0,
			width = 40,
			font = ('Arial Bold', 18)
		)
		self.thanksLabel.configure(
			text = self.thanksStr,
			font = ('Arial', 12),
			foreground = '#723724',
			wraplength = 600
		)
		self.nameLabel.configure(
			text = 'Name:     ',
			width = 10,
			foreground = '#723724',
			anchor = E
		)
		self.emailLabel.configure(
			text = 'Email:    ',
			width = 10,
			foreground = '#723724',
			anchor = E			
		)
		self.commentsLabel.configure(
			text = 'Feedback: ',
			width = 20,
			foreground = '#723724',
			anchor = NE
		)

		# entry widgets
		self.nameField.configure(
			width = 30,
			foreground = '#6A564A'
		)
		self.emailField.configure(
			width = 30,
			foreground = '#6A564A'
		)
		
		# text widgets
		self.commentsField.configure(
			width = 40,
			height = 5,
			relief = SUNKEN,
			wrap = 'word',
			background = '#FAEFDD',
			foreground = '#6A564A'
		)
		
		# pics, strings, scrollbars, buttons
		self.logo
		self.thanksStr
		self.yscroll
		self.submitButton
		self.clearButton
		
		# geometry management ---------------------------
		self.bannerFrame.pack()
		self.logoFrame.grid(row = 0, column = 0)
		self.titleFrame.grid(row = 0, column = 1)
		self.logoLabel.pack()
		self.exploreLabel.pack()
		self.caliLabel.pack()
		self.thanksFrame.pack()
		self.thanksLabel.pack()
		self.submitForm.pack()
		self.nameFrame.pack()
		self.nameLabel.grid(row = 0, column = 0)
		self.nameField.grid(row = 0, column = 1)
		self.emailFrame.pack()
		self.emailLabel.grid(row = 0, column = 0)
		self.emailField.grid(row = 0, column = 1)
		self.commentsFrame.pack()
		self.commentsLabel.grid(row = 0, column = 0)
		self.commentsFieldFrame.grid(row = 0, column = 1)
		self.commentsField.grid(row = 0, column = 0)
		
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