#import os  # defines the OS for use with CLS commands later
#os.system ("cls") #gets rid of screen/terminal clutter at the start of the program

print("\033[H\033[J", end="")
import string
string.ascii_letters 
'abcdefghiklmnopqrstuvwxyz'

import random
count=0

rnd_letter = random.choice(string.ascii_letters) #defines rnd_letter as a random letter from the alphabet
#print(f'rnd_letter = {rnd_letter.upper()}') #prints the random letter just as a debug thing so I can see that part is working
print('Welcome to the type letters from the alphabet in random order game!')
#for xyz in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
for xyz in range(27):
    if xyz==26:
        os.system("cls")
        print('You did it! This is a success story for the ages!')
        quit()
    elif xyz != 26:
        print(f'{26-xyz} to go!')
    rnd_letter = random.choice(string.ascii_letters)
    typed = input(f'Type {rnd_letter.upper()} >> ') #tells the user to type the random letter and captures their input as variable called "typed"
    if typed =="quit":
        quit()
    count +=1
    while typed.upper() != (rnd_letter.upper()): 
        typed=input(f'Wrong! Try again! Type {(rnd_letter.upper())} >> ')
    