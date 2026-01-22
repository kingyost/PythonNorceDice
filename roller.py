from random import randint as rand

def roll_dice(sides):
    """
    take in a number- 'sides', return a random number between 1 and 'sides'
    """

    try:
        if sides > 0:
            rolled = rand(1, sides)
        else:
            print("Did you just try to roll a die with 0 sides?")
    except:
        print("whoop, that wasn't a valid number. whole numbers only please.")



# TODO
def multi_roll(die, sides):
    """
    roll multiple dice of the same size, add the results and return
    """


    for each die:
        result = roll_dice(sides)
        print(f"\nResult: [ {result} ]")
        total += result


# TODO
# def roll_norse():
