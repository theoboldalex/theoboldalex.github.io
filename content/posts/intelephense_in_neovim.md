---
title: "NeoVim for PHP development in 2023"
date: 2022-12-19T14:33:58Z
draft: false
---

NeoVim is the most loved text editor for the second year running according to the [Stack Overflow survey](https://insights.stackoverflow.com/survey/2021#section-most-loved-dreaded-and-wanted-collaboration-tools)
and for good reason. The open source, Vim fork adds many quality of life improvements over Vim
but none do more to improve the developer exprerience than having the ability to configure and extend the editor using [Lua](https://www.lua.org/) rather than VimScript.

As a developer that has used a number of editors over the years including Sublime Text, VSCode, and most recently PHPStorm, I feel that I can confidently say that for 
me, nothing else out there right now comes close to NeoVim for what I want out of an editor. Sure, it doesn't have some of the bells and whistles that PHPStorm has out of 
the box; However, the Unix Philosophy applies here. As a text editor, it is unbeatable. As a database client, not so much. Responsiveness and a lightweight feel is paramount to
my enjoyment of the tools that I use and it is hard to ignore just how fast and snappy NeoVim feels to use in comparison to literally any GUI based editor. Yes, I am including you Sublime Text.

I have been using NeoVim as my daily driver for the dayjob for close to a year now after using it for most languages except PHP for a good while longer.
The key to making the switch away from the niceties of PHPStorm for me was getting an LSP configured to play nicely with PHP which, in most editors except for PHPStorm has always been a bit of a drag.

With that said, let's look at how I configure LSP with the premium version of [Intelephense](https://intelephense.com/) in NeoVim.

## Installing LSP-ZERO

There are many ways to configure LSP clients in NeoVim but one that has been garnering attention recently in the NeoVim subreddit and also through prominent community streamers/youtubers is by using LSP-ZERO.
Getting started with LSP-ZERO couldn't be easier and is simply a case of copy-pasting the below config from the docs which are freely [available on Github](https://github.com/VonHeikemen/lsp-zero.nvim).
I use [packer](https://github.com/wbthomason/packer.nvim) so my config looks like this.
```Lua
-- LSP-ZERO
use {
    "VonHeikemen/lsp-zero.nvim",
    requires = {
        -- LSP Support
        {"neovim/nvim-lspconfig"},
        {"williamboman/mason.nvim"},
        {"williamboman/mason-lspconfig.nvim"},

        -- Autocompletion
        {"hrsh7th/nvim-cmp"},
        {"hrsh7th/cmp-buffer"},
        {"hrsh7th/cmp-path"},
        {"saadparwaiz1/cmp_luasnip"},
        {"hrsh7th/cmp-nvim-lsp"},
        {"hrsh7th/cmp-nvim-lua"},

        -- Snippets
        {"L3MON4D3/LuaSnip"},
        {"rafamadriz/friendly-snippets"},
    }
}

```

## Configuring LSP-ZERO

[LSP-ZERO](https://github.com/VonHeikemen/lsp-zero.nvim) is a fantastic plugin that Leverages [Mason.nvim](https://github.com/williamboman/mason.nvim) for managing LSPs, code quality tools like linters and formatters as well as debugging tools.
Below, you can see a stripped down verison of my lsp configuration file that lives in a directory called `after/plugin/lsp.lua`. Files in this directory are auto loaded by NeoVim onn start
so any config in here will be available to us once inside NeoVim.

Much of this is boilerplate for setting up LSP-ZERO but the bits we are interested in are primarily the `on_attach` function,and also the call to `lsp.configure()` for intelephense.
```Lua
local lsp = require("lsp-zero")
lsp.preset("recommended")

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
end

lsp.ensure_installed({
  "intelephense",
})

lsp.configure("intelephense", {
    on_attach = on_attach,
})

lsp.setup()
```

## Accessing Intelephense premium features

Intelephense is a freemium product and while I held off on purchasing a license for the longest time, in order to use NeoVim with largew PHP codebases, I believe
that it is a necessary evil to hand over the admittedly small amount of cash for a license. Once you have received your license key via email, save into into a text file at 
`$HOME/intelephense/license.txt`

The way we are going to bring this license key into NeoVim is by reading the file in on opening a buffer containing a file with a `.php` extension. This method is much more secure than reading 
an environment variable or hard-coding the license into our config file as we avoid the risk of accidentally committing our license key to a public repo if we do it this way.

In order to read our license key, we will need to write a little Lua helper function. This is easy enough to do and if you have placed you license file in the location that I suggested, you could just copy-paste
the below function into your own config to grab the key.

```Lua
local get_intelephense_license = function ()
    local f = assert(io.open(os.getenv("HOME") .. "/intelephense/license.txt", "rb"))
    local content = f:read("*a")
    f:close()
    return string.gsub(content, "%s+", "")
end
```

**Note the spelling of `licenceKey` here.**
```Lua
lsp.configure("intelephense", {
    on_attach = on_attach,
    init_options = {
        licenceKey = get_intelephense_license()
    }
})
```
Once we have this in our config, we can quit and restart NeoVim. When we next open a PHP file, we should be prompted that our Intelephense key has been activated and we can now access all of the
premium features such as renaming symbols and jump to implementation.

NeoVim is a really great editor and I have only just scratched the surface in this article with regards to getting an LSP setup for working with PHP but there is a whole world of plugins out there for everything
from [Git integration](https://github.com/tpope/vim-fugitive) and [fuzzy finding](https://github.com/nvim-telescope/telescope.nvim) to [games](https://github.com/ThePrimeagen/vim-be-good) 
and [themes](https://github.com/Mofiqul/vscode.nvim). And for instances where there isn't yet a plugin available, well, build your own. It is super easy to get started but that is a story for another day.
