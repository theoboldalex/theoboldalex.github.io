---
title: "Two Guiding Principles of Software Design"
date: 2025-10-15T22:27:34+01:00
draft: true
---



## Simplicity

Simplicity. This is an oft overused term in software but is seldom understood in the way that Rich Hickey so eloquently explains in 
[Simple Made Easy](https://www.youtube.com/watch?v=LKtk3HCgTa8). Not to complect matters, but my understanding of what most people mean 
when talking about simplicity in software is "what is the easiest thing we can do that meets the brief?". While they sound almost identical 
(and most people would understand them as such) the question should really be "what is the simplest solution that meets the brief?". The former suggests
that to be simple, we should aim for the quickest solution to implement. Now, this may be the simplest solution however, it also may not be. It could be 
that the simplest solution requires significant refactoring of existing code to even be possible. It may be that the constraints of budget or time
mean that the simplest solution is not feasible and that the second or third simplest solution becomes the best option. We have to make trade offs such as this 
all the time as engineers.

The biggest benefit of designing a simple system though is that it enables us to change the system as we learn more about the domain and our requirements 
change over time. The ability to change the system, or _plasticity_ is my second guiding principle of software design.

## Plasiticity

If a software system is simply written and then left to work in an unaltered state forever or until it is deprecated, then plasticity is not important.
However, I have never come across such a system. For this reason, plasticity is my second guiding principle of software design. Every system I have ever
worked on has shifted its requirements over time, often before the system has even finished being built.

A system that is easy to change is a system that is enjoyable to work on. I have worked on many systems that were not malleable and they have never sparked 
joy in me. A system where change is hard means we cannot move as quickly or nimbly as we might in a system where change is easy. My experience tells me that
rigid, tightly coupled (adhesive not cohesive) systems also often lack automated tests (which has been a result of writing code that is not easy to test).

:wq
