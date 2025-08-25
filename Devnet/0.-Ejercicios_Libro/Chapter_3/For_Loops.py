# # The for statement allows you to create a loop that continues to iterate through the code a specific number of times. 
# # It is also referred to as a counting loop and can work through a sequence of items, such as a list or other data objects. 
# # The for loop is heavily used to parse through data and is likely to be your go-to tool for working with data sets. 
# # A for loop starts with the for statement, followed by a variable name (which is a placeholder used to hold each sequence of data),
# # the in keyword, some data set to iterate through, and then finally a closing colon

#ejemplo 1
print('ejemplo 1')
dataset=(1,2,3,4,5)
for variable in dataset:
    print(variable)

# The for loop continues through each item in the data set, and in this example, 
# it prints each item. You can also use the range() function to iterate a specific number of times.


#ejemplo 2
print('\nejemplo 2')
for x in range(3):
    print(x)


# By default, if you just give range() a number, it starts at 0 and goes by 1s until it reaches the number you provided. 
# Zero is a valid iteration, but if you don’t want it, you can start at 1. 
# Consider this example:

#ejemplo 3
print('\nExample 3')
for x in range(1,3):
    print(x)


# To change the increment from the default of 1, you can add a third attribute to the range() statement. 
# In the following example, you start at 1 and increment by 3 until you reach 10:

#ejemplo 4
print('\nExample 4')

for x in range(1,11,3):
    print(x)

    