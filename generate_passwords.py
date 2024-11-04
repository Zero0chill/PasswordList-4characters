import itertools

# Define your character set and length
charset = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = 4  # Change this to the desired password length

# Generate combinations
for password_tuple in itertools.product(charset, repeat=length):
    password = ''.join(password_tuple)
    print(password)
