# some notes on recursion
## i've always understood the big idea, but was never good at implementation

 - usually is when a function calls itself to iterate easier
 - you can return a value + the function call, you don't have to just return a new function call
  - I don't understand how this works yet but I'll memorize for now
 - recursion is solving a subproblem of the large problem, and that subproblem gets smaller each iteration until it can't get any smaller
 - must include base case and recursive case (think of discrete math)

 ### 3 laws of recursion

 1. must have a **base case** 
 2. must change its state and move towards the base case
 3. a recursive algorithm must call itself, recursively