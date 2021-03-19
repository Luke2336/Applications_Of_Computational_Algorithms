# Homework 1: Solving Sudoku by SAT

> Practice/Real-Life Applications of Computational Algorithms, Spring 2021


## Run

1. `g++ -std=c++17 -o solver solver.cpp`
2. `./solver [Input Filename] [Output Filename] ./MiniSat_v1.14_linux`

### Input Spec

1. has a size 𝑁x𝑁, and
2. is prefilled with numbers 0 to 𝑁, where 0 represents the square is empty.

```
0 6 0 1 0 4 0 5 0
0 0 8 3 0 5 6 0 0
2 0 0 0 0 0 0 0 1
8 0 0 4 0 7 0 0 6
0 0 6 0 0 0 3 0 0
7 0 0 9 0 1 0 0 4
5 0 0 0 0 0 0 0 2
0 0 7 2 0 6 9 0 0
0 4 0 5 0 8 0 7 0
```

### Output Spec

1. A 𝑁x𝑁 filled puzzle.
2. If the input is not solvable, then the output will be "NO".
