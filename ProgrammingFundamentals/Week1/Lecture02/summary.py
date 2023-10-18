# printing using ' and "
print('Hello')
print("This is the same thing - printing a String")

print() # using print on its own to create whitespace (gaps) in the output
print()


# \t (tab) and \n (newline)
print("Item1\tItem2\tItem3\nItem4\tItem5\tItem6")
print() # using print on its own to create whitespace (gaps) in the output
print()


# sep and end
print("The rain", "in Spain")  # print() adds a newline character to the end of the output
print("The rain", "in Spain", end=":")  # end can be used to change the newline character to anything else
print("The rain", "in Spain", end="CLIONA WAS HERE")
print() # using print on its own to create whitespace (gaps) in the output
print()
print("The rain", "is here", "now") # commas add spaces between items in the output
print("The rain", "is here", "now", sep=" *** ") # sep can be used to change this to whatever you want
print("Item1","Item2","Item3", sep="\t")




# Using " and ' together
print("Isn't this great?")
print() # using print on its own to create whitespace (gaps) in the output
print()


# Using ''' to print out exactly what you type
print('''Whatever I type
and however I type it
will appear       exactly''')

print() # using print on its own to create whitespace (gaps) in the output
print()
print() # using print on its own to create whitespace (gaps) in the output
print()




# VARIABLES - creating named pieces of memory in RAM
subject = "Programming Fundamentals"
print("This subject is", subject)

number_of_students = 178
print(subject, "has", number_of_students, "students")

average_mark = 78.6
print("The average mark in", subject, "is", average_mark)

# These are examples of String, integer numbers and decimal (floating point) numbers variables
print(type(subject))
print(type(number_of_students))
print(type(average_mark))

print()
print()

# Rules of names
# - must start with letter or underscore
# - may contain numbers, letters and underscores

# Some simple maths
number1 = 5
number2 = 2
print(number1, '+', number2,'=',number1 + number2)
print(number1, '-', number2,'=',number1 - number2)
print(number1, '*', number2,'=',number1 * number2)
print(number1, '/', number2,'=',number1 / number2)
print(number1, '**', number2,'=',number1 ** number2)

# What do the following operators do??? Can you guess??
# More about this on Thursday....
print()
number1 = 25
number2 = 4
print(number1, '//', number2,'=',number1 // number2)
print(number1, '%', number2,'=',number1 % number2)

