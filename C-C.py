letter = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        char = char.lower()
        if char in letter:
            index = letter.find(char)
            new_index = (index + key) % 26
            ciphertext += letter[new_index]
        else:
            ciphertext += char  
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        char = char.lower()
        if char in letter:
            index = letter.find(char)
            new_index = (index - key) % 26
            plaintext += letter[new_index]
        else:
            plaintext += char 
    return plaintext

print("\n*** WELCOME TO CAESAR CIPHER TOOL PROGRAM ***\n")

print("Do you want to encrypt or decrypt?")
print("1. Encrypt")
print("2. Decrypt")

user_input = input("1/2: ").strip()
print()

if user_input == '1':
    print("Congrats Buddy! You're successfully in ENCRYPTION mode.\n")
    key = int(input("Enter the key (1 - 26): ").strip())
    text = input("Enter the text to encrypt: ").strip()
    print("\nEncrypted text is:")
    print(encrypt(text, key))
    print()

elif user_input == '2':
    print("Congrats Buddy! You're successfully in DECRYPTION mode.\n")
    key = int(input("Enter the key (1 - 26): ").strip())
    text = input("Enter the text to decrypt: ").strip()
    print("\nDecrypted text is:")
    print(decrypt(text, key))
    print()

else:
    print("Invalid input")
    print("Please try again")
    print("Exiting the program")
    print("Goodbye!\n")
    exit()

