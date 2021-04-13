"""
You are welcome to use this as you wish
"""

import random #Imports random library.

score = 0 #Initializes score.

def game(score): #Defines the function. This is so we can call it again to play again.

    target = random.randint(0,100) #This is the target (the number you have to guess).
                                   #If you want to change the number (Currently it is from 1 to 100), change the second number.
                                   #The first number is the minimum, the second is the maximum.

    print("Guess the number!") #This prints out the "Guess the number!" token when you start a new game.

    while True: #While loop. DO NOT TOUCH THIS!

        try: #This is so when you enter anything that is not an integer (a whole number), it prints out "ONLY ENTER INTEGERS!"

            userInput = int(input()) #This is the user input

            if userInput < target: #If user input is less than the target it prints out "Too low!"
                print("Too low!") #This prints out "Too low!"
            
            elif userInput > target: #If user input is higher than the target it prints out "Too high!"
                print("Too high!") #This prints out "Too high!"
            
            elif userInput == target: #If user input is equal to the target (in other words, you guessed the number) it prints out "Correct!"
                print("Correct!") #This prints out "Correct!"
                
                score = score + 1 #This adds one to the score (because you got it correctly).

                print(f"Score = {score}") #This prints out your current score.

                game(score) #This restarts the game (the reason we put the entire thing in a function).
        
        except ValueError: #This handles the error that shows up if you enter anything other than an integer.
            print("WARNING: ONLY ENTER INTEGERS!") #This prints out "WARNING: ONLY ENTER INTEGERS!" to let you know that only integers are allowed.

game(score) #This calls the function (Starts the game).
