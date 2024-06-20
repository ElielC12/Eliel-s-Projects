from faker import Faker
import string, random

# Initialize the Faker library
fake = Faker()

print('Welcome to Password Generator')
print('''Select your password strength: 
                 1. Weak
                 2. Strong ''')

# Select the strength of the password
strength = int(input('Pick a number: '))
password = []

# If the user selects '1' for a weak password
if strength == 1:
    # Generate two random words using Faker
    word1 = fake.word()
    word2 = fake.word()
    # Concatenate the two words and add them to the password list
    password.append(word1 + word2)

# If the user selects '2' for a strong password
elif strength == 2:
    # Create a list of characters including letters, digits, and punctuation
    characterList = string.ascii_letters + string.digits + string.punctuation
    # Loop 12 times to generate a strong password with 12 random characters
    for i in range(12):
        # Choose a random character from the character list
        randomchar = random.choice(characterList)
        # Add the random character to the password list
        password.append(randomchar)

# Print the generated password by joining the list into a single string
print(f"Your new password is " + "".join(password))