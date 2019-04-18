# G51FAI revision

To revise for an exam, I decided to implement many problems / algorithms by implementing them in python.

## Using Adversarial algorithms

Problems implemented:

* Nim

Algorithms implemented:

* Minimax
* Alpha-beta

First you need to define the problem, which you can do using a problem class. You can then run it through an algorithm and attain a result

```python
import nim, adversarial
problem = NimProblem(7,True) # Starting with 7 sticks, with maximising player starting first.
minimax(problem.rootNode) #Returns 0
```

## Viewing a graph

You should have graphviz installed on your computer in order to get this to work.
Once you have a problem you run the following command:

```python
problem.render().view()
```

The graph should then appear.