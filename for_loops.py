import os
os.system ("CLS")

for item in 'Python': #this will do each letter
    print (item)

print ('___________________')

for item1 in ['Mosh', 'John', 'Sarah' ]: #the [] makes it a list, (not sure what type.. strings? tuples?) - will print them one by one
    print (item1)
    
print ('___________________')    

for item2 in [1,2,3,4,5,6,7 ]: #the [] makes it a list, (not sure what type.. strings? tuples?) - will print them one by one as before 
    print (item2)
    
print ('___________________')      
    
for item2 in range(10): #range creates a special kind of object (not a list) that we can iterate over. 
    print (item2)
    
print ('___________________')      
    
for item3 in range(5,10): #here we control the range to go from 5 to 10. Note it's the interval not the numbers - IE this list will display 5-9 not 5-10. Doesn't include the highest number
    print (item3)
    
print ('___________________')  

for item3 in range(5,10,2): #adding a third number adds a 'step' so here we go up in 2's not 1's
    print (item3)
    
print ('___________________')  
# excercise : print the sum of all prices in an imaginary shopping cart


prices = [10,20,30]
totalprice = 0
for price in prices:
    totalprice += price
    print(totalprice)
print (f'Overall total is {totalprice}')

print ('___________________')  

total2 = 0
for i in range (1,5):
    total2 += i
    print (total2)
    
print ('___________________')  

totty = 0
for a in range (1,10):
    totty += a
    print (a)
    print (f' Totty: {totty}')
    
totty2 = [1,2,3,4,5,6,7,8,9,10]
b = 0
for totty2 in totty2:
    b += totty2
    print(f'totty2= {totty2}')
    print(f'b= {b}')
    
star = 0
for (blembo) in range (1,11):
  #  star = star + element
    print (('*') * (blembo))
    
    


    
    