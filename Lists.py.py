#Author: https://github.com/Skeptjk/
# Licence: None - Don't steal my shit

print("\033[H\033[J", end="") #My standard bit of code to clear the terminal / screen at the start of the program. I don't like clutter. 

#Lists

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary'] #Creates a list - in this case, names. 
print (names) #prints our unmodified list.

print ('_____________________________________')
print ('Indexing names')
print ('_____________________________________')
print (f'names [0]: {names[0]}') # We can index items in a list - the index runs from 0 to however many items there are in the list. This outputs "John"
print (f'names [2]: {names[2]}') # Because lists start at zero, not 1, this will return Mosh, not Bob
print (f'names [-1]: {names[-1]}') # We can also do negative indexes - this will return Mary
print (f'names [-2]: {names[-2]}')
print ('_____________________________________')
print ('')
print ('Select a range of items from a list ')
print (f'names [2:] -  {names[2:]}') # adding the semicolon after the number means we select as a range from the list. This will select all items from 2 (Mosh) to the  end of the list
print (f'names [2:4] -  {names[2:4]}') # We can also specify an end index - in this case 4 - so the list will print from Mosh to Sarah in this case as the last item (4) is not included
print (f'names [1:3] -  {names[0:3]}') # and in this case from John to Mosh
print ('_____________________________________')
print ('')

# None of these modifiers *change* our list - the 'names' list is the same as it was at the start of this file. We can however modify the list if we want to..
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary'] #Creates a list - in this case, names. 
print (names) #prints our unmodified list.
names[0] = 'Jon' #here we change the item indexed at 0 (John) to "Jon"
print (names) # and we can see here that this time, we *have* changed the contents of the 'names' list - John has become Jon. 

print('')
print('')
print('')
# Excercise - Write a program to find the largest number in a list

numbers = [61, 5, 90, 38, 8, 89, 83, 63, 69, 56, 81, 91, 52, 49, 25, 18, 82, 65, 14, 3, 16] #defines our list
max=0 #creates variable max and gives it a value of 0
for x in numbers: #sets up a loop to iterate over all the numbers in the list
    if max < x:  #each time the loop goes around, this will check whether our variable max is smaller than x (which we created in the for loop). If it is, it overwrites the value of max with whatever x is. 
        max = x
        print (max) # Uncomment this to see it changing X1 over all the loop steps   
print (f'The highest number is {max}') # once the for loop has iterated over all the numbers, max will be the highest number that was found. This just prints it. 

print ('_____________________________________')
print ('')
# Could also do the above like this (Sort of like the above, anyway.. this returns all the numbers, sorted, instead of just the highest one..  
numbers.sort()
print ('numbers, ascending')
print (numbers)
print('')
# or

print ('numbers, descending')
numbers.reverse()
print (numbers)
