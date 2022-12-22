---
title: "No,you don't need multi cursor editing in Vim"
date: 2022-12-21T19:23:16Z
draft: false
---

**Disclaimer: This post assumes at least a passing familiarity with regular expressions.**

A question I see come up relatively often in the various vim communities online is a request for plugin recommendations that provide support for multi cursor editing in Vim
and Vim-like editors.

In this post, I'm going to show you why you (probably) don't need multi cursor editing in Vim and how to get the similar behavior to multi cursors through native features that have been
around in Vim for a long time (maybe even since its inception in some cases).

## Substitute command
### A starter for 10
Vim's substitute command is incredibly powerful. If this is your first exposure to it, `:h :substitute` is a great place to start. This first example is probably the most simple
yet useful command I could think up and shows how the substitute command can be used as a search and replace over a buffer. In this example, we are going to swap all double 
quotes for single quotes in a JavaScript object. (I know most editors can do this with search and replace all. This is just a primer before we get into the good stuff).

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

We can also run the substitute command across the entire buffer rather than just the currently selected line by preceding the command with `%` as in the next example.
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

### Using lookarounds for fine-tuning matches
Lookarounds are a great feature of Vim regular expressions that I make heavy use of in my day to day work when refactoring code and they can be a really powerful 
tool once you have grokked them. The Vim wiki has a great explanation of lookarounds so I will [point you there](https://vim.fandom.com/wiki/Regex_lookahead_and_lookbehind)
rather than butchering an attempt to explain it here; However, I will show an example of a positive lookahead on some use cases I use all the time.

The first example is one that I use almost daily at this point to offer business insight to stakeholders that often need small data-points quickly and might pass me for instance a bunch
of user ids and ask for a certain data point relating to those ids. These ids often come to me in the form of an excel spreadsheet and require some formatting so we need some way to get those from the spreadsheet
into an SQL query in order to use them. While I could do this in Excel before bringing them into Vim, I find the substitute command absolutely perfect for small tasks like this and you will see 
why in this example.

```SQL
-- BEFORE
-- vi[:s/\d\zs$/,
SELECT some_data_point
FROM users
WHERE id IN (
    12345
    54321
    98765
    56789
    328
    9
    673456
)

-- AFTER
SELECT some_data_point
FROM users
WHERE id IN (
    12345,
    54321,
    98765,
    56789,
    328,
    9,
    673456,
)
```

This command shows a positive lookahead but also highlights a couple more interesting features of the substitute command; such as allowing the command to be run only against a 
visually selected region of code `vi[:s`. It also shows how we can do away with the final slash of the regex if it is not required for the operation we want to carry out.

Another example that regularly finds use in my arsenal is when working with JavaScript. Context switching between multiple programming languages throughout a work day can lead to small syntactical
mistakes creeping into code and with a language like JavaScript this can have unwanted consequences. Take the following code as an example.

```javascript
// BEFORE
// V2j:s/^\ze[a-z]/const <CR>
greeting = 'Hello'
// don't add a const to me
personName = 'Alex'
age = 35

// AFTER
const greeting = 'Hello'
// don't add a const to me
const personName = 'Alex'
age = 35
```
 In the before example, all three declared variables could be leaking into the global scope which could have unintended consequences. If we wanted to make the first two of these variables
 constants, but leave the third alone along with any commented lines, we could run the command to prepend `const` to the required lines. All this command does is looks at the line start,
 checks whether the line begins with an alphabetical character for lines within the visually selected region and if it does, it prepends the `const` keyword to it.

 ```
 /line starts with|lookbehind|letter between a and z/replacement
 /^               |\ze       |[a-z]                 /const 
 ```

### Word under cursor match
Another cool feature of the substitute command is that the search pattern uses the last search if none is provided. By this I mean that we can call substitute like so `:%s//helloworld/g`
and it will replace whatever was last searched for with the replacement string. This is fantastic when paired with the `*` key. For those that don't know, the `*` key in Vim
uses the word under the cursor to perform a forward search in the buffer (`#` does backward search but I find `*` fine for my purposes as it is one less mapping to remember).

Lets look at a short example. The following lines from the Rifleman's Creed can be almost instantly transformed into the NeoVimmer's creed by placing the cursor on the word `rifle` and hitting the `*` key.
Now run the command `:%s//NeoVim/g and begin to recite your new mantra.

```
** BEFORE **

This is my rifle. There are many like it, but this one is mine.
My rifle is my best friend. It is my life. I must master it as I must master my life.
Without me, my rifle is useless. Without my rifle, I am useless. 

** AFTER **
This is my NeoVim. There are many like it, but this one is mine.
My NeoVim is my best friend. It is my life. I must master it as I must master my life.
Without me, my NeoVim is useless. Without my NeoVim, I am useless. 
```

### Match groups
urls for curl
### A more complex example
json to PHP array

### A new argument
Another task that crops up regularly and is a great fit for using the substitute command for a solution is replacing extracted variables in function calls.
Take the below example from my NeoVim config for setting keymaps upon an LSP client attahcing to a buffer. As you can see, many of the `vim.keymap.set` calls take a table 
as their final input. Initially this was written with table directly coded into the calls but as the list of mapings grew, it made sense to refactor this out into a variable
that could be reused across all calls. Again the first tool I reached for was the sub substitute command.

First, I extracted the table into a local variable called `opts` before I got to work on replacing all of the hardocded tbales with the new opts variable.
**Note: remember to visually select the lines we want the replacement to work on for this one.**
```lua
-- BEFORE
-- V8j:s/{.*})/opts)/g
local on_attach = function ()
    vim.diagnostic.config({
        virtual_text = true,
    })

    vim.keymap.set("n", "K", vim.lsp.buf.hover, {buffer = 0})
    vim.keymap.set("n", "gd", vim.lsp.buf.definition, {buffer = 0})
    vim.keymap.set("n", "gr", vim.lsp.buf.references, {buffer = 0})
    vim.keymap.set("n", "gi", vim.lsp.buf.implementation, {buffer = 0})
    vim.keymap.set("n", "<leader>dk", vim.diagnostic.goto_prev, {buffer = 0})
    vim.keymap.set("n", "<leader>df", "<cmd>Telescope diagnostics<cr>", {buffer = 0})
    vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, {buffer = 0})
    vim.keymap.set("n", "<C-h>", vim.lsp.buf.signature_help, {buffer = 0})
    vim.keymap.set("n", "<leader>do", "<cmd>lua vim.diagnostic.open_float()<CR>")
    vim.keymap.set("n", "<leader>dp", "<cmd>lua vim.diagnostic.goto_prev()<CR>")
    vim.keymap.set("n", "<leader>dn", "<cmd>lua vim.diagnostic.goto_next()<CR>")
end

-- AFTER
local on_attach = function ()
    local opts = {buffer = 0}
    vim.diagnostic.config({
        virtual_text = true,
    })

    vim.keymap.set("n", "K", vim.lsp.buf.hover, opts)
    vim.keymap.set("n", "gd", vim.lsp.buf.definition, opts)
    vim.keymap.set("n", "gr", vim.lsp.buf.references, opts)
    vim.keymap.set("n", "gi", vim.lsp.buf.implementation, opts)
    vim.keymap.set("n", "<leader>dj", vim.diagnostic.goto_next, opts)
    vim.keymap.set("n", "<leader>dk", vim.diagnostic.goto_prev, opts)
    vim.keymap.set("n", "<leader>df", "<cmd>Telescope diagnostics<cr>", opts)
    vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, opts)
    vim.keymap.set("n", "<C-h>", vim.lsp.buf.signature_help, opts)
    vim.keymap.set("n", "<leader>do", "<cmd>lua vim.diagnostic.open_float()<CR>")
    vim.keymap.set("n", "<leader>dp", "<cmd>lua vim.diagnostic.goto_prev()<CR>")
    vim.keymap.set("n", "<leader>dn", "<cmd>lua vim.diagnostic.goto_next()<CR>")
end
```

This is great but it could have also been achieved in another way too using Macros. We will get on those now.
## Macros
### From arrow functions to regular functions and back again

## Wrapping up
Hopefully I have convinced you in this post that you don't actually need multi cursor support in Vim-like editors and that you have all the power needed for even complex search and 
replace functionality with the added bonus of macros and being able to map your most commonly used substitutions to a keyboard shortcut no matter how complex they are. This is something that I
don't think can be said for most text editors and is another reason I choose NeoVim as my editor of choice.
