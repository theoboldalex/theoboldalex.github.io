---
title: "On Interactive Debugging"
date: 2024-02-08T21:44:46Z
draft: true
---

## A debate as old as time
Like spaces vs tabs and Emacs vs Vim, the debate between zealots on either side of the debate around debuggers has dragged on for so long 
that most people are probably bored of it now but us developers love to argue about unimportant things (see: Bike Shedding).

![the world if developers stopped arguing over their tools.](/the_world_if.jpeg)

So why drag this subject back up if we are all so bored of it? 

Well it turns out the "to debug or not to debug" debate comes up so often in work that I think there is some value in sharing my stance on the 
subject (if for the sole reason that I can just point people here next time I get dragged into this debate).

## In defence of Debuggers

As someone that primarily works with PHP, the debugger I am most familiar with is XDebug. Xdebug is a fantastic tool that can do so much more than just 
step debugging. It can used to profile an application as well as generating coverage reports and I hsve used it in the past for all of these tasks.

XDebug _can_ be a little tricky to setup for newcomers but overall it is still a relatively straightforward process (maybe less so than some other languages
where the debugger is a first class citizen or built into IDEs).

What debuggers give you is an incredibly detailed look inside a running application. This can be a boon when attempting find and fix tricky bugs.

The common argument from those that do not use debuggers is that they are slower than simply adding print statements to the code and running the application.
I don't agree with this premise. I don't think either is approach is inherently 'faster' and it is more about the use case.

## Print Debugging


