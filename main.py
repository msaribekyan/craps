import random

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sum = die1+die2
    print(f"The sum of dice is {die1} + {die2} = {sum}")
    return sum

def start_game():
    # Stage 1
    sum = roll_dice()

    if sum == 7 or sum == 11:
        print("You won")
    elif sum == 2 or sum == 3 or sum == 12:
        print("You lose")
    else:
        # Stage 2
        target = sum
        print(f"Now your goal number is {target}") 
        while(True):
            sum = roll_dice()
            if sum == target:
                print("You won")
                break
            elif sum == 7:
                print("You lose")
                break

start_game()
