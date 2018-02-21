# Psuedocode:

# 1. declare top bounds: begin with 100
# 2. declare bottom bounds: begin with 0
# 3. guess is always the avg of top and bottom

# 4. while !correct provide interface for high low and correct:
#     4.1 case or switch statement:
#         4.1.1 high then top now equals the old guess and guess now equals avg top:bottom
#         4.1.2 low then bottom equals the old guess and guess now equals avg top:bottom
#         4.1.3 correct end game declare number

topBound = 100
botBound = 0
def guessNum (top,bot):
    return(top+bot)/2;
    
guess = guessNum (topBound,botBound)

while (answer != 'c'):
    print('Is your secret number '+ str(guess)+'?')
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (answer == 'h'):
        topBound = guess
        guess = guessNum (topBound,botBound)
    elif (answer == 'l'):
        botBound = guess
        guess = guessNum (topBound,botBound)
    elif (answer == 'c'):
        print('Game over. Your secret number was: '+ str(guess))
        break
    else:
        print('Sorry, I did not understand your input.')