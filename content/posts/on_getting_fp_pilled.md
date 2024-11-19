---
title: "On Getting FP Pilled"
date: 2024-11-19T22:22:25Z
draft: true
---

I make no secret of the fact that I am an enjoyer (and advocate for) functional programming techniques but as yet, I have not put down into words, what functional programming is to me, why I 
evangelise it, how I found FP and why it has had such an impact on the way I write software.

## The Beginnings

<!-- code wars, leetcode etc -->
After a few failed attempts at learning to program with Python in the early 2010s and writing some basic SQL for work, my first real forays into programming came through 
sites like [project euler](). I found the problem solving aspect of these challenges addictive but more than that, I wanted to find clever and creative ways to solve the problems, not 
worrying too much about the performance or readability of the code I produced. Not exactly production ready corporate code but damn fun. I learned some JavaScript and went deep on Kyle Simpson's [You don't know JS]()
series of books to help me find creative ways to leverage the language. A typical example might look something like the below for solving the classic FizzBuzz game.

```JavaScript
[...Array(100).keys()]
    .map(i => i + 1)
    .map(i => i % 15 === 0 ? "FizzBuzz" : i % 3 === 0 ? "Fizz" : i % 5 === 0 ? "Buzz" : i)
```

What I didn't appreciate at the time was that I was not only learning to program, but also building the functional mindset through using higher order functions, avoiding mutable state and through method
chaining, I was essentially learning about pipes.

This approach to programming has always seemed more natural to me (OOP took much longer to get to grips with when I moved onto Ruby and later PHP).

## Finding Clojure

link to original post

## The Unix Shell

advent of code 2023 in shell/awk

## OCaml, Lisps, MIT

twitch, OCaml hype, The Little Schemer, SICP, Emacs rabbit hole

## Elixir, Phoenix and the Pipe operator

blend of functional programming with being an industrial language with pragmatic framework similar to Laravel/Rails that gives perfect blend of 
productive web stack with FP features (as well as scaling incredibly well due to the way the BEAM was designed)

Also great community/discord, docs (after getting used to them)
