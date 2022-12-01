#Author: https://github.com/Skeptjk/
# Licence: None - Don't steal my shit

print("\033[H\033[J", end="")

#2d lists 

#this 3x3 is a matrix
#  1  2  3
#  4  5  6
#  7  8  9
#we can model this in python

demo_matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
# this ^ is a 2 dimensional list. Each item/row is another list.
#to access an individual item we use square brackets, a la:

ex = demo_matrix1[0][1] #first number is the 'row' (starts at zero like everything else in python) - Second number is the horizontal value - also starts at zero
#that bit of code ^ is just to define 'ex' as something so we can print it easily and change it in examples later. Here it will return 2.
print (ex)

#we can also use similar syntax to change items in the matrix - like this

demo_matrix1 [0][1] = 20
ex = demo_matrix1 [0][1]
print (ex)
#now even though we are referencing the same 'place' in the matrix, the value there has been changed. It now returns 20 instead of 2. 

#for loops in matrices - 
#need a new matrix now
print('')
print('___________________________________')
print('')

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for i in matrix2:
    #in each iteration i will be one row
    for item in i:
        print (item)
        