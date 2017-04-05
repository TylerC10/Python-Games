from random import randint

print("Welcome to the number guess game! Guess a number between 0 and 100.")

def number_guess():
    turns = 4
    lucky_number = randint(0, 100)
    
    
    while True:
        print("Go ahead and guess a number: ")
        
        try:
            user_num = int(input())
        except ValueError:
            print("Please enter a number")
            continue
        
        if user_num == lucky_number:
            print("Congratulations. You Win!")
            break
        else:
            if user_num > lucky_number:
                turns -= 1
                if turns == 0:
                    break
                print("Nope, that guess is too high. Guess again.\n Turns left: %d" % (turns))              
                    
            else:
                turns -= 1
                if turns == 0:
                    break
                print("Nope, that guess is too low. Guess again.\n Turns left: %d" % (turns))                
                
    if turns == 0:
        print("Sorry, you didn't guess the number. Try again!")
        
number_guess()