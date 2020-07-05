import string
import random

character_set = string.punctuation + string.ascii_letters + string.digits

def password_gen(length):
    password = ""
    for digit in range(length + 1):
        password += random.choice(character_set)
    print(password)

password_gen(15)