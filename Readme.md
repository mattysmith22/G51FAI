# G51FAI revision

To revise for an exam, I decided to implement many problems / algorithms by implementing them in python.

## Problems

| Problem name | location | Class | BFS | DFS | UCS | A* | Minimax | Alpha-beta |
| :-- | :-- | :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| 8-Queen | `problems.eightqueen` | `QueenProblem` | Yes | Yes | No(1) | No (1) | No (2) | No (2) |
| Nim | `problems.nim` | `NimProblem` | No(3) | No(3) | No(3) | No(3) | Yes | Yes


1. Searches have no cost in this problem
2. This problem is not adverserial.
3. This prolem is not a single-player tree search

## Using Adversarial or Tree Search algorithms

First you need to define the problem, which you can do using a problem class. You can then run it through an algorithm and attain a result

**Note:** All example code is run from the root folder of this repo in a python3 interactive terminal.

**Example 1**

```python
import problems.nim as nim
import algorithms.adversarial as adversarial
problem = nim.NimProblem(7,True) # Starting with 7 sticks, with maximising player starting first.
adversarial.minimax(problem.rootNode) #Returns 0
```

**Example 2**

```python
import problems.eightqueen as queen
import algorithms.treesearch as tree
problem = queen.QueenProblem(10) # Size of the chess board, default being 8.
tree.depthfirst(problem) #Returns solution node
```

## Viewing a graph

You should have graphviz installed on your computer in order to get this to work.
Once you have a problem you run the following command:

```python
problem.render().view()
```

The graph should then appear in a PDF viewer that is preinstalled on your computer.