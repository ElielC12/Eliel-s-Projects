import datetime 
#variable for current year
current_year = datetime.datetime.now().year
#variables for name and age
name = str(input('Enter your name: '))
age = int(input('Enter your age: '))
result = age + current_year
print(f"{name}, the year you will turn 100 is {result}.")
