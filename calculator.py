from tkinter import *
from tkinter import messagebox

root = Tk() # object is created 
root.title("Calculator designed by pawan chaudhary") # Title of the GUI
root.resizable(0,0) # non-resizable
# Class is created for the GUI and its component
class Calculator(Frame):
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.calculatorDesign()

	def cleanText(self, value):
		self.display.delete(0, END)
		self.display.insert(0, value)

	def buttonFunction(self, value):
		self.entryText = self.display.get()
		self.textLength = len(self.entryText)
		if self.entryText == "0":
			self.cleanText(value)
		else:
			self.display.insert(self.textLength, value)

	def calculation(self): 
		self.expression = self.display.get()
		self.expression = self.expression.replace("%", "/ 100")

		try:
			self.result = eval(self.expression)
			self.cleanText(self.result)
		except:
			messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=root)

	def clearScreen(self):
		self.cleanText("0")

	def calculatorDesign(self):
		self.display = Entry(self, font=("Arial", 50), borderwidth=2, relief=RAISED, justify=RIGHT)
		self.display.insert(0, "0")
		self.display.grid(row=0, column=0, columnspan=5)

#This is the First Row
		self.sevenButton = Button(self, font=("Arial", 50, "bold"), text="7", command=lambda: self.buttonFunction("7"))
		self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")

		self.eightButton = Button(self, font=("Arial", 50, "bold"), text="8", command=lambda: self.buttonFunction("8"))
		self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")

		self.nineButton = Button(self, font=("Arial", 50, "bold"), text="9", command=lambda: self.buttonFunction("9"))
		self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")

		self.timesButton = Button(self, font=("Arial", 50, "bold"), text="x", command=lambda: self.buttonFunction("*"))
		self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")

		self.clearButton = Button(self, font=("Arial", 50, "bold"), text="C", command=lambda: self.clearScreen())
		self.clearButton.grid(row=1, column=4, sticky="NWNESWSE")

#This is the Second Row
		self.fourButton = Button(self, font=("Arial", 50, "bold"), text="4", command=lambda: self.buttonFunction("4"))
		self.fourButton.grid(row=2, column=0, sticky="NWNESWSE")

		self.fiveButton = Button(self, font=("Arial", 50, "bold"), text="5", command=lambda: self.buttonFunction("5"))
		self.fiveButton.grid(row=2, column=1, sticky="NWNESWSE")

		self.sixButton = Button(self, font=("Arial", 50, "bold"), text="6", command=lambda: self.buttonFunction("6"))
		self.sixButton.grid(row=2, column=2, sticky="NWNESWSE")

		self.divideButton = Button(self, font=("Arial", 50, "bold"), text="/", command=lambda: self.buttonFunction("/"))
		self.divideButton.grid(row=2, column=3, sticky="NWNESWSE")

		self.percentageButton = Button(self, font=("Arial", 50, "bold"), text="%", command=lambda: self.buttonFunction("%"))
		self.percentageButton.grid(row=2, column=4, sticky="NWNESWSE")

#This is the Third Row
		self.oneButton = Button(self, font=("Arial", 50, "bold"), text="1", command=lambda: self.buttonFunction("1"))
		self.oneButton.grid(row=3, column=0, sticky="NWNESWSE")

		self.twoButton = Button(self, font=("Arial", 50, "bold"), text="2", command=lambda: self.buttonFunction("2"))
		self.twoButton.grid(row=3, column=1, sticky="NWNESWSE")

		self.threeButton = Button(self, font=("Arial", 50, "bold"), text="3", command=lambda: self.buttonFunction("3"))
		self.threeButton.grid(row=3, column=2, sticky="NWNESWSE")

		self.minusButton = Button(self, font=("Arial", 50, "bold"), text="-", command=lambda: self.buttonFunction("-"))
		self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")

		self.equalsButton = Button(self, font=("Arial", 50, "bold"), text="=", command=lambda: self.calculation())
		self.equalsButton.grid(row=3, column=4, sticky="NWNESWSE", rowspan=2)

#This is the Fourth Row
		self.zeroButton = Button(self, font=("Arial", 50, "bold"), text="0", command=lambda: self.buttonFunction("0"))
		self.zeroButton.grid(row=4, column=0, columnspan=2, sticky="NWNESWSE")

		self.dotButton = Button(self, font=("Arial", 50, "bold"), text=".", command=lambda: self.buttonFunction("."))
		self.dotButton.grid(row=4, column=2, sticky="NWNESWSE")

		self.plusButton = Button(self, font=("Arial", 50, "bold"), text="+", command=lambda: self.buttonFunction("+"))
		self.plusButton.grid(row=4, column=3, sticky="NWNESWSE")
#Class is called through the varibale application
application = Calculator(root).grid()
# executing the the GUI
root.mainloop()
