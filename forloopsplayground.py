import os  # defines the OS for use with CLS commands later
os.system ("cls") #gets rid of screen/terminal clutter at the start of the program
import string
string.ascii_letters 
'abcdefghiklmnopqrstuvwxyz'

import random
count=0

rnd_letter = random.choice(string.ascii_letters) #defines rnd_letter as a random letter from the alphabet
print(f'rnd_letter = {rnd_letter.upper()}') #prints the random letter just as a debug thing so I can see that part is working

for rnd_letter in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    print(count)
    rnd_letter = random.choice(string.ascii_letters)
    typed = input(f'Type {rnd_letter.upper()} >> ') #tells the user to type the random letter and captures their input as variable called "typed"
    count +=1
    while typed.upper() != (rnd_letter.upper()): 
        typed=input(f'Wrong! Try again! Type {rnd_letter} >> ')

