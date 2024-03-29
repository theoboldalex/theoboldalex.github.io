---
title: "Solving Project Euler Problems With Nothing But Vim - Part 2"
date: 2023-09-19T22:37:46+01:00
draft: false
---

Ok, last time's Project Euler solution using nothing but Vim was so fun to do, I decided to up the ante this week and attempt
to solve the second problem in the Euler archive (Even Fibonacci Numbers). 
This one is much more tricky; so get your [Macros](https://vim.fandom.com/wiki/Macros) ready and let's dive in.

The problem states...


> **Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with and, the first terms will be:**

> **1,2,3,5,8,13,21,34,55,89...**

> **By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.**

## Getting started with the sequence

Much like last time, we need to start by generating a sequence of numbers. This time though, the sequence isn't simply incrementing intergers
but is a more complex sequence. Unfortunately there isn't a command built in to Vim that will help us here so we will have to do it ourselves.

To create the sequence we will record a macro, but first we need a single, simple equation to work from. If you are familiar with the fibonacci sequence, it is often exaplained as starting from zero and one summed, followed by the result of that summed with one and then on and on continually summing the previous two numbers in the sequence.

Let's start then by opening vim and entering insert mode on the first line of our fresh buffer. On this line, we will enter the text `1+1`. As simple an equation as we will ever see. We need this base in order to build up our sequence in the macro that we will write next.

For the purpose of clarity and brevity, this tutorial will just consider the first 10 items in the fibonacci sequence, but the same principle applies no matter how big we build our sequence.

The resulting content of the register `w` into which we will record our macro will be as follows but lets also step through this and take a look at each step in isolation. (To see the content of your registers at any stage run the command `:reg`)

```
V"wyo^R=^Rw^M+^[k0yiwj$p
```

### Step one
`V"wy`
The first step is to get our typed expression into a register of our choosing. I did this by visually selecting the first line of the buffer with `V` and then yanking the selection into the `w` register with `"wy`. I chose the `w` register purely because it is close to both `q` and `a` on the qwerty keyboard layout and I was using `q` to record the macro into register `a`.

### Step two
`o^R=^Rw^M+^[`
Step two is a little more involved and uses vim's expression registers to help us calculate the arithmatic operation captured inside our register. To achieve this, we enter insert mode on a new line with `o` and use `<C-r>` to access our registers. The `=` operator tells vim to treat our next command as an expression. We next need to access our registers again with another `<C-r>` and paste in the contents of our chosen register with `w`.

When we now hit enter, the result of our expression register should be rendered in our buffer. If this step has worked our buffer should look like this.

```
1+1
2
```
While still in insert mode we add a `+` symbol to the line in preparation for the next step and finally return to normal mode. The resulting buffer is.

```
1+1
2+
```

### Step three
`k0yiwj$p`
Ok, so at this stage we have managed to calculate the next value in the sequence, but how do we take this and make it into a repeatable action we can execute N times?

Well, we need to build the calculation for the next value in the sequence and knowing we can calculate this from `n[i] + n[i-1]` we can deduce that the first number on the previous line, is the previous value in the sequence. Knowing this we can;

- `k0` go to the start of the previous line
- `yiw` yank the contents of the first `<word>`
- `j$` return to the end of the second line in the buffer
- `p` and paste the yanked content

We have now built the repeatable calculation for generating N terms of the fibonacci sequence.

```
1+1
2+1
```

Make sure to end your recording of the macro by hitting `q` and then we can complete the generation of the first ten terms in the sequence with the command `8@a`.

```
1+1
2+1
3+2
5+3
8+5
13+8
21+13
34+21
55+34
89+55
```

Here you will see that the left hand side of each expression is the current term in the sequence and the right hand side is the previous term.

## Doing the math

### Signal vs Noise
`:%s/[^0-9]\d*//g`

Before we can do our filtering and summing we need to remove some of the now extraneous noise in our buffer. The above substitute command simply removes anything including the `+` symbol and following numbers fron each buffer line.

```
1
2
3
5
8
13
21
34
55
89
```

### Keeping the evens
`%s/\v\d+/\=submatch(0) % 2 == 0 ? submatch(0) : ''`

This command will be familiar from [my last vim solve]({{< ref "project_euler_in_vim" >}}). All this is doing is replacing lines which do not match an even number with a blank line.

```

2


8


34


```

### Stripping the blanks
`:%g/^\s*$/d`

Again, this global command should look familiar. We are just deleting any lines that are either blank or contain only whitespace.

```
2
8
34
```

### Finishing touches
`:%s/^/+/|%s/\n/`

A qick double substitution which adds a `+` symbol to the start of each line in the buffer and with the pipe `|` I can pass a second command which strips newlines from the file and we finally have our final expression ready to evaluate.

```
+2+8+34
```

### Calculating the expression

In a similar vein to how we generated the terms in the sequence, we are going to again reach for the expression register to help us complete our calculation and solve the problem once and for all.

`V"eyS^R=^Re^M^[`

This command visually selects the whole expression on the first line of our buffer and captures it into register `e`.
We then replace the contents of the first buffer line using `S`. The replacement is again just using `<C-r>` to access our registers and use `=` to evaluate the contents of them.

The result of this command should replace the buffer content with the number `44` and with that, we are done.

## Concluding

Ok, I know what you are thinking. We hand waved away the most difficult part of solving this one which is stopping the generation of the sequence terms when we hit the four million limit, but I haven't yet figured out a nice way to achieve this. Rest assured I will be back with another post once I have nailed a solution to that one.

My real reason for writing this post though was because it would act as the perfect segue for me to talk about the fibonacci sequence and its audacious misuse as an estimation tool for scrum teams; a practice that I can only describe as a flagrant and unapologetic affront to the very essence of software development.

Tune in next time to find out why that is a hill I may well end up dying on.

:wq

