## Hey I'm Eliel learning to code.
## Practice Problem From https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
## Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
## tells them the year that they will turn 100 years old.

import datetime 
#variable for current year
current_year = datetime.datetime.now().year
#variables for name and age
name = str(input('Enter your name: '))
age = int(input('Enter your age: '))
result = age + current_year
print(f"{name}, the year you will turn 100 is {result}.")
