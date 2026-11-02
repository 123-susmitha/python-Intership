
import random
import string

length = int(input("Enter password length: "))
if length < 15:
    print("Password length must be at least 15 characters.")

else:

    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = string.punctuation

    
    characters = lowercase + uppercase + numbers + special

    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    
    print("\n===== PASSWORD GENERATOR =====")
    print("Generated Password:", password)
    print("Password Length:", len(password))
    print("Password generated successfully!")
