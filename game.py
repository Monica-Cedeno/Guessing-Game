"""A number-guessing game."""
import random 

answer = random.randint (1, 100)

print("hello, what's your name? >")

name = input ("> ")

print (name, "I'm thinking of a number between 1 and 100.")
print ()
print ("try to guess my number > ")

tries = 0

while True:
    guess = input (" > ")
    guess = int (guess)
    tries = tries+1

    if guess < answer: 
        print ("too low! Try again > ")
    
    
    elif guess > answer: 
        print ("too high! try again >")
    
    else:
        print ("Success!")
        print ("It only took you", tries, "tries!")
        break

