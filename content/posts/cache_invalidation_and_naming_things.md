---
title: "10 Habits of Highly Destructive Developers"
date: 2023-05-12T09:39:15+01:00
draft: false
---

There are plenty of posts online about what makes a great developer so in this post I'm going to take
a different, slightly tongue in cheek approach and look at 10 things that really bug me when working on tech teams.

### *disclaimer: this is a bit of a rant/vent but it is not intended to offend anyone

## 1. Adding `Data` to variable names

This one is my personal biggest bug bear when reviewing Pull Requests. It is littered everywhere, and _I mean everywhere!!!_
`getData`, `orderData`, `customerData`. For me, seeing this word is an instant red flag that there could be a better name. 
For instance; `orderData` becomes `orders` if it is a list like structure or `order` if a single object. Likewise `customerData` becomes
`customer/customers` dependent on the context of what is held in the variable. Finally, `getData`? Come on we can do better than that!

## 2. Unhelpful commit messages

The power of good commit messages generally only becomes apparent when the pressure is on. Usually when something has blown up in production
and you are trying to find the offending commit that caused the outage. An example that springs to mind is a PR I saw recently where 5 commits
in a row had the same, unhelpful commit message. Simply `refactor`. The irony here is that none of those commits contained any refactoring,
it was all logic changes and adding tests which tells me either they don't know what refactoring means or they were being lazy. At least they are
writing tests though, I suppose.

## 3. Unfocussed PRs

This has become more apparent since I took a leadership role but the amount of PRs that are not focussed on a single change is scary. I think
that this is one of the main contributing factors in people struggling to find appropriate names for things is that the changes aren't focussed
enough in order to give clarity of vision on what impact the PR is supposed to have.

## 4. Inability to articulate technical details

Maybe this one is just the way the tech industry works but I have found that in a majority of cases, when I ask questions to dig deeper into technical
decisions, the questions are just hand waved. Sometimes, I'll double down but increasingly, it is becoming apparent that many people don't understand
the code they are writing, they are simply duct-taping things together.

## 5. Not having a command of their tools

OK OK, maybe I'm a bit biased on this one being a self-confessed terminal and vim nerd who wants to know the most efficient way to wield my tools
but, I'm amazed to see that in 2023 there are still people working out there as developers who can't touch type, are unable to use a terminal and don't 
know how to setup their own dev environment. (There is also that guy who always opens text files in Nano, but I'll let him off because he does this
purely because he knows it gets a rise out of me).

## 6. Weak grasp on fundamentals

I'm a self taught programmer so missed out on a bunch of the theoretical and foundational education that university educated developers benefit from
but one thing I did learn was that a strong grasp of programming fundamentals will take you a long way (thanks to my Dad for telling me this when I was 
getting started with programming). Things like data structures and algorithms, design patterns, how DNS works etc etc. The more people I speak to the more I realise
that the basics have been passed over in favour of learning shiny new frameworks and tools instead of the underlying tech. Maybe this will come back to bite 
me at some stage but it has served me well so far.

## 7. Not contributing to team discussions

Teams can only be effective when everyone contributes. Not just code, but also to technical discussions. This is hard in a remote first world where
it is pretty easy to hide during meetings with cameras and microphones turned off. I have made it a habit of asking for people's opinions directly during
meetings to try to combat this. It isn't as effective as I'd like it to be.

## 8. Not being available

As developers, we all know how important heads down time is when working on code but you should at least be reachable when working as part of a team.
It is pretty obvious to the trained eye when someone is bluffing their way through a daily standup because they didn't do any work the previous day.

I wish I could say that I hadn't done this myself but that would be a lie. :)

## 9. Telling porkies

Logs don't lie. This is one that has become apparent since taking on a leadership role. The amount of 'little white lies' that are told to managers
is higher than you would like to imagine. Example: 

Me: Hey, did you check that code in you said you were going to?
Them: Yeah I did it before I left for the day.
Me: Checks Git Logs next day. Hmmm, how did you commit this in the future?

## 10. Ranting about other developer's habits on their blog

Yep, that is me. When working in close knit teams on complex, often time pressured projects, conflict is inevitable. I'm certain that each and every 
coworker I have ever had could list at least 10 things I do that bugs them. All of the above points are based on true events but ultimately, I have written
them down not to publicly humiliate or point and laugh at but to highlight things we can do better, most of which don't require too much effort.

When Kent Beck said that he isn't a great programmer, just an average programmer with great habits, I believe him. Teams are so much more 
effective when their habits, routines and discipline are on point than if they are technical wizards that are horrible to work with.
