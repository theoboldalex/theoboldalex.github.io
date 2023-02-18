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

## Implementnig the CLI script

With the setup and config out of the way, we can get on with creating the CLI. 

**Note: I use the term CLI very loosely here. For this demo, we are only going to create a basic script; However, you can go as deep as you
like into this and have the script take arguments and flags**

We need to create a file in the location we declared in the `composer.json` bin array so let's do that.

```bash
md bin
vim bin/my-demo-cli
```

Inside the file, let's make a toy script which will simply show us the current time in a few major cities across the globe.

```php
#!/usr/bin/env php

<?php

$locations = [
    'New York' => getDateTimeByTimeZone('America/New_York'),
    'London' => getDateTimeByTimeZone('Europe/London'),
    'Tokyo' => getDateTimeByTimeZone('Asia/Tokyo')
];

foreach ($locations as $location => $time) {
    echo sprintf("%-10s %s\n", $location, $time);
}

function getDateTimeByTimeZone(string $timeZoneString): string {
    return (new DateTimeImmutable())
        ->setTimezone(new DateTimeZone($timeZoneString))
        ->format(DateTimeInterface::RFC822);
}

```

## Putting it all together

At this stage, make sure that you have initialised a Git repository in your package directory and committed your changes. This is required
before we can install and test our package in another repository. Ok, with that done, that is about it for the package itself so lets test i
it out.

You can do this by creating a new project and pulling in the dev branch of your package by first specifying in your project `composer.json`
(**not the package `composer.json`**) the following;

```json
{
    "repositories": [
        {
            "type": "vcs",
            "url": "../composer_packages_blog_post/"
        }
    ]
}
```

Next, simply install the dev branch of your package into the project with the following command

```bash
composer req alextheobold/composer_packages_blog_post @dev
```

If you have followed each step correctly, you should now see inside your project's `vendor` directory a `bin` directory and inside that
should be your executable binary. You can test this is working by running `./vendor/bin/my-demo-cli`.

## Wrapping up

It really is that simple to get started but this is just scratching the surface. There is so much more that you can do by taking in 
command line arguments and making the CLI more interactive to user input which ultimately leads to your packages being more useful and 
flexible to user demands.

Good luck, and please let me know if you found this guide useful. You can find me on [twitter](https://twitter.com/theoboldalex)
