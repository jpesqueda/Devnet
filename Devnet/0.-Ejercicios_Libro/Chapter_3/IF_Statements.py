# if: An if statement is a conditional statement that can compare values and make branching decisions.
# If Statements
# An if statement starts with an if and then sets up a comparison to determine the truth of the statement it is evaluating and ending with a : 
# to tell Python to expect the clause (the action if the condition is true) block of code next. 
# As mentioned earlier in this chapter, whitespace indenting matters very much in Python. 
# The clause of an if statement must be indented (four spaces is the standard) from the beginning of the if statement.

#ejemplo 1
print('ejemplo 1')
n = 20
if n == 20:
    print('The number is 20')


#ejemplo 2
print('\nejemplo 2')

n = 3
if n == 17:
    print('Number is 17')
elif n < 10:
    print('Number is less than 10')
elif n > 10:
    print('Number is greater than 10')


#ejemplo 3
print('Example 3-2 Adding a Final else Statement')
score = int(input('What was your test score?:'))

if score >= 90:
    print('Grade is A')
elif score >= 80:
    print('Grade is B')
elif score >= 70:
    print('Grade is C')
elif score >= 60:
    print('Grade is D')
else:
    print('Grade is F')