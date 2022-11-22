#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random


myguess = 0
attempts = 0
game_won = False
#Defining constants 
GUESS_SUC = 1
GUESS_FAIL = 0

def guess_number(user_guess):
  global myguess
  global attempts
  
  if(myguess > user_guess):
    attempts-=1
    print("Too low")
    return GUESS_FAIL
  if(myguess < user_guess):
    attempts-=1
    print("Too High")
    return GUESS_FAIL
  if(myguess == user_guess):
    print("You won!")
    return GUESS_SUC 


print(art.logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
def_level = input("Choose a difficult level type 'easy' or 'hard': ")
if(def_level == "easy"):
  attempts = 10
elif(def_level == "hard"):
  attempts = 5
myguess = random.randint(1, 101)
print(myguess)
while(game_won != True):
  if((attempts != 0) ):
    print(f"You have {attempts} attempts remaining to guess a number")
    guess = int(input("Make a guess: "))
    ret = guess_number(guess)
    if(ret == GUESS_SUC):
      game_won = True
  else:
    print("You've run out of guesses, you lose!")
    game_won = True