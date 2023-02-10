---
title: "One Small Step (or; How to draw an Owl)"
date: 2023-02-10T08:48:36Z
draft: false
---

This week, my team started a new project. It is only a small piece of work and shouldn't take long to get into production, I thought.
What I didn't account for was that the team haven't built anything new in a long time (or in some cases, ever) as our focus has been
supporting existing applications for the past year.

To get us rolling, I quickly set up a repository for the code and installed a couple of dependencies for Unit testing and Static Analysis.
Just the bare bones so we could start building something. As the team didn't have a huge amount of experience in TDD, we decided that we would 
do some mob programming to get the ball rolling and give those less experienced members of the team some confidence in working this way
by observing and then trying out some TDD. I was tasked with guiding this mobbing session without being _too_ involved in the process, instead guiding
and questioning decisions along the way.

This started out great, we wrote a failing test; made it pass and then... Well, then we tried to draw the rest of the Owl. For those not 
familiar with that reference, see below;

![How to draw an Owl](/draw_an_owl.jpeg)

The problem, like in the above meme was that the feedback loop was far too large. I didn't want to push the team in a certain direction,
rather, I wanted the design to be led by the tests telling us what the next right step was. Unfortunately, when the steps are too big, we often 
jump to conclusions and try to write code that isn't yet required. The ultimate result of this was that the design missed the mark as
the team didn't tease outr the correct data structure by thinking about and writing tests, instead they wrote a songle test, then tried to write 
all of the application logic.
