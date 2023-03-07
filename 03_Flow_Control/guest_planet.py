#While Loops

correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"



# if guess == planet:
#     print("Right guess! Louis is at Zortan")
# else:
#     print("Louis Says: Wrong planet guess again")

# But keeps the input string case sensitive. How do we change that?


# if guess.lower() == planet.lower():
#     print("Right guess! Louis is at Zortan")
# else:
#     print("Louis Says: Wrong planet guess again")

#But how can we keep guessing without havivng to run the program over?
#WHILE LOOPS:

while True:
    guess = input("Louis Says: Can you guess my planet? >>>")
    if guess.lower() == planet.lower():
        print("Right guess! Louis is at Zortan")
        break
    else:
        print("Louis Says: Wrong planet guess again")