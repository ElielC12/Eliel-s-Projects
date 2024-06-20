from faker import Faker
import string, random

fake = Faker()

print('Welcome to Password Generator')
print('''Select your password strenght: 
                 1. Weak
                 2. Strong ''')
#Selects the strenght of the password
strenght = int(input('Pick a number: '))
password = []
#This option generates two random words and appends to a list
if strenght == 1:
    word1 = fake.word()
    word2 = fake.word()
    password.append(word1 + word2)
#This option uses ascii letters, digits and punctuation
elif strenght == 2:
    characterList = string.ascii_letters + string.digits + string.punctuation
    #Loops trough characterList and appends to password
    for i in range(12): 
        randomchar = random.choice(characterList)
        password.append(randomchar)
#Prints the password      
print(f"Your new password is " + "".join(password))
