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
from rich.console import Console
from rich.table import Table
from rich.progress import track

def init_boxes() -> list[int]:
    """Initialize boxes"""
     # 100 boxes/drawers containing a number from 1-100.
    boxes = list(range(100))
    random.shuffle(boxes)

    # The boxes/drawers containing the number are placed in a random order.
    # The index of the box/drawer in the random list represents the number 
    # on the outside of the box/drawer.
    return boxes

def loop_strategy(*args) -> list[bool]:
    """
    Loop strategy for the 100 Prisoners Problem.
    Should result in a success rate of greather than 30% for all
    prisoners to find their number.
    """

    boxes = init_boxes()
    prisoners_free = []
    for player_number in list(range(100)):
        box_number = player_number
        for _ in range(50):
            if boxes[box_number] == player_number:
                # Prisoner found their number within 50 attempts
                prisoners_free.append(True)
                break
            box_number = boxes[box_number]
        else:
            # Prisoner failed find their number
            prisoners_free.append(False)

    return prisoners_free

def random_strategy(*args) -> list[bool]:
    """
    Random strategy for the 100 Prisoners Problem.
    Should result in a less then 0% success rate for all prisoners
    to find their number.
    """

    boxes = init_boxes()
    prisoners_free = []
    for player_number in list(range(100)):
        unchecked_boxes = boxes[:]

        for _ in range(50):
            box_number = random.randint(0, len(unchecked_boxes) - 1)
            prisoner_number = unchecked_boxes.pop(box_number)

            if player_number == prisoner_number:
                # Prisoner found their number within 50 attempts
                prisoners_free.append(True)
                break
        else:
            # Prisoner failed find their number
            prisoners_free.append(False)
    return prisoners_free


if __name__ == "__main__":
    # Run the strategy multiple times and print the average success rate.
    ITERATIONS = 50_000
    print('########## 100 Prisoner Problem ##########')

    print("Running Loop Strategy...")
    with multiprocessing.Pool() as pool:
        loop_results = pool.map(loop_strategy, range(ITERATIONS))

    print("Running Random Strategy...")
    with multiprocessing.Pool() as pool:
        random_results = pool.map(random_strategy, range(ITERATIONS))

    print("Tabulating Loop Strategy Results...")
    loop_group_success_count = sum(all(results) for results in loop_results)
    loop_free_prisoner_count = sum(sum(results) for results in loop_results)

    print("Tabulating Random Strategy Results...\n")
    random_group_success_count = sum(all(results) for results in random_results)
    random_free_prisoner_count = sum(sum(results) for results in random_results)
    total_prisoners = ITERATIONS * 100

    console = Console()
    table = Table()
    table.title = f"Results: 100 Prisoner Problem\n{ITERATIONS:,} Iterations"
    table.add_column("Strategy")
    table.add_column("Group\nSuccess Count", justify="right")
    table.add_column("Group\nSuccess Rate", justify="right")
    table.add_column("Total\nPrisoners", justify="right")
    table.add_column("Free\nPrisoners", justify="right")
    table.add_column("Individual\nSuccess Rate", justify="right")
    table.add_row(
        "Loop",
        f"{loop_group_success_count:,}",
        f"{(loop_group_success_count / ITERATIONS):.2%}",
        f"{total_prisoners:,}",
        f"{loop_free_prisoner_count:,}",
        f"{(loop_free_prisoner_count / total_prisoners):.2%}"
    )
    table.add_row(
        "Random", 
        f"{random_group_success_count:,}", 
        f"{(random_group_success_count / ITERATIONS):.2%}", 
        f"{total_prisoners:,}", 
        f"{random_free_prisoner_count:,}",
        f"{(random_free_prisoner_count / total_prisoners):.2%}"
    )

    console.print(table)
