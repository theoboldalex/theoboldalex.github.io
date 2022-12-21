---
title: "No,you don't need multi cursor editing in Vim"
date: 2022-12-21T19:23:16Z
draft: false
---

**Disclaimer: This post assumes at least a passing familiarity with regualr expressions.**

A question I see come up relatively often in the various vim communities online is a request for plugin recommendations that provide support for multi cursor editing in Vim
and Vim-like editors.

In this post, I'm going to show you why you (probably) don't need multi cursor editing in Vim and how to get the similar behavior to multi cursors through native features that have been
around in Vim for a long time (maybe even since its inception in some cases).

## Substitue command
### A starter for 10
Vim's subsitute command is incredibly powerful. If this is your first exposure to it, `:h :substitute` is a great place to start. This first example is probably the most simple
yet useful command I could think up and shows how the substitute command can be used as a search and replace over a bufer. In this example, we are going to swap all double 
quotes for single quotes in a javascript object. (I know most editors can do this with search and replace all. This is just a primer before we get into the good stuff).

Take the below code for an example

```javascript
// simple line level substitute command
// :s/"/'/g
const name = "Alex"
```

Let's break down this simple example and see what is going on when we run this command.

Firstly, we enter command mode and pass substitute to it `:s`. The substitute command takes a couple of regular expressions. The first is the pattern to search for, the second is
the replacement. SO in this example, we swap double quotes for single quotes `/"/'/`. Finally, we add the `g` or `global` flag. This tells the substitute command to replace all instances
of double quotes on the line with single quotes rather than just the first match.

We can also run the subsitute command across the entire buffer rather than just the currently selected line by preceding the command with `%` as in the next example.
`:%s/"/'/g`.

```javascript
// simple buffer level substitute command

// BEFORE
// :%s/"/'/g
const people = [
    {
        name: "Alex",
        age: 35
    },
    {
        name: "Fred",
        age: 4
    }
]

// AFTER
const people = [
    {
        name: 'Alex',
        age: 35
    },
    {
        name: 'Fred',
        age: 4
    }
]
```

### replacements over visual selection
### Word under cursor match
### A new argument
### A more complex example
## Macros
### From arrow functions to regular functions
