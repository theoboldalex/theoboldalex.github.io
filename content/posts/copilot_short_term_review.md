---
title: "Github Copilot - My First Thoughts After a Month of Daily Use"
date: 2025-07-01T21:45:47+01:00
draft: true
---

So it finally caught up with me. Github Copilot. The corporate darling of blazingly fast software delivery and cognitive rot. In this short term review I will make some attempt
to give an unbiased opinion of a tool I both despise _and_ think is massively overrated.

## The Good

### API Docs
In my first week of corporate enforced credit spunking, I found a reasonably useful side project for the cyborg intern to carry out while I attended a particulalry boring meeting.
I needed to hit some API endpoints on an unfamiliar service so, I opened Bruno client, created a collection and a quick `.bru` file for the service's ping endpoint. I then gave VSCode some context of the API
routes and prompted the agent mode with Claude Sonnet 4 model to ~~draw the rest of the fucking owl~~ implement the rest of the API routes.

This was useful, sure, but hardly groundbreaking. It saved me a couple of hours and made the API easier to ramp up on for other developers once I had raised my changes as a pull request, but really, I would 
have just written a curl command to hit the route I needed if I was not being forced to "accellerate delivery".

### Code Completions
_Some_ of the code suggestions have been fine, maybe saving me a few seconds here and there but honestly, even touch typing at a fairly modest 80wpm, I have never really found typing to be the bottleneck that the 
suits with skill issues seem to think it is. While there is some upside to having the suggestions, such as saving me typing out getters on my value objects, again, is this really worth the hype when tools like 
intellij have been able to auto generate getters, setters, constructors and more for over a decade? Hell, I could write a Vim or Emacs macro to a keybind in a few minutes that would do the same thing and be less likely to hallucinate.

## The Bad

### Vimrc for Zoomers

At this point, I am convinced that `.github/copilot-instructions.md` files are just this generations' equivalent to tweaking your Vim config. Overlaying the data for credit usage and pull requests raised, was 
an interesting study in the delivery of fuck all. I cannot say that I was surprised to see that the strongest engineers continue to be the strongest engineers with or without their annoying sidekick. The data 
does not lie.

### The Tooling
The tooling for anything other than Microsoft's VSCode just isn't up to much yet, especially if you want to use agent mode. I would be more inclined to give it a solid shot if the tooling for Neovim or Emacs was even half way usable. I did try PHPStorm too but that was the worst of the lot.

## The Ugly

### Blame the Bot
During the trial, there have been some incidents and outages, nothing out of the ordinary and no decrease from our usual levels of stability but what I have noticed is that people blame the bot now. 
I have pulled people up a couple of times when they have blamed Copilot for shipping a bug and reminded them that Copilot does not ship anything, it is you, the engineer that should remian in control and be
responsible for the testing of your changes (this is not helped by the fact that Copilot now writes all of the tests).

### The Bugs are a Feature Now
I have seen developers writing their code and then prompting Copilot to write the tests to cover the code. You are baking the bugs right into the tests you fucking idiot. Stop doing that, for the love of God.

## Conclusion

I have heard AI grifters claim time and time again that Copilot is like having an intern or a junior developer at your disposal. It is not like an intern or a junior developer, it is far more dangerous than that. Unlike a human, it does not ask questions, nor does it have impostor syndrome, the natural deterrent for junior developers to do anything _too_ stupid without first checking themselves with a more tenured colleague.

Also, unlike working with an actual human, with Copilot, I learn nothing from it. I just switch off my brain and spam tab or worse, sit in a meeting pretending to listen while the agent takes over my codebase and generates technical debt by the bucketload. When I work with human junior devs, they force me to explain things in simple terms, challenge my assumptions and help me to get better at communicating to a lesser knowledgable audience. With Copilot, it does whatever it thinks I have asked it to do with no compliants and the more code it writes, the more likely I am to slap a LGTM on it and ship it.

I really do not understand the corporates forcing engineers to use Copilot. The cynic in me (*dons tin foil hat) says that the only reason there is any interst in this at all is as a monitoring tool for developers. Not convinced it was a bad idea to measure lines of code or commits, we have a new metric in town. How many premium credits we can spunk up the wall just to show the user's birthday on the settings page. If there is any correllation between credits used and impact delivered, I am yet to see it.

The worst; absolute worst use I have seen of Copilot in the short time I have been using it though is those people that have outsourced their entire being to the AI. You know the ones. The ones where every message is clearly run through an AI tool. The ones where they ruin any kind of debate or discussion with their AI generated slop prose. The ones who when you ping them on Slack, you half expect a response to come back indicating that your message is important to them and that they are currently experiencing a particularly high volume of messages. To those people, I say, go fuck yourself.

:wq
