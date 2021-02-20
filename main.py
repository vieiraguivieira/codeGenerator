from encrypt import *


print("ENCRYPT YOUR NAME")
print("Insert your name and get your own encrypted version!" + "\n")

name = encrypt()

print()

decrypt = input("Do you want to decrypt a name? ")
if "y" in decrypt.casefold():
    from decrypt import *
    decrypt()
else:
    print("Have a good day {}!".format(name))