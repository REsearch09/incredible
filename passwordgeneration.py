import random

character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_lenght = int(input("Parolanın uzunluğunu söyleyiniz."))
password = ""
if password_lenght >= 6:
    for i in range(password_lenght):
        password += random.choice(character)
    print(password)
else:
    print("Lütfen en az 6 haneli bi şifre seçiniz")
