# algoritmic-potato
repo for algorithms and data structures

---

**Data Structures :** DS is a way of organizing data so that it can be used effectively.

**Abstract Data Type :** ADT is an abstraction of a data structure which provides only the interface to which a data structure must adhere to

List    (Abstraction) > Dynamic array linked list (Data Structure)

Queue   (Abstraction) > Linked list based queue, array based queue, stack based queue (Data Structure)

Map     (Abstraction) > Tree map, hash map/ hash table (Data Structure)

Vehicle (Abstraction) > Golf cart, bicycle, smart car (Data Structure)


## Computational Complexity Analysis
1. How much time does this algorithm need to finish?
2. How much space does this algorithm need for its computation?

> **Big-O** notation gives an upper bound of the complexity in the *worst* case, helping to quantify performance as the input size becomes *arbitrarily large*.
> *(n The size of the input, order is from complex to simle)*
>   * O(1)       : Constant Time
>   * O(log(n))  : Logaritmic Time
>   * O(n)       : Linear Time
>   * O(nlog(n)) : Linearitmis Time
>   * O(n^2)     : Quadratic Time
>   * O(n^3)     : Cubic Time
>   * O(b^n)     : Exponential Time, b>1
>   * O(n!)      : Factorial Time 

> **Big-O Properties**
>   * O(n + c) = O(n)
>   * O(cn) = O(n), c>0
>   * for the function : f(n) = 7log(n)^3 + 15n^2 + 2n^3 + 8, Big-O notation is : O(f(n)) = O(n^3)
>   * Finding all subsets of a set - O(2^n)
>   * Finding all permutation of a string - O(n!)
>   * Sorting using mergesort - O(nlog(n))
>   * Iterating over all the cells in a matrix of size n by m - O(nm)

## Extra Info Section

```
A static array is a fixed length container containing n elements indexable from the range [0, n-1]    

When and where is a static array used?
    > Sorting and accessing sequential data
    > Temporarily storing objects
    > Used by IO routines as buffers
    > Lookup tables and inverse lookup tables
    > Can be used to return multiple values from a function
    > Used in dynamic programming to cache answers to subproblems
```

```
How can we implement a dynamic array?

    Method 1:
        i-   Create a statica array with an initial capacity
        ii-  Add elements to the underlying static array, keeping track of the number of elements.
        iii- If adding another element will exceed the capacity, 
                then create a new static array with thice capacity and copy the original elements into it.
```
