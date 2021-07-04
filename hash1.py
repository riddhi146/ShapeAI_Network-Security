import hashlib

str_data = input("Enter string to be hashed: \n")

#To generate md5 of string data

result = hashlib.md5(str_data.encode()).hexdigest()

print('The result generated after hashing is: ', result)


