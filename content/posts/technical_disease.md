---
title: "Technical Disease"
date: 2023-12-15T21:16:31Z
draft: false
---

We developers love to talk about tech debt. In fact, we love the subject so much that it seems to pervade every discussion we have; sometimes
in ways we don't even notice.

## Exhibit 1 - The Big PR

[Cory House says it better than I ever could](https://twitter.com/housecor/status/1735673153894900212?s=20) 
so I will leave it to him, but I see this so often that it is not even funny at this point.

If a massive PR is urgent enough to forego quality, that is a major red flag. The truth is, that it is not urgent, there is just external pressure.

The difficulty as a technical leader is standing firm and doing the _right_ thing in scenarios like this given external pressures to 
"Get shit done". I don't always get this right.

## Exhibit 2 - The JFDI

Speaking of "Getting shit done" and external pressures, a theme that comes up time and again in incident retrospectives when something has gone 
wrong is the notion of a JFDI. A JFDI for the uninitiated stands for "Just F***ing Do It". JFDIs mostly come from senior business leaders and are 
usually either unclear in scope and requirements, have unrealistic deadlines, or most commonly, both.

The problem here is that quality is the first thing to go out of the window in these situations and that is what leads to problems.

A small amount of technical debt is not a problem if something is truly urgent; however, most things that seem urgent are not. Also, the second
step is paying down that debt at the earliest reasonable opportunity but this seldom happens. Creating technical debt like this may provide short
term business value but long term, it does not.

## Business Value? For Whom?

"Business value" is a term that is thrown around with abandon these days. The problem is that it is not measurable in any meaningful way.
Value is entirely dependent on perspective. What is important for one stakeholder is not necessarily important for another. The problem arises
when the perspective of the technical teams in not heard. I have heard countless horror stories of companies where developers don't write
tests because "the business" says it slows them down. I have also spoken with developers in my own organisation that have told me that they don't 
have time to refactor their code. This shocks me and I always remind these developers that testing and refactoring are part of engineering 
practice. Business leaders may have the remit to decide _what_ we work on but, the _way_ we work is nobody's business but ours. 
I will die on this hill.

## So what do we do about it?

So, we have decided to make a concerted effort to pay down our technical debt. How then should we approach this? Well, lets stick with the 
financial metaphor and pull at that thread a little.

If we had financial debt, a good plan might be to;

### Step 1 - Create a Budget

Look at everything coming in and everything going out. Seeing the problem in its entirety helps us come up with a sensible plan of action.

### Step 2 - Stop Spending Beyond Our Means

Imagine you are in a boat that has a leak. Bailing water out of the boat is of no use whatsoever until you have plugged the leak. We need to 
dedicate time and effort to make sure that we are not just paying down our existing debt but we are also ensuring the quality of new work is not
exacerbating the problem.

### Step 3 - Pay Down the Highest Interest Debt

Identify which debt is having the most impact on your ability to work on the product. Many organisations have gone through "Agile Transformations"
which generally means "We do Waterfall but without the planning". 

The Oxford English Dictionary defines the word `agile` to mean "Able to move (esp. to climb or manoeuvre) quickly and easily;". 
Every implementation I have seen has forgone the "easily" part so that we can move fast. This is a fools errand though because unless we can 
move easily, we will never move fast.

_sidenote: the irony is not lost on me that until the 1500s, the word agile actually meant "To decieve or entrap"._

### Step 4 - Iterate on Step 3

I believe this to be a good plan for approaching paying down technical debt and other metaphors also work here with an almost identical set of steps
to success. Instead consider the problem as "Techincal Disease" rather than debt. The disease in this metaphor can be obesity.
A good plan to lose weight and tackle obesity does not begin with buying a treadmill or investing in sportswear,
it begins by stopping eating so much and focussing on putting less, but higher quality food in your body.

## Conclusion

The idea of spending time paying down tech debt is not a new one, in fact it has been right there in the metaphor since Ward Cunningham first coined the 
phrase.

> "Shipping first-time code is like going into debt. A little debt speeds development so long as it is paid back promptly with refactoring."
>
> _Ward Cunningham_

Many of the reasons we end up with a problem with technical debt is that we have forgone technical excellence to move faster.
I lay much of the blame on Agile (with a capital A) for this as the obsession with moving quickly and measuring the wrong things 
incentivises shipping first time code and punishes course correction. The problem is not (lower case) agile as it is right there in the
`Manifesto for Agile Software Development` and always has been. 

> "Continuous attention to technical excellence and good design enhances agility."

Without a focus on quality in all but the most urgent of cases (which should be anomolous) we cannot deal with the problem of technical debt 
and will be consigned to perpetually kicking the can down the road.

My last thought is this;

We don't have to pay down all of our debt today, or even this year; what we need to do, is to stop the rot and build good engineering practices
which value technical excellence above all else. Only once we have done this, can we begin to pay down old debts and avoid being on a constant treadmill
of taking and paying down debt. If the debt continues unmanaged, eventually the interest will compound and cause technical death where the system
is so broken it cannot be fixed.

:wq
