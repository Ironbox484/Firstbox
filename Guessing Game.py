#Guessing game :)
import random

print("Hello, What's you're name homie?")
name = input()

print("Well, " + name + ", I'm thinking of a number between 1 and 20. Can you find out that number?")
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print("Take a guess.")
    guesses= int(input())

    if guesses < secretNumber:
        print("Your guess is too low.")
    elif guesses > secretNumber:
        print("Your guess is too high.")
    else:
        break #Correct answer
    
if guesses == secretNumber:
    print("Good Job, " + name + "! You guessed my number in " + str(guessesTaken) +" guesses.")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
