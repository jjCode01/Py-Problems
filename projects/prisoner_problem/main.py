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

def loop_strategy(boxes: list, prisoners: int = 100, attempts: int = 50) -> int:
    """
    Loop strategy for the 100 Prisoners Problem.
    Should result in a success rate of greather than 30% for all
    prisoners to find their number.
    """

    # boxes = init_boxes()
    prisoners_free = 0
    for prisoner_number in list(range(prisoners)):
        box_number = prisoner_number
        for _ in range(attempts):
            if boxes[box_number] == prisoner_number:
                # Prisoner found their number within 50 attempts
                prisoners_free += 1
                break
            box_number = boxes[box_number]

    return prisoners_free

def random_strategy(boxes: list, prisoners: int = 100, attempts: int = 50) -> int:
    """
    Random strategy for the 100 Prisoners Problem.
    Should result in a less then 0% success rate for all prisoners
    to find their number.
    """

    # boxes = init_boxes()
    prisoners_free = 0
    for prisoner_number in list(range(prisoners)):
        unchecked_boxes = boxes[:]

        for _ in range(attempts):
            box_number = random.randint(0, len(unchecked_boxes) - 1)
            number_in_box = unchecked_boxes.pop(box_number)

            if prisoner_number == number_in_box:
                # Prisoner found their number within 50 attempts
                prisoners_free += 1
                break

    return prisoners_free


if __name__ == "__main__":
    # Run the strategy multiple times and print the average success rate.
    PRISONER_COUNT = 100
    ITERATIONS = 10_000
    print('########## 100 Prisoner Problem ##########')
    loop_results = []
    random_results = []

    for _ in track(range(ITERATIONS)):
        boxes = init_boxes()
        loop_results.append(loop_strategy(boxes[:]))
        random_results.append(random_strategy(boxes[:]))

    loop_group_success_count = sum(results == PRISONER_COUNT for results in loop_results)
    loop_free_prisoner_count = sum(results for results in loop_results)

    random_group_success_count = sum(results == PRISONER_COUNT for results in random_results)
    random_free_prisoner_count = sum(results for results in random_results)

    total_prisoners = ITERATIONS * PRISONER_COUNT

    console = Console()
    table = Table()
    table.title = f"\nResults: 100 Prisoner Problem\n{ITERATIONS:,} Iterations : {total_prisoners:,} Prisoners"
    table.add_column("Strategy")
    table.add_column("Group\nSuccess Count", justify="right")
    table.add_column("Group\nSuccess Rate", justify="right")
    table.add_column("Free\nPrisoners", justify="right")
    table.add_column("Individual\nSuccess Rate", justify="right")
    table.add_row(
        "Loop",
        f"{loop_group_success_count:,}",
        f"{(loop_group_success_count / ITERATIONS):.2%}",
        f"{loop_free_prisoner_count:,}",
        f"{(loop_free_prisoner_count / total_prisoners):.2%}"
    )
    table.add_row(
        "Random", 
        f"{random_group_success_count:,}", 
        f"{(random_group_success_count / ITERATIONS):.2%}", 
        f"{random_free_prisoner_count:,}",
        f"{(random_free_prisoner_count / total_prisoners):.2%}"
    )

    console.print(table)
