# Collatz Conjecture (3n + 1 problem)

Reference [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)  
This program was inspired by watching a [Youtube video](https://www.youtube.com/watch?v=094y1Z2wpJg&t=319s) from Veritasium about Collatz Conjecture, and implements a function to ouput the steps for a given set of integers and plot the results to a graph.  

## Problem

This problem concerns any sequences of integers in which each term is obtained from the previous term as follows: 

* If the previous term is even, the next term is one half of the previous term (*n / 2*).
* If the previous term is odd, the next term is 3 times the previous term plus 1 (*3n + 1*).

The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.