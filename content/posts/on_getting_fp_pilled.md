---
title: "On Getting FP Pilled"
date: 2024-11-19T22:22:25Z
draft: false
---

## The Beginnings: Problem-Solving and JavaScript Adventures

My journey into programming wasn’t smooth at first. After a few false starts learning Python in the early 2010s and dabbling in SQL for work, I discovered [Project Euler](https://projecteuler.net/). Its addictive problem-solving challenges resonated with me. I wasn’t just solving problems; I was experimenting with clever and creative ways to approach them. Performance and readability took a backseat to fun.

This experimental phase led me to JavaScript, supported by Kyle Simpson’s seminal [You don't know JS](https://github.com/getify/You-Dont-Know-JS). These books encouraged me to explore the language deeply, sparking a fascination with higher-order functions, immutability, and method chaining. A prime example of this approach is solving the classic FizzBuzz:

```JavaScript
[...Array(100).keys()]
    .map(i => i + 1)
    .map(i => i % 15 === 0 ? "FizzBuzz" : i % 3 === 0 ? "Fizz" : i % 5 === 0 ? "Buzz" : i)
```

At the time, I didn’t realize I was learning functional programming principles. Treating programs as pipelines of data transformations rather than state mutations came naturally. Later, as I ventured into Ruby and PHP, I realized just how much this mindset shaped my approach to coding. FP felt intuitive; object-oriented programming (OOP) took more effort to grasp.

## Discovering Clojure: Fun Rediscovered

A pivotal moment came when I stumbled upon a Rich Hickey conference talk that introduced me to Clojure. This Lisp-inspired language rekindled the joy of programming that had been missing from my day job. It was my first truly functional language, and its expressiveness blew me away. The simplicity and elegance of Lisp matched my mental model for how programming languages should work.

That said, Clojure wasn’t without its challenges. Its minimalistic, library-focused ecosystem clashed with my preference for more "batteries-included" frameworks, honed during my time with Rails and Laravel. While Clojure remains my go-to for pure programming challenges like Advent of Code, I’ve found it less practical for larger software projects.

## Functional Programming in the Unix Shell

In 2023, I took on Advent of Code with a twist: solving challenges using shell scripting and Awk. This deepened my appreciation for Unix's philosophy of small, composable tools connected by pipes. The shell embodies functional programming principles: input transforms into output through a pipeline of operations.

While I only made it a few days into Advent of Code, the experience sharpened my skills and reinforced my belief that FP is both simpler and better suited to many real-world programming tasks.


## Exploring New Paradigms: OCaml, Haskell, and the Joy of Elixir

This year, I declared 2024 the “Year of the Emacs Desktop” and dove into Elisp, Scheme, and MIT Press’s [The Little Schemer](https://vpb.smallyu.net/[Type]%20books/The%20Little%20Schemer.pdf). This book reshaped my understanding of recursion—not just conceptually, but practically. It’s a skill few of my peers fully embrace, and I now feel confident leveraging it in my work.

I also explored OCaml and Haskell, two powerful languages that have piqued my curiosity. But it was a chance encounter with Joe Armstrong’s talks on Erlang that set me on my current path: discovering Elixir.

## Falling for Elixir: A Practical and Functional Powerhouse
Elixir, a language built on the same BEAM VM as Erlang, captivated me immediately. Created by a former Rails contributor, it offers the productivity of frameworks like Laravel with the functional elegance I love.

Within my first week, I built a Phoenix web app with LiveView and solved Advent of Code problems with ease. The framework's speed, scalability, and simplicity astonished me. Writing rich client experiences without JavaScript? Sign me up. The community was another highlight—welcoming, helpful, and patient with my newbie questions.

Here’s what FizzBuzz looks like in Elixir:

```Elixir
1..100 |> Enum.map(fn i -> cond do
    rem(i, 15) == 0 -> "FizzBuzz"
    rem(i, 3) == 0 -> "Fizz"
    rem(i, 5) == 0 -> "Buzz"
    true -> i
    end
end)
```
While I still prefer Clojure’s syntax, Elixir’s pipeline operator makes data transformations effortless. Comparing this to PHP’s equivalent for a simple Advent of Code solution highlights how FP can simplify complex tasks:

```PHP
<?php declare(strict_types=1);

echo array_reduce(
    array_map(
        fn (string $i) => intval(substr($i, 0, 1) . substr($i, -1)),
        preg_replace(
            "/[^\d]/",
            '',
            preg_split(
                pattern: "/\n/",
                subject: file_get_contents(__DIR__ . "/real.txt"),
                flags: PREG_SPLIT_NO_EMPTY
            )
        )
    ),
    fn (?int $a, ?int $b) => $a + $b
);

```
The difference in readability and maintainability speaks for itself.

## Wrapping Up

Is Elixir a silver bullet? No. Will I use it for every project? Absolutely not. But I’ve found immense joy and productivity in this language. Over the coming months, I look forward to sharing more about my Elixir adventures and the fantastic ecosystem it offers.

Functional programming has transformed how I write code. It’s a mindset that prioritizes simplicity, elegance, and efficiency. Whether it’s Clojure, shell scripting, or Elixir, FP continues to shape my journey—and I couldn’t be more excited to see where it leads next.
