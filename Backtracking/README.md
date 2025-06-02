What is Backtracking?
Backtracking is a problem-solving algorithmic technique used to find a solution by building a solution incrementally and removing those solutions that fail to satisfy the problem constraints at any point.

It’s essentially a depth-first search for finding feasible solutions in decision trees or combinatorial problems.


Complexity Analysis of Backtracking
Since backtracking algorithm is purely brute force therefore in terms of time complexity, it performs very poorly. Generally backtracking can be seen having below mentioned time complexities:

Exponential (O(K^N))
Factorial (O(N!))




✅ Cases where you don't need a for loop:
When you have only one or two choices at each step — like:

Include or exclude an element (as in subset generation)

Move forward or stay (in some binary choice problems)

Binary trees (left or right child)


Do we always need to call recursion again after removing a choice?
Answer: No — only if your problem requires exploring multiple branches (choices) at the same level.

In problems like the subsets problem (without a for loop) — yes, you typically have two recursive calls:

One where you make a choice (include the current element)

And another where you don’t make that choice (exclude it)



📍 But in other problems (like N-Queens, permutations, etc.):
You don’t necessarily call recursion again immediately after removing a choice.
Instead — you usually use a for loop to iterate through multiple choices and recurse on each one.

Example (N-Queens):
for col in range(N):
    if is_safe(row, col):
        place_queen(row, col)
        backtrack(row + 1)
        remove_queen(row, col)  # backtrack



void FIND_SOLUTIONS(parameters):

    if (valid solution):
        store the solution
        return

    for (each possible choice):
        if (valid choice):
            APPLY(choice)
            FIND_SOLUTIONS(updated parameters)
            BACKTRACK(remove choice)

    return
