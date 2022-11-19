#import os  # defines the OS for use with CLS commands later
#os.system ("cls") #gets rid of screen/terminal clutter at the start of the program

print("\033[H\033[J", end="")
import string
string.ascii_letters 
'abcdefghiklmnopqrstuvwxyz'

import random
import time

errorcount=0

t0=time.time()

rnd_letter = random.choice(string.ascii_letters) #defines rnd_letter as a random letter from the alphabet
#print(f'rnd_letter = {rnd_letter.upper()}') # this line for debugging purposes - prints the random letter just as a debug thing so I can see that part is working
print('Welcome to the type letters from the alphabet in random order game!')
#for xyz in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']: /// Ignore this, snippet of old code.
for xyz in range(27):
    if xyz==26:
        print("\033[H\033[J", end="") #clears the screen without being OS dependent 
        t1=time.time()
        tt = t1-t0
        print('You did it! This is a success story for the ages!')
        print(f'You made {errorcount} mistakes and your time was {tt} seconds!')
        quit()
    elif xyz != 26:
        print(f'{26-xyz} to go!')
    rnd_letter = random.choice(string.ascii_letters)
    typed = input(f'Type {rnd_letter.upper()} >> ') #tells the user to type the random letter and captures their input as variable called "typed"
    if typed =="quit":
        quit()
    
    while typed.upper() != (rnd_letter.upper()): 
        errorcount+=1
        if errorcount > 4:
            print(f'You have made {errorcount} mistakes! Are you even trying???')
        typed=input(f'Wrong! Try again! Type {(rnd_letter.upper())} >> ')
    