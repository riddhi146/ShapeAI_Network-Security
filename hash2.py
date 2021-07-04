import hashlib

str_data = input("Enter string to be hashed: \n")

#to generate hashes of string data using 3 algos from hashlib

rst1 = hashlib.blake2s(str_data.encode()).hexdigest()
rst2 = hashlib.sha512(str_data.encode()).hexdigest()
rst3 = hashlib.sha256(str_data.encode()).hexdigest()

print('The result generated after hashing using blake2s is: ', rst1)
print('\nThe result generated after hashing using sha512 is: ', rst2)
print('\nThe result generated after hashing using sha256 is: ', rst3)