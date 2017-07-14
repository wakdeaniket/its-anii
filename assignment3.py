from __future__ import print_function
import random
import time
guessword={'opner':'warner','wicket-keeper':'sangakara','spinner':'jadeja','fast bowler':'umesh','middle order':'raina','allronder':'ashwin','batting coach':'dravid'}
option=random.choice(guessword.keys())

print('loading....')
time.sleep(1)

print ('\n'+str(option))
word=guessword[option]

guess=' '
chance=0

while(chance<5):
 
  ch=raw_input("\nenter charater :")

  if ch not in word:
  
     print ("wrong input")
     print ("next trial")
     chance=chance+1

  else:

     guess=guess+ch
     print ("go ahead")
     chance=chance+1

  print ("chance: ",chance)

  for ele in word:
   
     if ele in guess:
       print (ele,end='')

     else:
       print ("-",end='')
  
  if(len(guess)-1)==len(set(word)):

   print ("\nu won")
   break

  if(chance==5):
   print ('you lost')
   print ('the word was :'+str(word))
         
