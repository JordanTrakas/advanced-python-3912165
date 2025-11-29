# Example file for Advanced Python by Joe Marini
# Using the built-in string constants

import string
import secrets

# built-in constants for a variety of needs
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.punctuation)


# Define a test string
# testStr = "The quick brown fox jumps OVER the lazy dog."
# testStr = "The quick brown fox jumps OVER the lazy dog"

# use an iterator to see if a string contains any punctuation 
# if any(c in string.punctuation for c in testStr):
#     print("The string contains punctuation")
# else:
#     print("No punctuation found")

# generate a secure random password
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(10))
# print(password)

# Check the strength of a password
def check_password_strength(test_pass):
    if (len(test_pass) >= 10 and
        any(char in string.punctuation for char in test_pass) and
        any(char in string.digits for char in test_pass) and
        any(char in string.ascii_letters for char in test_pass)):
        return f"{test_pass} is a strong password."
    else:
        return f"{test_pass} is a weak password."

print(check_password_strength("MyTestPa$$123!"))
print(check_password_strength("password"))
print(check_password_strength("pa$$w0rd!"))
