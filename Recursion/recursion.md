Recursion: 

A recursive definition of an entity defines the entity in terms of itself.

Recursion is a very important problem-solving approach that is an alternative to iteration (remember that iterative solutions include loops).

     The idea: Each successive recursive call should bring you one step closer to a situation in which the problem can easily be solved. Each recursive definition has two separate parts: a base case and a general (or recursive) case.

1.     The easily solved situation is called the  base case. The base case is a simple case of the problem that we can answer directly; the base case does NOT use recursion. Each recursive algorithm must have at least one base case. Without at least one base case --> infinite recursion.

2.     The general (recursive) case is the more complicated case of the problem that isn't easy to answer directly, but can be expressed elegantly with recursion. The general case is the place where the recursive calls are made --> written so that with repeated calls it reduces to the base case (or brings you closer to the base case). Must eventually be reduced to a base case; if not --> infinite recursion. Must have at least one general case --> if not, no recursion!

General format for recursive functions:

if(some easily-solved problem) // base case
    solution statement
else                        // general case
    recursive function call

Direct recursion = the method is calling itself. A method that calls another method and eventually results in the original method call is called indirectly recursive. a calls -> b and b -> calls a. 

Indirect recursion = the method calls another method and eventually results in the original method call. Indirect recursion requires the same careful analysis as direct recursion. Tracing through indirect recursion can be a tedious process.

Use cases: 

·       The examples listed here could all have been written without recursion, by using iteration instead.  The iterative solution uses a loop, and the recursive solution uses an if statement. However, for certain problems the recursive solution is the most natural solution.

·       Recursion is a very important tool in supporting data abstraction. Recursive definitions are often necessary to define data and associated operations, and the recursive functions are (in many cases) the natural solution for the implementation of the operations on data.

·       Drawbacks of recursion: the amount of stack space used to implement recursion and possible redundancy. Every recursive method call produces a new instance of the method (with a new set of local variables and parameters).  Each set of local variables and parameters related to the current call is stored on the stack, to be picked up on return. For example, the recursive implementation for the factorial method is a good example for its simplicity, but not a practical solution (huge overhead --> huge usage of stack space).

·       There are no absolute rules when choosing between a recursive or an iterative solution. The most powerful benefit of recursive methods is the fact that they are concise, which makes them easier to maintain and read. On the other hand, recursive methods consume time and computer storage, which means that they may not be very efficient. These are some guidelines when considering the alternatives:

1.     Design a recursive method if the problem is stated recursively and the recursive algorithm is less complex. Keep in mind that in many cases, recursion is a technique that reduces the complexity of the algorithms you want to implement.

2.     Design an iterative method if similar complexities for the recursive and the iterative algorithms (the iterative solution is likely to be more efficient)

In many cases the choice is not very clear (concise vs. efficient). More experienced designers know when efficiency really matters and when it is less important.

Can use sub-problem,s like if calculating n, we can use n-1 to solve it. 