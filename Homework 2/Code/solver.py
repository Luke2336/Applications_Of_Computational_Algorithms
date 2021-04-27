from pyeda.inter import *
import math
import itertools


def solve(Puzzle):
    n = len(Puzzle)
    sq = int(math.sqrt(n))
    X = exprvars('x', (1, n + 1), (1, n + 1), (1, n + 1))
    V = And(*[
        And(*[
            OneHot(*[X[r, c, v] for v in range(1, n + 1)])
            for c in range(1, n + 1)
        ]) for r in range(1, n + 1)
    ])
    R = And(*[
        And(*[
            OneHot(*[X[r, c, v] for c in range(1, n + 1)])
            for v in range(1, n + 1)
        ]) for r in range(1, n + 1)
    ])
    C = And(*[
        And(*[
            OneHot(*[X[r, c, v] for r in range(1, n + 1)])
            for v in range(1, n + 1)
        ]) for c in range(1, n + 1)
    ])
    B = And(*[
        And(*[
            OneHot(*[
                X[sq * br + r, sq * bc + c, v] for r in range(1, sq + 1)
                for c in range(1, sq + 1)
            ]) for v in range(1, n + 1)
        ]) for br in range(sq) for bc in range(sq)
    ])
    P = And(*[
        X[r + 1, c + 1, Puzzle[r][c]]
        for r, c in itertools.product(range(n), repeat=2) if Puzzle[r][c] > 0
    ])
    Fun = And(V, R, C, B, P)
    return Fun.satisfy_count()