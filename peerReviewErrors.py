# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Kyle Melroy
# Creation Date: 8/1/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors. You need to identify the issues and correct them.

import random
import time

def displayIntro():
   print('''You are in a land full of dragons.
In front of you, you see two caves.
In one cave, the dragon is friendly and will share his treasure with you.
The other dragon is greedy and hungry, and will eat you on sight.''')
#Edited format of text, displayed weird. 
   print()

def chooseCave():
   cave = ''
   while cave != '1' and cave != '2':
     #while cave != '1' and cave != '2': had incorrect indentation error
       print('Which cave will you go into? (1 or 2)')
       cave = input()

   #return caves, there's no caves variable.
   return cave


def checkCave(chosenCave):
   print('You approach the cave...')
   #sleep for 2 seconds
   time.sleep(2)
   print('It is dark and spooky...')
   #sleep for 2 seconds
   time.sleep(2)
   #time.sleep(3), note says sleep for 2 seconds, but this was 3 seconds.
   print('A large dragon jumps out in front of you! He opens his jaws and...')
   print()
   #sleep for 2 seconds
   time.sleep(2)
   friendlyCave = random.randint(1, 2)

   if chosenCave == str(friendlyCave):
       print('Gives you his treasure!')
   else:
       print( 'Gobbles you down in one bite!')
       #print 'Gobbles you down in one bite!', statement was missing ()

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
#while playAgain = 'yes' or playAgain = 'y': was missing an = on each to make it a conditional statement.
   displayIntro()
   caveNumber = chooseCave()
   #caveNumber = choosecave(), incorrect function was called

   checkCave(caveNumber)

   print('Do you want to play again? (yes or no)')
   playAgain = input()
   if playAgain == "no":
       print("Thanks for playing")
       #print("Thanks for planing"), corrected to say "Thanks for playing"
