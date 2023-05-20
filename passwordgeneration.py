import random

character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_lenght = int(input("Parolanın uzunluğunu söyleyiniz."))
password = ""
for i in range(password_lenght):
    password += random.choice(character)
print(password)
