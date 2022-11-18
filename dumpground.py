import os  # defines the OS for use with CLS commands later
os.system ('cls') #gets rid of screen/terminal clutter at the start of the program

import string
string.ascii_letters 
'abcdefghiklmnopqrstuvwxyz'

import random

rnd_letter = random.choice(string.ascii_letters) #defines rnd_letter as a random letter from the alphabet
print(f'rnd_letter = {rnd_letter}') #prints the random letter just as a debug thing so I can see that part is working

#line 14 = hopefully saying "for all the time that rnd_letter is in the range of abcdefghi etc etc, keep the loop running "
for rnd_letter in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    typed = input(f'Type {rnd_letter} >> ') #tells the user to type the random letter and captures their input as variable called "typed"
    while typed.upper() != (rnd_letter.upper()): #subloop that captures errors - if 'typed' doesnt equal rnd_letter variable then print wrong and recapture "typed" (in the next line)
        print('Wrong! Try again')
        typed=input(f'Type {rnd_letter} >> ')
#my thought was if they don't hit the 'doesnt equal' loop tripwire then it means they got it right and the loop will loop