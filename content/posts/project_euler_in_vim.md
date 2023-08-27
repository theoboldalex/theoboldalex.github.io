---
title: "Solving Project Euler Problems With Nothing But Vim"
date: 2023-08-27T11:32:04+01:00
draft: false
---

Another rainy British weekend, another wholly unnecessary project. This time, I thought it would be fun to find out whether I could solve
some simple problems starting from an empty Vim buffer and running some commands to get to the correct answer. It required a little thought and 
getting creative with substitute commands and registers but this process will show just just how powerful Vim's text editing features are and this only
scrathes the surface of what is possible.

## The Problem

The problem is one that many are familiar with and is the first exercise in Project Euler. I remember trying to solve this with Ruby back when I
was first getting into programming and it took considerable effort for me to get to the correct answer back then. It is nice for the ego coming
back to simple problems like this after a number of years to remind yourself how far you have come.

The problem asks us to `Find the sum of all the multiples of 3 and 5 below 1000`. Should be easy enough, right?

## Building a range on numbers

First things first, I opened an empty buffer to work in. There are many ways to build a range of newline separated incrementing integers.
If I wasn't trying to stay fully inside Vim, I might have called out to seq from normal mode by double tapping bang to filter the current buffer 
line and calling seq. `:.!seq 1 999` Instead, I will enter insert mode and use some of the simple repeat and increment commands to achieve a similar result.

If you enter insert mode, type a `0`, hit enter then return to normal mode, you can fill 999 lines with a zero by then typing `998.`. The period 
character in Vim repeats the last action (which was entering a zero followed by a newline). Preceeding this with a number tells Vim how many 
times you want it to repeat the last action. We should now have a buffer which contains 999 lines, each containing a zero.

Next, we will want to make this list of zeros into an incrementing range of numbers. To do this, go right back to the start of the buffer with `gg`
and then type `shift+vG` to enter visual line mode and select all lines. Once selected, we can type `g<C-a>` which will magically turn our list
of zeros into that incrmenting list we wanted. Nice!

## Filtering the multiples of 3 and 5


