# appProject_noClass.py
# for requirements, see requirements.txt

# imports ===========================================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# functions =========================================
# print contents of submit form to the console
def printToConsole():
	nameStr = nameField.get()
	emailStr = emailField.get()
	feedbackStr = commentsField.get('1.0', 'end')
	print('Name: ', nameStr)
	print('Email: ', emailStr)
	print('Feedback: ', feedbackStr)
	
# clear the submit form
def clearFields():
	commentsField.delete('1.0', 'end')
	nameField.delete(0, END)
	emailField.delete(0, END)

# provide user with popup confirmation that form was submitted	
def confirmSubmission():
	messagebox.showinfo(title = 'Success!', message = 'Thanks! Your form has been submitted!')
	
# clear submit form, confirm submission, and print contents to console
def submitInfo():
	printToConsole()
	clearFields()
	confirmSubmission()

# read 'thanks' text from external file and return to caller
def getThanksStr():
	infile = open('thanks.txt', 'r')
	textStr = infile.read().strip()
	infile.close()
	return textStr

# tkinter ===========================================
# create feedback-form window
root = Tk()
root.title('Feedback Form')
root.geometry('640x480')

# banner -----------------------------------
bannerFrame = Frame(root, height = 75)
bannerFrame.pack()

logoFrame = Frame(bannerFrame)
logoFrame.grid(row = 0, column = 0)

titleFrame = Frame(bannerFrame)
titleFrame.grid(row = 0, column = 1)

# logo section of banner
logo = PhotoImage(file='tour_logo.gif')
logoLabel = ttk.Label(logoFrame)
logoLabel.configure(image = logo, border = 0)
logoLabel.pack()

# title section of banner
exploreLabel = ttk.Label(
	titleFrame,
	text = 'EXPLORE',
	background = '#5DBCD2',
	foreground = '#723724',
	border = 0,
	width = 40,
	font = ('Arial Bold', 18)
	)
exploreLabel.pack()

caliLabel = ttk.Label(
	titleFrame,
	text = 'CALIFORNIA',
	background = '#723724',
	foreground = '#FFFFFF',
	border = 0,
	width = 40,
	font = ('Arial Bold', 18)
	)
caliLabel.pack()

# request for feedback ---------------------
thanksFrame = Frame(root)
thanksFrame.pack()

thanksStr = '\n' + getThanksStr()
thanksLabel = ttk.Label(
	thanksFrame,
	text = thanksStr,
	font = ('Arial', 12),
	foreground = '#723724',
	wraplength = 600)
thanksLabel.pack()

# submit form ------------------------------
# submit frame
submitForm = Frame(root, pady = 20)
submitForm.pack()

# name frame
nameFrame = Frame(submitForm, pady = 10)

nameLabel = ttk.Label(
	nameFrame,
	text = 'Name:     ',
	width = 10,
	foreground = '#723724',
	anchor = E)

nameField = ttk.Entry(
	nameFrame,
	width = 30,
	foreground = '#6A564A'
	)

nameFrame.pack()
nameLabel.grid(row = 0, column = 0)
nameField.grid(row = 0, column = 1)

# email frame
emailFrame = Frame(submitForm, pady = 10)

emailLabel = ttk.Label(
	emailFrame,
	text = 'Email:    ',
	width = 10,
	foreground = '#723724',
	anchor = E)

emailField = ttk.Entry(
	emailFrame,
	width = 30,
	foreground = '#6A564A',
	)
emailFrame.pack()

emailLabel.grid(row = 0, column = 0)
emailField.grid(row = 0, column = 1)

# comments frame
commentsFrame = Frame(submitForm, pady = 10)

commentsLabel = ttk.Label(
	commentsFrame,
	text = 'Feedback: ',
	width = 20,
	foreground = '#723724',
	anchor = NE)

commentsFieldFrame = Frame(commentsFrame)

commentsField = Text(
	commentsFieldFrame,
	width = 40,
	height = 5,
	relief = SUNKEN,
	wrap = 'word',
	background = '#FAEFDD',
	foreground = '#6A564A'
	)

commentsFrame.pack()
commentsLabel.grid(row = 0, column = 0)
commentsFieldFrame.grid(row = 0, column = 1)
commentsField.grid(row = 0, column = 0)

# scroll bar
# add scroll bar to commentsField
yscroll = ttk.Scrollbar(
	commentsFieldFrame,
	orient = VERTICAL,
	command = commentsField.yview
	)

yscroll.grid(row = 0, column = 1, sticky = 'ns')

# synch scrollbar to text field
commentsField.configure(yscrollcommand = yscroll.set) 

# buttons frame
buttonsFrame = Frame(submitForm, pady = 20)
buttonsFrame.pack()

submitButton = ttk.Button(
	buttonsFrame,
	text = 'Submit',
	command = submitInfo
	)

clearButton = ttk.Button(
	buttonsFrame,
	text = 'Clear',
	#command = lambda: nameField.delete(0,END)
	command = clearFields
	)

submitButton.grid(row = 1, column = 0)
clearButton.grid(row = 1, column = 1)

# ttk main loop
root.mainloop()

# main ==============================================
def main():
	print('Done')

if __name__ == '__main__': main()