---
title: "How I (finally) Grokked Recursion"
date: 2023-05-14T18:53:14+01:00
draft: true
---

Recursion is one of those concepts that you either grasp or you don't. Conceptually, recursion is as simple as a function calling itself. 
However, understanding the intricacies of how, when, and why to use recursion can be challenging. Two influential factors that 
aided my understanding were [this book](https://media.pragprog.com/newsletters/2020-08-13.html) and learning Clojure.

## A Starter for Ten

Suppose we want to write a program for a rocket launch which counts down from ten to zero before taking off. Most of us (myself included)
would write a loop starting at ten and decrements a counter in each iteration only stopping when we reach zero but there is also another
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

### Off by One

### The Base Case

Defining a solid base case is imperative to writing recursive code. Without a base case, our function would call itself indefinitely leading
our program to eventually run out of memory and cause what is known as a stack overflow (No, not _that_ toxic hellscape).

## The Three Steps in action

```python
def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)
```

## Maslow's Hammer

It is tempting once you have grasped recursion to want to use your new found tool everywhere but in my opinion, this is the wrong approach.
Yes, use recursion, but for problems it is well suited to. Forcing a soluiton rarely ends well. The idea is that as programmers, we learn many 
techniques but just as importantly, learn where each of these techniques work well.
