# _appProject.py
# for requirements, see requirements.txt
# imports ===========================================
from tkinter import *
from tkinter import ttk

# globals ===========================================

# classes ===========================================
		
	
# functions =========================================
def printToConsole():
	# print contents of input fields to the console
	print('printToConsole()')
	
def clearFields():
	# empty the input fields
	print('clearFields()')

def confirmSubmission():
	# popup window confirming that form was submitted
	print('confirmSubmission()')

def submitForm():
	# printToConsole()
	# clearFields()
	# confirmSubmission()
	print('submitForm()')

def getThanksStr():
	# read the thanks text from external file and return it
	# to the calling function
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
# 
# PhotoImage-->logo.grid(0, 1)  |  label-->title.grid (0, 2)
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
exploreLabel = ttk.Label(titleFrame, text = 'EXPLORE',
						 background = '#5DBCD2',
						 foreground = '#723724',
						 border = 0,
						 width = 40,
						 font = ('Arial Bold', 18)
						 )
exploreLabel.pack()

caliLabel = ttk.Label(titleFrame, text = 'CALIFORNIA',
					  background = '#723724',
					  foreground = '#FFFFFF',
					  border = 0,
					  width = 40,
					  font = ('Arial Bold', 18)
					  )
caliLabel.pack()

# request for feedback ---------------------
# 
# label-->label.pack() (text = 'we appreciate you, please submit feedback')
thanksFrame = Frame(root)
thanksFrame.pack()

thanksStr = '\n' + getThanksStr()
thanksLabel = ttk.Label(thanksFrame,
						text = thanksStr,
						font = ('Arial', 12),
						foreground = '#723724',
						wraplength = 600)
thanksLabel.pack()

# submit form ------------------------------
# labelFrame.grid( name, email, comment)  |  inputFrame.grid(textBox, textBox, entryField)
# submit frame
submitFrame = Frame(root)
submitFrame.pack()

# submit labels
submitLabelsFrame = Frame(submitFrame)
submitLabelsFrame.grid(row = 0, column = 0)

nameLabel = ttk.Label(submitLabelsFrame, text = 'Name:')
emailLabel = ttk.Label(submitLabelsFrame, text = 'Email:')
commentsLabel = ttk.Label(submitLabelsFrame, text = 'Comments')

nameLabel.pack()
emailLabel.pack()
commentsLabel.pack()

# submit fields
submitFieldsFrame = Frame(submitFrame)
submitFieldsFrame.grid(row = 0, column = 1)

nameField = ttk.Entry(submitFieldsFrame, width = 30)
nameField.pack()

emailField = ttk.Entry(submitFieldsFrame, width = 30)
emailField.pack()

commentsFieldFrame = Frame(submitFieldsFrame)
commentsField = Text(commentsFieldFrame,
					 width = 40,
					 height = 10,
					 relief = RIDGE,
					 wrap = 'word'
					 )
yscroll = ttk.Scrollbar(commentsFieldFrame,
						orient = VERTICAL,
						command = commentsField.yview)
# synch scrollbar to contents of text field
commentsField.configure(yscrollcommand = yscroll.set)

commentsFieldFrame.pack()
commentsField.grid(row = 0, column = 0)
yscroll.grid(row = 0, column = 1, sticky = 'ns')





# submit buttons ---------------------------
# submitButton.pack()
# clearButton.pack()


# ttk main loop
root.mainloop()

# main ==============================================
def main():
	print('Done')

if __name__ == '__main__': main()