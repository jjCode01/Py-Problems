"""
The 100 prisoners problem is a mathematical problem in probability theory and combinatorics. 
In this problem, 100 numbered prisoners must find their own numbers in one of 100 drawers in 
order to survive. The rules state that each prisoner may open only 50 drawers and cannot 
communicate with other prisoners.

The code below tests the probability of the Loop Pattern resulting in a 30% success rate for 
all prisoners to find their number.
"""
import multiprocessing
import random

def game(_) -> bool:
    # 100 boxes/drawers containing a number from 1-100.
    boxes = list(range(100))

    # The boxes/drawers containing the number are placed in a random order.
    # The index of the box/drawer in the random list represents the number 
    # on the outside of the box/drawer.
    random.shuffle(boxes)

    for player in list(range(100)):
        num = player
        for _ in range(50):
            if boxes[num] == player:
                break
            num = boxes[num]
        else:
            return False    # Prisoner failed find their number

    return True # Prisoner succeeded in finding their number

if __name__ == "__main__":
    # Run the strategy multiple times and print the average success rate.
    GAMES = 100_000

    with multiprocessing.Pool() as pool:
        results = pool.map(game, range(GAMES))

    print(f'Won {sum(results):,} out of {GAMES:,} games --> {sum(results) / GAMES * 100:.2f}% success rate')

