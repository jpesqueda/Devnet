# Strings
# The string data type is a sequence of characters and uses quotes to determine which characters
# are included. The string ‘Hello’ is just a set of characters that Python stores in order
# from left to right. Even if a string contains a series of numbers, it can still be a string data
# type. If you try to add a 1 to a string value, Python gives you an error, as shown in this
# example:
# >>> '10' + 1
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# This error tells you that you have to convert the string to an integer or another data type to
# be able to use it as a number (in a math formula, for example). 
# The int() function can convert
# a string value into an integer for you, as shown in this example:
print (int('10') + 1)

# If you assign the string DevNet to a variable, you can separate and manipulate the component
# values of the string by using the index value. You can use brackets to specify the index
# number. The following example prints a capitol D from DevNet:
a='DevNet'
print (a[0])

# 'D'
# You can also specify ranges to print. The colon operator gives you control over whole sections
# of a string. The first number is the beginning of the slice, and the second number
# determines the end. The second number may be confusing at first because it is intended to
# identify “up to but not including” the last character. Consider this example:

print ( a[0:3] )

# 'Dev'
# This example shows a 3 at the end, but this is technically four characters since the index
# starts at 0, but Python doesn’t print the last character and instead stops right before it. For
# new Python programmers, this can be confusing, but remember that Python is literal. If you
# think of an index value as a box, in Figure 3-3, you want to stop at box 3 (but don’t want to
# open the box). If you want to print the whole string, just pick a number beyond the index
# value, and Python will print everything, as in this example:

print ( a[0:6] )


# 'DevNet'
# If you omit a value for the first number, Python starts at 0, as in this example:

print ( a[:2] )

# 'De'
# If you omit the second value, Python prints to the end of the string, as in this example:

print ( a[2:] )

# 'vNet'
# You can also reverse direction by using negative numbers. If you put a negative first number,
# you start from the end of the string, as in this example:

print ( a[-2:] )

# 'et'
# A negative value on the other side of the colon causes Python to print using the end as a reference
# point, as in this example:

print ( a[:-2] )

# You can perform math operations on strings as well. The + is used to add or concatenate two
# strings together, as in this example:

print ('DevNet' + 'Rocks')
# 'DevNetRocks'
# Multiplication works as well, as in this example:
print ('DevNet Rocks ' * 5)
# 'DevNet Rocks DevNet Rocks DevNet Rocks DevNet Rocks DevNet Rocks '

# Method What It Does
# str.capitalize()                          Capitalize the string
# str.center(width[, fillchar])             Center justify the string
# str.endwith(suffix[, start[, end]])       Add an ending string to the string
# str.find(sub[, start[, end]])             Find the index position of the characters in a string
# str.lstrip([chars])                       Remove whitespace characters from the end of the string
# str.replace(old, new[, count])            Replace characters in the string
# str.lower()                               Make the string all lowercase
# str.rstrip([chars])                       Strip whitespace characters from the front of the string
# str.strip([chars])                        Remove whitespace characters from the beginning and end of the string
# str.upper()                               Make the string all uppercase
