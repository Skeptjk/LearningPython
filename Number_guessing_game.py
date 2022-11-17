import random
lives = 3
secretnumber= (random.randint (1,10))
#secretnumber = 5 // define the secret number rather than use random for testing purposes 
# print (secretnumber) // show the secret number at the start of the game for testing purposes
print ('Secret number has been selected! You have 3 lives. Can you guess it?')
guess = input ('Take a guess! ')


while int(guess) != secretnumber and lives !=0:
    lives=lives-1
    print(f'You guessed {guess} - sorry, wrong answer!')
    if secretnumber > int(guess):
        print(f'The secret number is higher than {guess}!')
    elif secretnumber < int(guess):
        print(f'The secret number is lower than {guess}')
    guess=input(f'Try again! You have {lives} lives remaining ')
    
    
if lives == 0 and int(guess) != secretnumber:
    print(f'You ran out of lives! The secret number was {secretnumber} Sorry, game over!')
    quit()
    
elif int(guess) == secretnumber:
    print(f'You did it! The secret number was {secretnumber} and you guessed it with {lives} lives remaining ')
    
 
