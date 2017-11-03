from random import *
print('Welcome to dice roller 2.1\n')
sided=-1
i=input('enter roll to roll the die, new for a new die, end to end, \nor input in dnd standerd form\n')
while i != 'end':
  if 'd' not in i or i =='end':
    if i != 'roll' and i != 'new':
    
    
     print ('enter only roll end or new please\n')
    elif i == 'new':
      sided=int(input('how many sides should the die have?\n'))
      while sided <0:
        sided=int(input('enter a positive integer please\n'))
    else:
      if(sided==-1):
        print('How many sides should the die have\n')
      while sided <0:
        sided=int(input('enter a positive integer please\n'))
      for i in range(int(input("enter number of times to roll the dice in a row\n"))):
        print('the result of roll number',i+1, "is", randrange(sided)+1)
  elif isinstance(int(i[:i.index('d')]),int) and isinstance(int(i[i.index('d')+1:]),int):
    for e in range(int(i[:i.index('d')])):
      d=i.index('d')
      print('the result of roll number',e+1, "is", randrange(int(i[d+1:]))+1)

  i=input('roll, new, or end or dStand\n')
print ("Thank you for using dice roller 3.0\n Created By Darron Anderson 11/3/2017")

  
