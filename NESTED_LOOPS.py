#Author: https://github.com/Skeptjk/
# Licence: None - Don't steal my shit

print("\033[H\033[J", end="")

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print (f'x' * (x))
    
print ('')
print ('')
print ('')
print ('')
print ('____________')

#the same output but using nested loops
numbers = [5, 2, 5, 2, 2]
for x_count in numbers: #creates X count and sets it up to have its value change according to the list (numbers) as the main loop iterates
    output = '' #creates a variable called output which is basically empty, we're going to add to it later. This also will reset it, for later, which is an important bit!
    for count in range (x_count): #this is the nested loop, it's going to loop around based on what x_count is, which is going to be the quantity in the list called 'numbers' from earlier
        output = output + 'x' #used the long form here as it's more illusrtative of what's going on inside the nested loop / this adds the number of X's currently held in x_count
    print (output) #once the nested loop has iterated the number of times in x_count (ie, the current value from the list 'numbers') it prints whatever X is. 
    
print ('')
print ('')
print ('')
print ('')
print ('____________')

#the same but this time printing an L 
numbers = [2, 2, 2, 6]
for x_count in numbers: #creates X count and sets it up to have its value change according to the list (numbers) as the main loop iterates
    output = '' #creates a variable called output which is basically empty, we're going to add to it later. This also will reset it, for later, which is an important bit!
    for count in range (x_count): #this is the nested loop, it's going to loop around based on what x_count is, which is going to be the quantity in the list called 'numbers' from earlier
        output = output + 'x' #used the long form here as it's more illusrtative of what's going on inside the nested loop / this adds the number of X's currently held in x_count
    print (output) #once the nested loop has iterated the number of times in x_count (ie, the current value from the list 'numbers') it prints whatever X is. 
