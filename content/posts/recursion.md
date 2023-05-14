---
title: "How I (finally) Grokked Recursion"
date: 2023-05-14T18:53:14+01:00
draft: true
---

Recursion is a concept that can be either grasped or elude you. Conceptually, recursion is as simple as a function calling itself. 
However, understanding the intricacies of how, when, and why to use recursion can be challenging. Two influential factors that 
aided my understanding were [this book](https://media.pragprog.com/newsletters/2020-08-13.html) and learning Clojure.

## A Starter for Ten

Suppose we want to write a program for a rocket launch which counts down from ten to zero before taking off. Most of us (myself included)
would write a loop starting at ten and decrements a counter in each iteration only stopping when we reach zero but there is also another
way to do this. Enter recursion. Instead of using a loop, we can have our function call itself with ever decreasing arguments unitl we hit
a base case. The base case is the condition under which we want our function to stop calling itself and return.

```python
def blast_off(num):
    print(num)
    if num == 0:
        print('BLAST OFF!')
        return

    return blast_off(num - 1)
```

1. Some basic examples
2. Clojure and tail recursion
3. The three steps to make it easier
