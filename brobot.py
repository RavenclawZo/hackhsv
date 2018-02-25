import random
import sys
def guessing_game():
    number = random.randint(1, 10)
    tries = 1
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))
    if guess > number:
        print("Guess Lower")
    if guess < number:
        print("Guess Higher")
    while guess != number:
        tries += 1
        guess = int(input("Try Again: "))
        if guess > number:
            print("Guess Lower")
        if guess < number:
            print("Guess Higher")
    if guess == number:
        print("Hey, you got it right! The number was", number, \
              "and it only took you", tries, "tries!")
        print("Thanks for playing with me :^) See ya later!")
        sys.exit()
#________________________________________________________________________________
def rps():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()
#Define Function when computer chooses rock
def computer_choice_rock():
    user_choice = input("Rock, paper, scissors -- ")
    if "rock" in user_choice.lower():
        print("You Tie. You chose rock and I chose rock.")
        try_again()
    if "paper" in user_choice.lower():
        print("You Win! You chose paper and I chose rock.")
        try_again()
    if "scissor" in user_choice.lower():
        print("You Lose! You chose scissors and I chose rock.")
        try_again()
    else:
        print("Try Again")
        computer_choice_rock()
#Define function when computer chooses paper
def computer_choice_paper():
    user_choice = input("Rock, paper scissors -- ")
    if "rock" in user_choice.lower():
        print("You Lose! You chose rock and I chose paper.")
        try_again()
    if "paper" in user_choice.lower():
        print("You Tie. You chose paper and I chose paper.")
        try_again()
    if "scissor" in user_choice.lower():
        print("You Win! You chose scissors and I chose paper.")
        try_again()
    else:
        print("Try Again")
        computer_choice_paper()
#Define function when computer chooses scissors
def computer_choice_scissors():
    user_choice = input("Rock, paper scissors --")
    if "rock" in user_choice.lower():
        print("You Win! You chose rock and I chose scissors.")
        try_again()
    if "paper" in user_choice.lower():
        print("You Lose! You chose paper and I chose scissors.")
        try_again()
    if "scissor" in user_choice.lower():
        print("Aw, it's a tie! You chose scissors and I chose scissors.")
        try_again()
    else:
        print("Try Again")
        computer_choice_scissors()
#Define the Try Again function
        
def try_again():
    choice = input("Would you like to play again?")
    if "ye" in choice.lower() or "sure" in choice.lower() or "ok" in choice.lower() or "alright" in choice.lower():
        rps()
    elif "no" in choice.lower() or "na" in choice.lower() or "don't want" in choice.lower() or "dont want" in choice.lower():
        print("Thank you for playing!")
        sys.exit()
    else:
        print("I'm sorry, that doesn't quite answer my question. Try retyping your answer.")
        try_again()
        
        
#________________________________________________________________________________
        
        
        
# What is your name?
h = 0
greetings = ["Hello", "Nice to meet you", "Welcome",]
name = input("Hello, what is your name?\n")
print(random.choice(greetings), name + "." + " My name is Brobot!")
# how are you feeling
print("How are you doing today", name + "?")
r = input()
h = 0
while h == 0:
    if "a-ok" in r.lower() or "good" in r.lower() or "great" in r.lower() or "awesome" in r.lower() or "cool" in r.lower() or "well" in r.lower():
        responses = ["Nice", "Yeah", "Great", "Good", "YAY", "Woohoo"]
        response = random.choice(responses)
        print(response + "! I'm feeling good, too!")
        h = 1
    elif "ok" in r.lower() or "fine" in r.lower() or "alright" in r.lower():
        print ("Just okay? Hopefully your day brightens up a bit.")
        h = 1
    elif "bad" in r.lower() or "not good" in r.lower() or "terrible" in r.lower or "horrible" in r.lower() or "worst" in r.lower() or "not well" in r.lower():
        print ("What's wrong?")
        input()
        kk = ["I'm sorry :(", "That sucks :("]
        kl = random.choice(kk)
        h = 1
    else:
        print ("Sorry, I can't quite understand that. Could you try rephrasing it?")
    
print("Do you want to play a game?")
k = input()
h = 0
while h == 0:
    if "ye" in k.lower() or "ya" in k.lower() or "sure" in k.lower() or "ok" in r.lower():
        rpsgame = input("Which game do you wanna play? Guessing Number game or Rock Paper Scissors? \n")
        if "rock" in rpsgame.lower() or "paper" in rpsgame.lower() or "scissor" in rpsgame.lower() or "rps" in rpsgame.lower() and "do" in rpsgame.lower() or "want" in rpsgame.lower():
            rps()
            h = 1
        elif "guess" in rpsgame.lower() or "game" in rpsgame.lower() or "num" in rpsgame.lower():
            guessing_game()
            h = 1
    elif "na" in k.lower() or "no" in k.lower():
        print("Then what do you want to do?")
        s = input()
        h = 1
        if "nothing" in s.lower():
            print ("Awww man. Bye.")
        elif "dont know" in s.lower() or "not sure" in s.lower() or "dunno" in s.lower() or "no idea" in s.lower():
            print("Yeah, me neither. It's been fun talking to you though! :) Bye!")
            sys.exit()

        else:
            print("Could you try rephrasing that? I can't quite understand what you're saying :(")    
