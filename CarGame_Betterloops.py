import os
os.system ("cls")


started =False

print('Welcome to the car game')

while True:
    usrcmd=input('Type a command > ').lower()
    if usrcmd == "help":
        print('''
start - to start the car
stop  - to stop the car
quit  - to exit
    ''')

    elif usrcmd == "start":
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car started, ready to go?')
        
      
    elif usrcmd == 'stop':
        if not started:
            print ('Car already stopped')
        else:
            started = False
            print('Car stopped!')
 
        
        
    elif usrcmd == 'quit':
        #gameloop = False
        break
    
    else:
        print("I don't understand that")
        
print('Thanks for playing!')
quit()