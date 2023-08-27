---
title: "Solving Project Euler Problems With Nothing But Vim"
date: 2023-08-27T11:32:04+01:00
draft: false
---

Another rainy British weekend, another wholly unnecessary project. This time, I thought it would be fun to find out whether I could solve
some simple problems starting from an empty Vim buffer and running some commands to get to the correct answer. It required a little thought and 
getting creative with substitute commands and registers but this process will show just just how powerful Vim's text editing features are and this only
scratches the surface of what is possible.

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
character in Vim repeats the last action (which was entering a zero followed by a newline). Preceding this with a number tells Vim how many 
times you want it to repeat the last action. We should now have a buffer which contains 999 lines, each containing a zero.

Next, we will want to make this list of zeros into an incrementing range of numbers. To do this, go right back to the start of the buffer with `gg`
and then type `shift+vG` to enter visual line mode and select all lines. Once selected, we can type `g<C-a>` which will magically turn our list
of zeros into that incrementing list we wanted. Nice!

## Filtering the multiples of 3 and 5

Ok, that out of the way we can now look to filter our range so that we only have the multiples of 3 and 5 that we wanted.
This is where the substitute command comes in...

```vim
:%s/\v\d+/\=submatch(0) % 3 == 0 || submatch(0) % 5 == 0 ? submatch(0) : ''
```

What the above command does is replaces any lines which are neither a multiple of 3 or 5 with an empty line. This make it possible for us to then
remove those blanks in the next step. The interesting bit of the above command is how you can evaluate expressions in sub commands with `\=`. This is 
the bit that lets us do mathematical operations on each match and apply a substitute accordingly.

For now, your buffer should start to look like the below.

```


3

5
6


9
...
```

## Removing the blanks

Removing the blanks is straightforward enough using the [global command](https://vim.fandom.com/wiki/Power_of_g) `:help global`.

```vim
:%g/^\s*$/d
```

Ok, I know that last one looks a bit weird and people generally hate regular expressions but we are just setting the scope of the command 
to all lines with `:%g` then matching on lines that are blank or have whitespace with the regex `/^\s*$/` and rather than passing a replacement
like we would with the substitute command, we instead give a command to run. In this case `d` means `delete` all matched lines. We are getting there!

```
3
5
6
9
```

## Building the equation

We are most of the way there now. We have a list of newline separated numbers below our limit of 1000 and all are multiples of 3 or 5.
Next up we need to find a way of summing those values to give us our end result. Again, if I wasn't solely limited to Vim, I might pipe out the 
whole buffer to AWK with something like `:%!awk '{sum += $1;} END {print sum}'` which would do the job easily enough but that would be cheating
however elegant a solution it may seem.

Instead we will have to get a little creative. This will involve a couple of quick transformations to the data through really simple sub commands.

We are going to create a mathematical expression from all the numbers in the buffer and one way I thought to do this, was prepend every line with a `+`.
As easy as a sub command could be `:%s/^/+`. Great! Our buffer should start to look like this.

```
+3
+5
+6
+9
```

Next, I want to remove all the new line characters so that we can evaluate the whole expression in one. Again, as simple as sub commands come.
`:%s/\n//`.

```
+3+5+6+9
```

Nearly there now that we have our full expression ready to be evaluated.

For the next and final step I'm to take advantage of vim's registers so first, I'll want to make sure I have one empty and ready to be filled.
I'll do this by typing `qaq`. This will clear the `a` register by starting a macro recording and then immediately ending it this flushing that
register.

To fill the `a` register, I'll type `"ayy" to yank the entire line into the register and then `o` to enter insert mode on a new line.

While still in insert mode, I can type `<C-r>` to give me access to my registers and then type `=`. You should see the equals symbol appear in 
the command prompt at the bottom of the Vim window. Then we just need to paste the contents of the `a` register into this command prompt to evaluate
the expression. We do this with `<C-r>a<CR>`.

TADA! Your solution appears before you. If you have done this correctly, you should see the number 233168.


## Wrapping up

This was a super fun brain teaser and shows just what is a capable from merely a text editor. Sometimes setting limitations like this forces us to get 
creative with solutions to real problems which I believe is a skill worth sharpening. No doubt I will come across problems in my day job where
there are limitations and I need to solve a problem. You can never be too prepared. 

Maybe [real programmers](https://xkcd.com/378/) do use a magnetic needle and a steady hand (or even butterflies) but I prefer Vim.
