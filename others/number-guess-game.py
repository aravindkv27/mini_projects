import random
print("""
   ____                     _               _   _                 _               
  / ___|_   _  ___  ___ ___(_)_ __   __ _  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __| | '_ \ / _` | |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \ | | | | (_| | | |\  | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/_|_| |_|\__, | |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                    |___/                                         
""")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100 ")
answer=random.randint(1,101)
print(f"The correct answer is {answer}")

def easy(number):
    attempts=10
    
    while attempts>0:
        print(f"You have {attempts} attempts to find a correct number.")
        guess=int(input("Guess a number: "))
        if number>guess:
            attempts-=1
            print("Too Low\nGuess again")
        elif number<guess:
            attempts-=1
            print("Too High\nGuess again")
        else:
            attempts=0
            print("The number guessed is correct")
            print("You Win.")
    if attempts==0:
        print(f"You Lose! answer is {number}\nTry Again")

def hard(number):
    attempts=5
    while attempts>0:
        print(f"You have {attempts} attempts to find a correct number.")
        guess=int(input("Guess a number: "))
        if number>guess:
            attempts-=1
            print("Too Low\nGuess again")
        elif number<guess:
            attempts-=1
            print("Too High\nGuess again")
        else:
            attempts=0
            print("The number guessed is correct")
            print("You Win.")
    if attempts==0:
        print(f"You Lose! answer is {number}\nTry Again")
con=True
while con:
    option=input("Choose a Difficulty level Easy or hard\n").lower()
    number=random.randint(1,101)
    print(number)
    if option=="easy":
        easy(number)
    elif option=="hard":
        hard(number)
    new_game=input("Play again? Yes or No: ")
    if new_game=='no':
        con=False
        
