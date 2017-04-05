from random import randint
       
def dice_roll():
    lucky_number = randint(1,6) 
    my_number = randint(1, 6)
    if my_number == lucky_number:
        print("You win! Your got a matching number with a roll of %d" % (my_number))
    else:
        print("Sorry, your dice roll was %d and the lucky number was %d" % (my_number, lucky_number))
        
dice_roll()