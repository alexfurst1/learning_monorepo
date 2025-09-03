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

  - the memory bookkeeping is due to the call stack, which stacks up until the base case is it then collapses back down
   - kind of difficult to remember at first. Try to memorize and it will click eventually after repetition.
 - how list_sum works, and other recursive problems work is that it doesn't add each element to the first index as it goes. instead,
 it isolates each int in memory, all seperate im the stack, and then when all items have been seperated it adds them together afterwards, backwards, in the form of a stack. Hence the call stack.

 - honestly I could care less about binary and hexadecimal, and so I'm just not going to learn it now. i really hope that doesn't bite
 me in the ass later on

 - same with fractals this stuff is boring me so much
 - god I hate recursion

