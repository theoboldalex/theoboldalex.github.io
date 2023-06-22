---
title: "Exercises in the Pointless"
date: 2023-06-22T13:51:57+01:00
draft: true
---

## Reflecting on side projects

I have been a programmer now for nearly a decade. In that time, I have completed countless side projects (and started many more than that)
To this day, I am yet to create anything particulalry useful or interesting. Part of me has felt a bit disappointed about this at times and 
sometimes it feels like I'm "falling behind". But what is the point of a side project? Well, for me it is about learning and exploration.
Not every project must be an open source success with a solid user base and nor should it. The most fun and insightful side projects I have
worked on have had very little practical value and they are often the projects that have the worst coding standards, most buggy code and are
thrown together quickly sometimes in matter of hours.

Take a recent project of mine that I did in a Friday afternoon. The premise is simple. I don't like the PHP documentation site. Being a
"terminal guy" I am much happier using man pages and 'less'ing my way through docs so I thought, why not compose a bunch of my favorite
command line utilities to bring the PHP docs to my terminal?

The great things about projects like this is the speed at which you are able to iterate and hack away on something. Scripting languages 
are unbeatable for tasks like this so Bash was an easy choice (although I do enjoy scripting in Lua too)

This project simply started with a single curl command and then I iterated from there.

```bash
curl https://www.php.net/manual/en
```

## The user journey

Before diving into the code, lets have a look at how I envisaged this working. Firstly, I wanted ot be able to call a simple script from anywhere
in my terminal. This is easy enough. Create a script either in a directory on your path, or in a new location and add that to your path.
I decided to place mine in `$HOME/.config/bin` as this is both on my `$PATH` and also in version control along with my dotfiles. Next up, I 
created an alias for running the script to save myself a few keystrokes in typing `.sh` everytime I wanted to call my script into action.

So now we have a simple bash script that we can run anywhere just by typing `phpdoc` and hitting return. At present, this just fires off
that curl command we saw earlier, but what I _wanted_ it to do was the following...

1. Give me an interactive, filterable list of docs pages that I can fuzzy search through unitl I find the option I want. This is a task 
perfectly suited to [fzf]("https://github.com/junegunn/fzf"). I decided it would be a good idea to separate the docs into sections for each
part of the docs. Tp begin with I just created sections for function docs and class docs.

![select between function or class docs](/phpdoc-first-screen.png)

2. Selecting an option from this screen should move us onto another `fzf` selection with the results for that section. Again we can fuzzy find
our way through the results until we reach our desired function or class name.

![select a function name from the results](/phpdoc-function-search.png)

3. Selecting an option from the list should bring up a formatted version of the documentation in `less` allowing us to scroll and search through
the resulting documentation. This is much more like the man page interface I am used to and like.

![the formatted docs in less](/phpdoc-function-doc-result.png)

And that is it!

## So, how did I approach it?

Well, as I mentioned, I started with a simple script that just curled the root of the PHP docs site. The way I iterate on scripts like this is 
simply running them from within vim.
