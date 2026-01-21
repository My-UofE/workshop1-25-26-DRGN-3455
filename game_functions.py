import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    poss_value_length = len(poss_values)
    poss_values = range(poss_values[int(1/4 * poss_value_length)],poss_values[int(3/4 * poss_value_length)])
    x = random.choice(poss_values)
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if current_val > next_val and user_input == "l": 
        return True
    elif current_val > next_val and user_input == "h": 
        return False
    
    elif current_val < next_val and user_input == "l": 
        return False
    elif current_val < next_val and user_input == "h": 
        return True
    

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    isinword = False
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                board[i] = letter
                isinword = True

    if isinword == True:
        print(f"The letter {letter} is in the word")
        return True
    else:
        print(f"The letter {letter} is not in the word")
        return False
                
            
