import sys
import fileIO
import solver

sys.setrecursionlimit(10000)
Puzzle = fileIO.read_input(sys.argv[1])
fileIO.write_output(sys.argv[2], solver.solve(Puzzle))