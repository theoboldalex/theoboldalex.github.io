---
title: "Minimalism_in_software_development"
date: 2023-01-09T18:46:53Z
draft: false
---

I recently read and contributed to [this reddit thread](https://www.reddit.com/r/minimalism/comments/zzlce3/minimalism_as_a_guiding_principle_in_software/) and it got me to thinking.
As a person that would begrudgingly identify as a 'Minimalist' whatever that term actually means nowadays, I think that the desire to strip things back to only the essential in my life, aligns
really well with software development and the practices, habits and principles I bring to my work.

The more I think about it, the more I see minimalist values everywhere even if they are not direct. Think YAGNI, DRY, the Unix philosophy of simple tools that do one thing with no cruft, XP, TDD and more. Also,
I try to keep my workspace clean, tidy and organised, both in the physical sense but also in the tools I use. Unlike many developers that have hundreds of browser tabs open at any one time and multiple GUIs or terminal sessions
open and fighting for monitor real estate, I take an approach that involves only a single monitor and I try to keep any running applications to a minimum. Those that do make the cut are put into full screen view and I use only one 
at a time where possible. 

Thinking about this in the way I use vim, I very rarely use features such as [tabs](https://vim.fandom.com/wiki/Using_tab_pages) and [splits](https://thoughtbot.com/blog/vim-splits-move-faster-and-more-naturally), opting to instead use a single file as my anchor point and if I need to navigate around, I can do so using a 
[fuzzy finder](https://github.com/nvim-telescope/telescope.nvim) or jumps to definitions via LSP and then use `<C-^` to jump back and forth between the current buffer and my anchor point. Having this anchor point, for me lessens the cognitive load of trying to remember where
I am within a codebase and keeps things really simple.

I did try to simplify things even further by getting my entire workflow just into PHPStorm; Text editing, HTTP requests, Database Client and all, but this was a step too far in stripping things back even for me (really, I just couldn't let
go of NeoVim in the terminal but PHPStorm is fantastic and still gets used for what it excels at from time to time).

So to sum up, I think trying to sculpt both my work and my workflow down to the bare essentials to still add maximum value is the key to maintianing a healthy balance between not enough and too much. the key is in knowing when to stop
optimising for simplicity, and start shipping real work.
