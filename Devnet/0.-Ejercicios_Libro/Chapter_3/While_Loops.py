# While Loops
# Whereas the for loop counts through data, the while loop is a conditional loop, 
# and the evaluation of the condition (as in if statements) being true is what determines how many times the loop executes. 
# This difference is huge in that it means you can specify a loop that could conceivably go on forever, 
# as long as the loop condition is still true. You can use else with a while loop. 
# An else statement after a while loop executes when the condition for the while loop to continue is no longer met. 
# Example 3-3 shows a count and an else statement.

#ejemplo 1
print('ejemplo 1')
count = 1
while (count < 5):
    print("Loop count is:", count)
    count = count + 1
else:
    print("loop is finished")



# You can probably see similarities between the loop in Example 3-3 and a for loop. 
# The difference is that the for loop was built to count, 
# whereas this example uses an external variable to determine how many times the loop iterates. 
# In order to build some logic into the while loop, you can use the break statement to exit the loop. 
# Example 3-4 shows a break with if statements in an infinite while loop.

#ejemplo 2
print('\nejemplo 2')
while True:
    string = input('Enter some text to print. \nType "done" to quit> ')
    if string == 'done' :
        break
    print(string)
print('Done!')

