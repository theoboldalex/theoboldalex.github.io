---
title: "Say No To Story Points"
date: 2023-09-20T00:50:18+01:00
draft: false
---

Welcome to the Scrum universe, where there are just two unwavering certainties: developers will come to despise it, and if they dare to 
voice their complaints, they will be swiftly dismissed as "doing it wrong".

Scrum has committed untold crimes against programming; the most heinous of which is the
[flagrant and unapologetic affront to the very essence of software development]({{< ref "more_project_euler_in_vim">}}); story points.

## It's Official

The public blog of the _official_ Scrum guide has [this](https://www.scrum.org/resources/blog/why-do-we-use-story-points-estimating) to say about story points:

> Story Points are intended to make team estimating easier. Instead of looking at a product backlog item and estimating it in hours, teams consider only how much effort a product backlog item will require, relative to other product backlog items.

My first point of contention with the above is that any non-trivial programming task cannot be estimated to any level of accuracy in hours, days, even weeks in some cases so the comparison is pointless.

Secondly, the notion that we can or _should_ estimate units of work relative to each other leads to what I have come to call "Bikeshedding Unbounded".

## WTF is a five-pointer anyway?

Ok, let's say we are going to put our reservations aside briefly and give this relative estimation a try.

Shall we revisit the official Scrum guide blog for some guidance?

> For those unfamiliar with Story Points; teams that use this technique estimate effort with relative estimates instead of time-based estimates (e.g. hours, days). This is usually done with a simplified version of the Fibonacci sequence (0, 1, 2, 3, 5, 8, 13, 20, etc). The numbers have no meaning in themselves, but only in relation to other items. So an item of 5 points takes roughly twice as much effort from the team as an item of 3 points, and so on.

1. There is no such thing as a `simplified fibonacci sequence`. The fibonacci sequence is the fibonacci sequence. I like to call the sequence described here the `Pyrite Ratio`.
2. `The numbers have no meaning in themselves`... STOP! PLEASE, HE'S ALREADY DEAD!
3. `So an item of 5 points takes roughly twice as much effort from the team as an item of 3 points`: U wot m8?

I want to dig a little deeper into point three. Let's do the math:

`an item of 5 points takes roughly twice as much effort from the team as an item of 3 points`

Ok I'll let them get away with that one because they added the word `roughly`. I suppose 5 is _roughly_ double 3 in the same way that 
8 is double 5 and 13 is double 8 and 20 is double 13. At least the difference doubles every iteration so there is always that.

Where `Bikeshedding Unbounded` really gets going though is when trying to find consensus on a constant within the relative scoring system that
the entire team can agree on as a beacon around which all other backlog items can find their relative places.

If (and it is a big if) you can find enough common ground to avoid attmepted strangulation of your team mates and come to a consensus on what constitues a 
"five-pointer", you will likely then descend into my least favorite part of the whole process. The mental gymnastics associated with the `Pyrite Ratio`.

Taking the Scrum guide at face value, we can say that a backlog item of 5 points is double the effort of an item worth three points. Please tell me then;
does a backlog item of 8 points represent double the effort of a 5 point item or the combined effort of a 5 and a 3 point item?

## Taoist Tale

Let us pause and reflect on a story that may or may not be based on real events.

> One day during their lunch break, the young apprentice, Fu, approached his master, Bah, his face displaying a perplexed expression. Sensing Fu's inner turmoil, Master Bah invited him to share his concerns.
> With reverence, young Fu took a seat across from his wise master and inquired, "Master, I am curious. Why, when a sprint can effortlessly accommodate twenty story points, do we estimate two sprints for a project that is sized at only ten story points?"

> Master Bah responded with a knowing smile, selecting a small cracker from his plate. He gently broke it in half, placing the first portion into his mouth, savoring the taste as he chewed thoughtfully.

> In silence, he then adorned the second half with a pinch of salt before consuming it, all the while maintaining his serene smile. "Much improved," Master Bah remarked.

> In that singular moment, enlightenment washed over the young apprentice.

## Stifled creativity

Estimation discourages course correction. The Scrum literature claims that one of the framework's core benefits is that it allows you to `inspect
and adapt`. My experience is in direct contravention to this though. Estimating just leads to developers running with the first idea of a solution that
they have, never stopping to think whether the solution is _actually good_. This is not helped of course by non-technical stakeholders taking
estimates as deadlines and pushing development teams for ever more work in smaller timeframes.

Due to the inaccurate nature of estimations by definition, developers rush through units of work to keep client deadlines on course; 
inevitably producing projects which over time become unmaintainable, big balls of mud.

I am yet to see any non-trivial example contrary to this.

## Anti-Agile

Much of Scrum is purely a means for snake oil salesmen to make bank at the expense of companies that are trying to shift working methods in the hope that they stay 
relevant in a changing market. The framework claims to be a lightweight wrapper around agile methodologies yet I see no evidence for this, in fact,
Scrum as a whole, but especially estimation and story points are some of the most anti-agile practices out there. When the likes of Kent Beck, Uncle Bob,
Martin Fowler and Ward Cunningham signed the Manifesto for Agile Software Development, I'm not convinced that what they had in mind was perpetual 
meetings and selling certificates to corporate clients.

## An Alternate Approach

The primary purpose of any software team should be to deliver working software that provides business value. How long this takes should be directly
proportionate to the complexity of the problem being solved. It is my opinion that teams should maximise cognitive effort spent on understanding
the problem and stating it in simple terms. I like Rich Hickey's [Hammock Driven Development](https://www.youtube.com/watch?v=f84n5oFoZBc)
approach to this but each team will find what works for them.

If you are interested in casting off the shackles of story points here is my number one tip:

Continue to use story points. No, really.

It is unlikely that your boss will allow you to stop using them. Instead, point every story as 1 point. 
Your burn down chart will still function in much the same way it always has, keeping your boss happy and you will never have to think about points ever again.

If you do get any push back on your new found freedom from story points, simply direct your agressor's attention once again to the official Scrum guide blog which
states:

`Story Points are of no value whatever to a business because they can’t be used to predict cost or delivery dates. Even the Scrum team cannot make any predictions as to how many Story Points it can complete in a sprint`




:wq
