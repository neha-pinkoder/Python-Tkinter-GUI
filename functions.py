# functions for _appProject.py

# print contents of submit form to the console
def printToConsole():
	nameStr = nameField.get()
	emailStr = emailField.get()
	feedbackStr = commentsField.get('1.0', 'end')
	print('Name: ', nameStr)
	print('Email: ', emailStr)
	print('Feedback: ', feedbackStr)
	
# clear the submit form
'''
def clearFields():
	commentsField.delete('1.0', 'end')
	nameField.delete(0, END)
	emailField.delete(0, END)
'''
def clearFields(*args): # (nameField, emailField, commentsField)
	name = args[0]
	name.insert(0, '')
	#args[0].delete(0, END)
	#args[1].delete(0, END)
	#args[2].delete('1.0', 'end')
		
# provide user with popup confirmation that form was submitted	
def confirmSubmission():
	print('confirmSubmission()')
	# popup window confirming that form was submitted
	
# clear submit form, confirm submission, and print contents to console
def submitInfo():
	printToConsole()
	clearFields()
	#confirmSubmission()

# read 'thanks' text from external file and return to caller
def getThanksStr():
	infile = open('thanks.txt', 'r')
	textStr = infile.read().strip()
	infile.close()
	return textStr