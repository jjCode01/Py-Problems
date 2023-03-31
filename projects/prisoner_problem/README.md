# 100 Prisoners Problem
Reference the [Wikipedia](https://en.wikipedia.org/wiki/100_prisoners_problem#:~:text=The%20100%20prisoners%20problem%20is,cannot%20communicate%20with%20other%20prisoners.) page.  
This program was inspired by watching a [Youtube video](https://www.youtube.com/watch?v=iSNsgj1OCLA) from Veritasium about the 100 Prisoner Problem, and tests the probabilities of the Loop Strategy described below. 

## Problem

The 100 prisoners problem is a mathematical problem in probability theory and combinatorics. In this problem, 100 numbered prisoners must find their own numbers in one of 100 drawers in order to survive. The rules state that each prisoner may open only 50 drawers and cannot communicate with other prisoners.  

## Strategy

### Random

If every prisoner selects 50 drawers at random, the probability that a single prisoner finds their number is 50%. Therefore, the probability that all prisoners find their numbers is the product of the single probabilities, which is a vanishingly small number.

### Loop

Not only the prisoners, but also the drawers, are numbered from 1 to 100; for example, row by row starting with the top left drawer. The strategy is now as follows:

1. Each prisoner first opens the drawer labeled with their own number.
2. If this drawer contains their number, they are done and were successful.
3. Otherwise, the drawer contains the number of another prisoner, and they next open the drawer labeled with this number. 

The prisoner repeats steps 2 and 3 until they find their own number, or fail because the number is not found in the first fifty opened drawers. 

By starting with their own number, the prisoner guarantees they are on the unique permutation cycle of drawers containing their number. The only question is whether this cycle is longer than fifty drawers.  

If each prisoner follows this strategy, the probability that all prisoners find their numbers increases to greather than 30%.
