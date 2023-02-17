---
title: "Create a CLI for your Composer package"
date: 2023-02-15T23:37:57Z
draft: false
---

I have been trying out a newly released PHP library [Streetlamp](https://github.com/willitscale/streetlamp) the last couple weeks
and it is really great. However, one feature it is missing is a way of easily discovering API endpoints for your application.
The package creator is aware of this and there is an issue in the project todo that will look to rectify this but I thought I 
would have a tinker to see what I could come up with. Maybe I'll submit it as a PR if my solution is any good but that is yet to be seen.

My idea was to give the package a lightweight CLI so upon running something like `./vendor/bin/streetlamp routes` we could get an output 
of all of the application's routes that are registered on controllers via PHP attributes. Having never implemented a Composer package of
my own, I had some learning to do to get this up and running. In this post, I am going to share the very basics of getting something like this
implemented.

## Bootsrapping a package skeleton

There are a ton of package skeleton template repos out there to choose from if you are building packages; However, for this demo
we will just create a directory somewhere on our host machine and navigate to it before running `composer init` 
(assumes you have PHP and Composer installed) and following the prompts. Once this is done, we should have a `composer.json` and 
`composer.lock` file in our directory.

Your `composer.json` will look a little something like;

```json
{
    "name": "alextheobold/composer_packages_blog_post",
    "description": "A demo repo for my post on creating CLIs for Composer packages",
    "license": "MIT",
    "authors": [
        {
            "name": "theoboldalex",
            "email": "theoboldalex@gmail.com"
        }
    ],
    "require": {},
    "autoload": {
        "psr-4": {
            "theoboldalex\\ComposerPackagesBlogPost": "src"
        }
    }
}
```

## Creating the executable binary

In order for Composer to know you want to run part of your package as an executable binary, we are required to add a property to our
`composer.json` config. This is simple enough and if you want to go deeper into this you can 
[Read The Friendly Manual](https://getcomposer.org/doc/articles/vendor-binaries.md).

So let's add that! Our config should now look like this;

```json
{
    "name": "alextheobold/composer_packages_blog_post",
    "description": "A demo repo for my post on creating CLIs for Composer packages",
    "license": "MIT",
    "authors": [
        {
            "name": "theoboldalex",
            "email": "theoboldalex@gmail.com"
        }
    ],
    "require": {},
    "autoload": {
        "psr-4": {
            "theoboldalex\\ComposerPackagesBlogPost": "src"
        }
    },
    "bin": ["bin/my-demo-cli"]
}
```

Notice the new line we added

```json
{
    "bin": ["bin/my-demo-cli"]
}
```

This tells composer that when our package is installed, we want to symlink the file at `bin/mydemo-cli` to the `/vendor/bin` directory and 
make it executable. Also worth noting is that the `bin` key holds an array so we can simply list any further scripts we want Composer to
link to `/vendor/bin`.
