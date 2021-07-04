import hashlib
import os

str_data = input("Enter string to be hashed: \n")

salt = os.urandom(32)

rst = hashlib.pbkdf2_hmac('sha256',str_data.encode(),salt,500)
pt = rst.hex()

print("The result after adding salt and iterations is: ",pt)