---
title: "How I (finally) Grokked Recursion"
date: 2023-05-30T18:53:14+01:00
draft: false
---

Recursion is one of those concepts that you either grasp or you don't. Conceptually, recursion is as simple as a function calling itself. 
However, understanding the intricacies of how, when, and why to use recursion can be challenging. Two influential factors that 
aided my understanding were [this book](https://media.pragprog.com/newsletters/2020-08-13.html) and learning Clojure.

## A Starter for Ten

Suppose we want to write a program for a rocket launch which counts down from ten to zero before taking off. Most of us (myself included)
would write a loop starting at ten and decrement a counter in each iteration only stopping when we reach zero; but there is also another
way to do this. Enter recursion. Instead of using a loop, we can have our function call itself with ever decreasing arguments until we hit
a base case. The base case is the condition under which we want our function to stop calling itself and return.

```python
def blast_off(num):
    print(num)
    time.sleep(1)

    if num == 0:
        print('BLAST OFF!')
        return

    return blast_off(num - 1)
```

The above example prints its argument to the console (in this case a number). Next it checks whether the number is zero. If it is the
function returns. This is called the base case. In any other scenario, the function simply calls itself with its own argument but decremented 
by one. Eventually, we will call ourself with an argument of zero, satisfy the condition of our base case and exit our function.

The way this works though is interesting. Each time the function is called, that call is pushed onto the call stack just like any other function.
The difference here though is that multiple calls of our function will be added to the stack until the base case is satisfied and the function
returns. At this stage, all other invocations of the function will return and be popped from the stack in the opposite order that they 
were pushed onto the stack.

## The Three Steps

### Make Believe

The first step to easily solving problems with recursion is to stop thinking about recursion. Make the assumption that the implementation of
your function already exists and works correctly.

### Off by One

Next up, figure out what the solution would be for the penultimate solution. For example, lets say we want to create a recursive function
that returns a factorial of a given number `n`. The penultimate step in this solution would simply be to call our function with `n` being one smaller
that the final case i.e. `factorial(n - 1)`. All we have to do from this point on would be to multiply n by the "off-by-one" solution to 
finish our function because we know that to calculate a factorial, we simply multiply each number from `n` down to one together.

### The Base Case

If our factorial function was called at this point though, it would not be particularly useful as it would run indefinitely due to us not creating 
a base case. Defining a solid base case is imperative to writing recursive code. Without a base case, our function would call itself indefinitely leading
our program to eventually run out of memory and cause what is known as a stack overflow (No, not _that_ toxic hellscape).

## The Three Steps in action

```python
def factorial(num):
    # STEP_THREE: A solid base case
    if num == 1:
        return 1

    # STEP_ONE: Assume the function is already implemented
    # STEP_TWO: Find the solution to the penultimate iteration
    return num * factorial(num - 1)
```

## Maslow's Hammer

It is tempting once you have grasped recursion to want to use your new found tool everywhere but in my opinion, this is the wrong approach.
Yes, use recursion, but for problems it is well suited to. Forcing a soluiton rarely ends well. The idea is that as programmers, we learn many 
techniques but just as importantly, learn where each of these techniques work well.

In some circumstances, using recursion can make your code wildly inefficient, for example, when you have overlapping subproblems. This is where 
using Dynamic Programming techiques such as Memoisation to cut down the amount of recursion can be beneficial, but that is another post in itself.

## Wrapping up

There is a ton more to say about recursion and it will no doubt continue to baffle novice and experienced programmers alike for decades to come.
However, if you keep the three steps in mind, hopefully you too will have an easier time _writing_ recursive code which is in my opinion harder than
reading and understanding it.
