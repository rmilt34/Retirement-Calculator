from tkinter import *

age = 28
retirementAge = 55



root = Tk()

#def addField(field, fieldLabel, fieldText):
#    fieldLabel = Label(root, text = fieldText)
#    fieldLabel.pack()
#    field = Entry(root)
 #   field.pack()

#addField("age", "ageLabel", "Enter your age:")
#addField("retirementAge", "retirementAgeLabel", "Enter the age at which you plan to retire:")
#addField("savingsPerYear", "savingsPerYearLabel", "Annual retirement contribution:")

ageLabel = Label(root, text = "Enter your age:")
ageLabel.pack()
age = Entry(root)
age.pack()


retirementAgeLabel = Label(root, text = "Enter the age at which you plan to retire:")
retirementAgeLabel.pack()
retirementAge = Entry(root)
retirementAge.pack()





def calculate():
    testLabel = Label(root, text = retirementAge - age)
    testLabel.pack()

calculateButton = Button(root, text = "Calculate", command = calculate)
calculateButton.pack()


root.mainloop()





#savingsPerYear = int(input("$ Saved per year:\n"))
#retirementSpending = int(input("$ Spent per year in retirement:\n"))
#age = int(input("enter your age now"))
#retirementAge = int(input("enter the age of retirement"))
#savingsGoal = retirementSpending / 0.04

#totalSavings = savingsPerYear * (retirementAge - age)
#print(totalSavings, savingsGoal)