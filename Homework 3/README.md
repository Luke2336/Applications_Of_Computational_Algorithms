# Homework 3: Viterbi Algorithm

>   Practice/Real-Life Applications of Computational Algorithms, Spring 2021

## Execution

```bash
make
./viterbi [input file] [output file]
```

## Implementation

-   Since the weather is a markov model, we can use Viterbi algorithm.
-   To avoid floating-point precision error of multiplication, I use `log()` to calculate with addition and maximum.
-   For backtracking, I record the transition state of each state.

```mermaid
graph LR
subgraph t
1[sunny]
2[foggy]
3[rainy]
end
subgraph t+1
4[sunny]
5[foggy]
6[rainy]
end
1 -- 0.8 --> 4
1 -- 0.15 --> 5
1 -- 0.05 --> 6
2 -- 0.2 --> 4
2 -- 0.5 --> 5
2 -- 0.3 --> 6
3 -- 0.2 --> 4
3 -- 0.2 --> 5
3 -- 0.6 --> 6
```

