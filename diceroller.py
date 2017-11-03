from random import *
print('Welcome to dice roller 2.1\n')
sided=int(input('How many sides should the die have?\n'))

while sided <0:
  sided=int(input('enter a positive integer please\n'))
i=input('enter roll to roll the die, new for a new die or end to end\n')
while i != 'end':
  
  if i != 'roll' and i != 'new':
  
    
    print ('enter only roll end or new please\n')
  elif i == 'new':
    sided=int(input('how many sides should the die have?\n'))
    while sided <0:
      sided=int(input('enter a positive integer please\n'))
  else:
    
    for i in range(int(input("enter number of times to roll the dice in a row\n"))):
      print('the result of roll number',i+1, "is", randrange(sided)+1)
    

  i=input('roll, new, or end\n')
print ("Thank you for using dice roller 2.1\nCreated By Darron Anderson 10/24/2017")
