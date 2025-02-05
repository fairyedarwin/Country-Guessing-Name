import random
import countries
name = input("Hello there. What is your name?")
print("Hello ",name,". Welcome to Guess the country game. All you have to do is guess the country in 12 attempts! Good luck!")
country = random.choice(countries.countries)
print("Guess the country's name")
guesses = ''
turns = 12
while turns > 0:
    failed_guesses = 0
    for char in country:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed_guesses+=1
    if failed_guesses == 0:
        print("you win!")
        print("the country is:",country)
        break
    guess = input("guess the country:")
    guesses += guess
    if guess not in country:
        turns -= 1
        print("Oops! your guess was wrong! The country is",country)
        print("you have",turns,"left")

        if turns == 0:
            print("Sorry! you were not able to guess the country. Better luck next time.")



