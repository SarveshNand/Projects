import string
import random

pass_cnt = int(input("How many passwords? -> "))
pass_lngth = int(input("Password length? -> "))

characters = string.ascii_letters + string.digits + string.punctuation

for _ in range(pass_cnt):
    password = ""

    for _ in range(pass_lngth):
        random_char = random.choice(characters)
        password += random_char

    print(password)