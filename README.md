# lesson 1 

# how to write function in py 

# Function to print a greeting message
# def greet():
#     print("Hello! Welcome to Python.")

# Function to add two numbers
# def add_numbers(a, b):
#     return a + b

# Function to greet a user with a default name
# def greet_user(name="Guest"):
#     print(f"Hello, {name}!")

# Function to multiply three numbers
# def multiply(a, b, c):
#     return a * b * c

# Function to calculate sum and difference
# def calculate(a, b):
#     sum_result = a + b
#     diff_result = a - b
#     return sum_result, diff_result

# Calling functions
# greet()

# Calling add_numbers function
# sum_result = add_numbers(5, 3)
# print("Sum:", sum_result)

# Calling greet_user function
# greet_user("Alice")
# greet_user()

# Calling multiply function
# product = multiply(2, 3, 4)
# print("Product:", product)

# Calling calculate function
# sum_val, diff_val = calculate(10, 4)
# print("Sum:", sum_val)
# print("Difference:", diff_val)


#############################################################################

# lesson 2

# .lower() = change the alphabets to lowercase 
# .upper() = change the alphabets to uppercase
# .title() = change the first alphabets to uppercase and rest to lowercase
# .strip() = remove the spaces from the string
# .split() = split the string into a list of words
# .join() = join the list of words into a string
# .replace() = replace the word with another word
# .find() = find the index of the word in the string
# .count() = count the number of times the word appears in the string

#############################################################################

# lesson 3


#############################################################################

# SOURCE CODE 

# letter = 'abcdefghijklmnopqrstuvwxyz'
# num_letter = len(letter)

# def encrypt(plaintext,key):
#     ciphertext = ''
#     for letter in plaintext : 
#         letter = letter.lower()
#         if not letter == '' :
#             index = letter.find(letter)
#             if index == -1 : 
#                 ciphertext += letter
#             else :
#                 new_index = index + key 
#                 if new_index >= 26 :
#                     new_index = new_index - 26
#                     ciphertext += letter[new_index]
#                     return ciphertext
                
# def decrypt(ciphertext,key) : 
#     plaintext = ''
#     for letter in ciphertext :
#         letter = letter.lower()
#         if not letter == '' :
#             index = letter.find(letter)
#             if index == -1 :
#                 plaintext += letter
#             else :
#                 new_index = index - key
#                 if new_index < 0 :
#                     new_index = new_index + 26
#                     plaintext += letter[new_index]
#                     return plaintext


# print( )
# print('*** WELCOME TO CAESER CIPHER TOOL PROGRAM ***' )
# print( )

# print('Do you want to encrypt or decrypt ?')
# print('1. Encrypt')
# print('2. Decrypt')

# user_input = input('1/2: ')
# print()

# if user_input == '1' :
#     print('Congrats Buddy Ur successfully enter to ENCRYPTION mode ')
#     print()
#     key = int(input('Enter the key ( 1 - 26 ): '))
#     text = input('Enter the text to encrypt : ')
#     print()
#     print('Encrypted text is : ')
#     print(encrypt(text,key))


# elif user_input == '2' : 
#     print('Congrats Buddy Ur successfully enter to DECRYPTION mode ')
#     print() 
#     key = int(input('Enter the key ( 1 - 26 ): '))
#     text = input('Enter the text to decrypt : ')
#     print()
#     print('Decrypted text is : ')
#     print(decrypt(text,key))

# else :
#     print('Invalid input')
#     print('Please try again')
#     print('Exiting the program')
#     print('Good Bye')
#     print()
#     exit()


##################################################################################
    




