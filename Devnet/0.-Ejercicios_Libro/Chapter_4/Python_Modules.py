# Importing a Module
# All modules are accessed the same way in Python: by using the import command. 
# Within a program—by convention at the very beginning of the code—you type import followed by the module name you want to use. 
# The following example uses the math module from the standard library:

print('Ejemplo 1 - Importing a Module')
import math

print('\nEjemplo dir(math)' )
print(dir(math))

# you can use the help() function to get more details and read the documentation on the math module.
#print(help(math)) 

#You can also use help() to look at the documentation on a specific function, as in this example:

print(help(math.sqrt))

#If you want to get a square root of a number, you can use the sqrt() method by calling math.sqrt and passing a value to it, as shown here:
print('\nEjemplo math.sqrt(15)' )
print(math.sqrt(15))

#Python lets you rename a module by adding as and a short version of the module name to the end of the import command. 
#For example, you can use this command to shorten the name of the calendar module to cal.

print('\nEjemplo import calendar as cal' )
import calendar as cal

#Now you can use cal as an alias for calendar in your code, as shown in this example:
print(cal.month(2020, 2, 2, 1))


#Python allows you to import specific methods by using the from syntax. 
# Here is an example of importing the sqrt() and tan() methods:
# Notice that you no longer have to use math.sqrt and can just call sqrt() as a function, 
# since you imported only the module functions you needed. Less typing is always a nice side benefit.

print('\nEjemplo import just method sqrt and tan from math module >>> from math import sqrt,tan' )
from math import sqrt,tan
print(sqrt(15))


print('\nEjemplo Importing Your Own Modules' )

import sys
print(sys.path)
