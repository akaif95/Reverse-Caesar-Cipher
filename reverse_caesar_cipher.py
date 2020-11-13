#Reverse Cipher

user_message = input("Please enter the message you would like to encrypt: ")
encrpyted_message = ""


i = len(user_message) - 1

while i >= 0:
    encrpyted_message = encrpyted_message + user_message[i]
    i -= 1

print()
print("ORIGINAL MESSAGE")
print("=========================")
print(user_message)

print()
print()
print("ENCRYPTED MESSAGE")
print("=========================")
print(encrpyted_message)


























