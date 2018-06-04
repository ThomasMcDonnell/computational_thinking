# computational_thinking

## Optimization problems
---
#### 0/1 Knapsack Problem 
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
###### Representation 
1. Each item is represented by a pair (value, weight) and the Knapsack can accommodate items with a total weight of no more than the constraint. 
2. An array, A, of lenght n, represents the set of available items. Each element of the array is an item.
3. An array, B, of lenght n, is used to indicate whether or not an item has been taken.
...=> if B[i] = 1, item A[i] is taken.
...=> if B[i] = 0, item A[i] is not taken.

#### Greedy Algorithm O(nlogn)
---
A greedy algorithm is one which follows the paradigm of making the locally optimal choice at each stage with the hope of finding a golobal optimal solution. Implementing a greedy solution to the 0/1 Knapsack problem we need to define what is ment by "best" when selecting the
best items. 
* Best by value 
* Best by least weight
* Best by highest weight:value ratio

Upon implementation you will note that the algorithm will produce different answers depending on the definition of best. The reason for this is that a sequence of locally "optimal" choices don't always yield an optimal solution. 
* There is no way to tell which "best" will yield the more optimal solution.
* You get an answer, but you don't always know weather it is the optimal solution. 
