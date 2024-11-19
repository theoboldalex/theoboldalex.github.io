---
title: "On Getting FP Pilled"
date: 2024-11-19T22:22:25Z
draft: true
---

I make no secret of the fact that I am an enjoyer (and advocate for) functional programming techniques but as yet, I have not put down into words, what functional programming is to me, why I 
evangelise it, how I found FP and why it has had such an impact on the way I write software.

## The Beginnings
After a few failed attempts at learning to program with Python in the early 2010s and writing some basic SQL for work, my first real forays into programming came through 
sites like [project euler](https://projecteuler.net/). I found the problem solving aspect of these challenges addictive but more than that, I wanted to find clever and creative ways to solve the problems, not 
worrying too much about the performance or readability of the code I produced. Not exactly production ready corporate code but damn fun. I learned some JavaScript and went deep on Kyle Simpson's [You don't know JS](https://github.com/getify/You-Dont-Know-JS)
series of books to help me find creative ways to leverage the language. A typical example might look something like the below for solving the classic FizzBuzz game.

```JavaScript
[...Array(100).keys()]
    .map(i => i + 1)
    .map(i => i % 15 === 0 ? "FizzBuzz" : i % 3 === 0 ? "Fizz" : i % 5 === 0 ? "Buzz" : i)
```

What I didn't appreciate at the time was that I was not only learning to program, but also building the functional mindset through using higher order functions, avoiding mutable state and through method
chaining, I was essentially learning about pipes.

This approach to programming of treating a program as a series of data transformations rather than state mutations has always seemed natural to me having learned to program in this way (OOP took much longer to get to grips with when I moved onto Ruby and later PHP).

## Finding Clojure

A couple of years ago I stumbled across a fantastic conference talk from Rich Hickey and found the Lisp like language he is the creator of Clojure. I even wrote the first ever post on this blog about 
Clojure and how learning it had brought the fun back to programming that seemed to be missing from my day job at the time. Clojure was the first truly functional language I ever learned and to this day
I still find its expressiveness second to none. Lisps just work the way that I expect programming languages to work and find that I enjoy programming more without all of the ceremony involved in many OOP
languages. There are a couple of issues with Clojure though, namely that I prefer a somewhat batteries included framework when I am trying to build software so Clojure with its convention of sticking to a 
small core and importing libraries was not as productive as I would like. Perhaps I had been spoiled by years of working with Rails and Laravel in this respect. Unfortunately, there does not seem to be much
appetite for a more fully fledged framework in the Clojure community so this was a little off putting to me (I still love Clojure for solving pure programming problems such as Advent of Code though).

## The Unix Shell

In 2023, I decided to attempt Advent of Code using only shell scripts with a heavy focus on Awk. I had learned Awk earlier in the year and had enjoyed using it to solve some real problems at work. The shell
with its small but sharp, composable tools and pipes sounded a lot like the way I had been programming all along i.e. making a transformation on some input, passing it along a pipeline, doing another transformation and on and on until I have the final result.

I only got a few days into Advent of Code but learned some really valuable techniques (not to mention wrote some gnarly regular expressions) and furthered my belief that functional programming is both simpler
than some other paradigms, but also fits better the work that many of us do as software professionals.

## OCaml, Lisps, MIT

This year, I have gone deeper down the rabbit hole, proclaiming 2024 as the year of the Emacs desktop, getting a little into Elisp, and Scheme through reading MIT press' [The Little Schemer](https://vpb.smallyu.net/[Type]%20books/The%20Little%20Schemer.pdf).
I thought I understood recursion before reading this book and conceptually, I did. Having read the book now, I feel confident actually using recursion to solve problems. A feat only few of my colleagues can also attest to.

I also spent some time with both OCaml and Haskell, two very interesting languages that I will no doubt dig deeper into in future but it was a chance encounter with a conference talk from Joe Armstrong, one 
of the creators of Erlang at Ericsson in the 80s that has led to my current infactuation with Elixir.

## Elixir, Phoenix and the Pipe operator

<!-- blend of functional programming with being an industrial language with pragmatic framework similar to Laravel/Rails that gives perfect blend of --> 
<!-- productive web stack with FP features (as well as scaling incredibly well due to the way the BEAM was designed) -->

<!-- Also great community/discord, docs (after getting used to them) -->
I had heard about Elixir for quite a while but had never really looked into it given I had a full time job and young family as well as multiple hobbies outside of programming. I also just really wanted to 
use Clojure for everything outside of my day job such was my love for Lisps.

I had started preparing a talk to give at work on functional programming and one of my slides was titled "FP why should you care?". I wanted to show people that FP was not simply some academic thing that 
required a new way of thinking for no great benefit so decided to use this slide to do a bit of a case study on Erlang's use in industry.
