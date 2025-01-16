#1Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).
def convert_to_binary(num):
    binary = "" 
    if num < 0:
        print("Please enter a positive integer!")
        return None 
    
    while num > 0:
        remainder = num % 2  
        binary = str(remainder) + binary
        num = num // 2  
    return binary

num1 = int(input("Enter a positive integer: "))
binary_number = convert_to_binary(num1)

if binary_number:
    print(f"Binary representation of {num1} is: {binary_number}")


#2. Write and test a function that takes an integer as its parameter and returns the
#factors of that integer. (A factor is an integer which can be multiplied by another to yield the original).
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:  
            factors.append(i)
    return factors

num = int(input("Enter an integer: "))
factors = get_factors(num)
print(f"The factors of {num} are: {factors}")



#3. Write and test a function that determines if a given integer is a prime number. A
#prime number is an integer greater than 1 that cannot be produced by multiplying two other integers.
def prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:  
            return False  
    
    return True

number = int(input("Enter a positive integer: "))
if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")



#4. Computers are commonly used in encryption. A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message
#and reverse the resulting string. Write, and test, a function that takes a string containing a message and "encrypts" it in this way.
def encrypt_message(mssg):
    encrypted_msg = mssg.replace(" ", "")[::-1]
    return encrypted_msg

message = input("Type word or sentence for encryption: ")
print(encrypt_message(message))


#5. Another way to hide a message is to include the letters that make it up within seemingly random text. The letters of the message might be every fifth characte
#for example. Write and test a function that does such encryption. It should randomly generate an interval (between 2 and 20), space the message out accordingly, and should fill the gaps with random letters. The function should return the encrypted message and the interval used.
import random

def encrypt_message_with_key(message):
    interval = random.randint(2, 20)
    encrypted_message = []
    key = []  
    
    for i in range(len(message)):
        if i % interval == 0:
            encrypted_message.append(message[i])
        else:
            encrypted_message.append('x')
            key.append(message[i])  
    
    encrypted_message_str = ''.join(encrypted_message)
    return encrypted_message_str, interval, key


message = input("Enter the message for encryption: ")
encrypted_message, interval, key = encrypt_message_with_key(message)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval: {interval}")
print(f"Key: {key}")




#6. Write a program that decrypts messages encoded as above
def decrypt_message_with_key(encrypted_message, interval, key):
    decrypted_message = []
    key_index = 0

    for i in range(len(encrypted_message)):
        if i % interval == 0:
            decrypted_message.append(encrypted_message[i])  # Use the retained character
        else:
            decrypted_message.append(key[key_index])  # Use characters from the key
            key_index += 1

    return ''.join(decrypted_message)

encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the encryption interval: "))
key = input("Enter the key (comma-separated): ").split(',')

original_message = decrypt_message_with_key(encrypted_message, interval, key)

print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted (Original) Message: {original_message}")