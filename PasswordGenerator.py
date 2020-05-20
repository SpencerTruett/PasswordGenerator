from random import seed
from random import randint
import random
import time
import string

print("Let's create a password!")
time.sleep(.5)

letters = input("How many letters should be in the password?: ")

numbers = input("How many numbers should be in the password?: ")


def random_alphaNumeric_string(lettersCount, digitsCount):
    sampleStr = ''.join((random.choice(string.ascii_letters) for i in range(lettersCount)))
    sampleStr += ''.join((random.choice(string.digits) for i in range(digitsCount)))
    
    # Convert string to list and shuffle it to mix letters and digits
    sampleList = list(sampleStr)
    random.shuffle(sampleList)
    finalString = ''.join(sampleList)
    return finalString

print("Your Password is ", random_alphaNumeric_string(int(letters), int(numbers)))