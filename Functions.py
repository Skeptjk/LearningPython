#Author: https://github.com/Skeptjk/
# Licence: None - Don't steal my shit

print("\033[H\033[J", end="")

x1=input(f'lets learn about functions')
l1=1
def a1():
    l1 = 0
    while True:
        if l1 == (0):
            print('You are on the first gorbock')
        elif l1 != (0):
            print (f'you are on gorbock number {l1}')
        
        l1 +=1
        i1 = input('This will loop until you type blenkos. >')

        if i1 == "blenkos":
            break

a1()
print ('you escaped the loop! what a genius')
quit()
