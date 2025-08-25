# Python offers two types of functions: built-in functions that are part of the standard library and functions you create yourself. 
# The standard library includes a huge number of functions you can use in your program, like print(), 
# many of which you have already been introduced to in Chapter 3. Building your own functions is how you construct capabilities 
# that are not already present within the Python language.

# -To define a function in Python, you use the keyword def, a name for the function, a set of parentheses enclosing any arguments you want to pass to the function, and a colon at the end. The name of a function must follow these rules:
# -Must not start with a number
# -Must not be a reserved Python word, a built-in function (for example, print(), input(), type()), or a name that has already been used as a function or variable
# -Can be any combination of the A–Z, a–z, 0–9 and the underscore (_) and dash (-)

#ejemplo 1
print('Ejemplo 1 - prints simple function')
def devnet():
    '''prints simple function'''
    print('Simple function')
devnet()


# help(devnet)
#     Help on function devnet in module __main__:

# devnet()
#     prints simple function



# Using Arguments and Parameters
# An argument is some value (or multiple values) that you pass to a function when you call the function within code. Arguments allow a function to produce different results and make code reuse possible. You simply place arguments within the parentheses after a function name. For example, this example shows how you can pass multiple numeric arguments to the max() function to have it return the largest number in the list:
#max(50, 5, 8, 10, 1)

#ejemplo 2
print('\nEjemplo 2 - Using Arguments and Parameters')

def sub(arg1, arg2):
    result = arg1 - arg2
    return result

print(sub(10, 15))



#ejemplo 3
print('\nExample 3 - using arguments')
def hello(*args):
        for arg in args:
            print("Hello", arg, "!")
hello('Caleb', 'Sydney', 'Savannah')


# Note the use of the items() function in the for statement to unpack and iterate through the values.
#ejemplo 
print('\nExample 4 - using keyword arguments')
def hello(**kwargs):
    for key, value in kwargs.items():
        print("Hello", value, "!")

hello(kwarg1='Caleb', kwarg2='Sydney', kwarg3='Savannah')


#ejemplo 
print('\nExample 5 - defining a function with an assigned key value')
def greeting(name, message="Good morning!"):
    print("Hello", name + ', ' + message)

greeting('Caleb')
greeting('Sydney', "How are you?")
