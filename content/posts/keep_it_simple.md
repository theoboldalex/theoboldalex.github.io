---
title: "On the value of simplicity"
date: 2022-12-17T13:37:31Z
draft: false
---

As somebody that espouses the benefits of simplicity and the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy), I disappointed myself
on multiple occassions this week. In both instances, I missed the obvious and simple soultion to a problem by overcomplicating things
and asking the wrong questions.

In the first instance, my team wrote hundreds of lines of Python to achieve a task that could have easily been done through a CLI that
was available to us. Granted, in this instance, I wasn't particulalry close to the problem being worked on, but could and maybe _should_
have noticed this and highlighted it to those working on the problem.

In the second instance, we needed to hit an endpoint thousands of times in order to generate some documents. I'm embarrased to say that
even after an example earlier in the week of overcomplicating a problem, my initial approach was to crack open vim and start writing a script
to solve the problem rather than breaking down the problem into the most managable chunks and using command line utilities to turn
what seemed like a problem that could take all day into a problem that takes five minutes and a one liner in the terminal. 
Thankfully we had someone on hand to point out the blooming obvious and save us writing even a single line of code.

Maybe this over complication of problems is a symptom of having been working mainly in a support capacity recently and without any meaty
projects to get stuck into, my hands and brain are itching to write code and create something, or maybe it is just another stop on the 
developer maturity journey. Either way, I now have the self awareness to look for instances where I am over complicating things. The most
disappointing thing about both of these problems, is that these are all things that I already know, but it's not just that, these are ideas 
that I advocate for to others and this week, when the crunch came, I was found wanting. Twice.

I think [The Zen of Python](https://peps.python.org/pep-0020/) articluates it best when it says "Simple is better than complex.
Complex is better than complicated." and I will keep this in mind when approaching problems in future. If I can take the 
[Unix as an IDE](https://blog.sanctum.geek.nz/series/unix-as-ide/) approach to my development environment as I do, I can certainly
take some of the same ideas into solving real business problems because after all, the aim is to deliver the most amount of value for 
the least amount of effort and I believe that this is exactly what the unix philosophy is all about. Simple, minimalist and modular tools
that can be composed to solve complex problems in simple ways.
