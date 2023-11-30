from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0

def check_answer(guess,answer,turns):
    """checks answer against guess. Returns the number of turns remaining"""      
    if guess>answer:
        print("Too High")
        return turns - 1
    elif guess<answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was. {answer}")
    

def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=="easy":
        global turns
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Gussing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer=randint(1,100)
    print(f"Psst, the correct an is {answer}")

    turns=set_difficulty()

    guess=0

    while guess !=answer:
        print(f"You have {turns} attempts remanining to guess the number")
        guess=int(input("Make  a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out  of guesses, you lose. ")
            return
        elif guess!=answer:
            print("guess again")

game()