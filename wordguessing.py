import random
import countries
name = input("Hi there. Welcome to the game! May I know your name please?")
print("Hello ",name,". All you have to do is guess the country in 10 attempts! Good luck!")
country = random.choice(countries.countries).lower()
print("Guess the country's name")
guesses = ''
turns = 10
guessed = "_"*len(country)
usr_guess=""
while turns > 0:
    guess = input(f"Guess the country:{guessed}")
    guessed= ""
    if guess in country:
        for char in country:
            if char == guess or char in usr_guess:
                guessed+=char
                usr_guess +=char
            else:
                guessed+="_"
        print("You guessed right!")
    else:
        print("Oops.. Try again. You have ",turns,"more attempts")
    turns -=1
    if guessed == country:
        print("You won, the country is indeed",country)
        break
    if turns == 0 and guessed != country:
        print("You lose. The country is ",country,". Better luck next time.")
        break
