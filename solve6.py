import random

def guessGame(a, b, actual):
    guess = int(input(f"Geuss a number between {a} and {b}\n"))
    nguess = 1
    while nguess != actual:
        if guess < actual:
           guess = int(input(f"Enter the bigger number\n"))
           nguess += 1
        else:
            guess = int(input(f"Enter the smaller number\n"))
            nguess += 1
            print(f"You geussed the number in {nguess} guesses")
            return nguess

if __name__ == '__main__':
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessGame(a, b, actual1)

    print("Player 2's turn\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("Player 1 is win the match\n")
    elif g1 > g2:
        print("Player 2 is win the match\n")
    else:
        print("it is tie!\n") 

print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")