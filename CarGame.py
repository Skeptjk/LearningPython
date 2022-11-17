import os
os.system ("cls")

#gameloop = True
carstarted =False

print('Welcome to the car game')

while True:
    usrcmd=input('Type a command > ').lower()
    if usrcmd == str("help"):
        print('''
start - to start the car
stop  - to stop the car
quit  - to exit
    ''')

    elif usrcmd == "start" and carstarted == False:
        print('Car started, ready to go?')
        carstarted = True
    
    elif usrcmd == "start" and carstarted == True:
        print('Car is already started!')
    
    elif usrcmd == 'stop' and carstarted == True:
        print('car stopped')
        carstarted = False
        
    elif usrcmd == 'stop' and carstarted == False:
        print('car is already stopped!')
        carstarted = False
        
    elif usrcmd == 'quit':
        #gameloop = False
        break
    
    else:
        print("I don't understand that")
        
print('Thanks for playing!')
quit()