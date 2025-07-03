---
title: "Profiling ZSH - How I Made My Shell Startup Exponentially Faster (and borked my machine)"
date: 2025-07-03T19:44:04+01:00
draft: true
---

Flashback to 2023. I was working with Node on a project and needed to switch between versions easily. A quick Google search led me to [nvm](https://github.com/nvm-sh/nvm) (Node Version Manager)
which promised to allow me to install and use different Node versions via the command line. Perfect. Or so I thought.

I installed it without a second thought as you do with any script you find on the internet and I was away. It solved my problem and I was able to easily switch between Node versions as I pleased.
After a while though I began to notice something. Nothing major but something felt off. Slow. Not as snappy as I am used to. At first I couldn't pinpoint it but then one day it hit me. Starting up a new shell
was hanging. Only for a short while but noticeable and long enough just to throw me out of my flow. As someone that lives on the command line and spawns lots of short lived shell sessions via tmux, it was starting 
to become an issue. What had started as a solution, was now looking like a problem, but at this stage I had no idea what the culprit of my slow shell startup was. Without having looked into it, I was wondering
whether my old laptop was starting to struggle, but then the issue was also noticeable on my work machine which was vastly more powerful. I needed to figure out what was causing the slowness and quick because
when you are in a tool all day long and there is noticable lag and latency, it is a real productivity killer. It is one of the reasons why I am a shell and vim user in the first place. The speed and resource usage.

So I needed to figure out why my shell was slow to start up and had a couple of theories that proved to be false. I also considered uninstalling Oh My Zsh as I wondered whether that might be the culprit. I use 
barely any of the features other than a minimal prompt that I wrote myself including git branch information and zsh-autosuggestions which really, I could live without and instead rely on bck-search or fzf.

Before I did anything drastic though, I thought I would look into a profiling tool called `zprof` which had been mentioned in a couple of Stack Overflow posts while I had been researching around my issue.

`zprof` is simple a utility that comes pre-packaged with `zsh` and can be used to profile the shell. It is incredibly simple to use, but first I wanted to benchmark my shell startup time. To do this, I just did
a simple one liner on the command line to give me my shell startup time averaged out over 10 new sessions.

```shell
for i in {1..10}; do /usr/bin/time -f "Run $i: %e seconds" $SHELL -i -c exit; done
```
I was not looking for total accuracy here, just a quick ball park benchmark of the shell startup time. It did the trick. I could see that every time the shell started up, it was taking around 1 second for the 
prompt to be available. Far too long to be usable.

Ok, now I could get to finding the culprit of the slowness. To profile a `zsh` shell with `zprof` you need to edit your `.zshrc` like the following.

```shell
zmodload zsh/zprof

# The rest of your config

zprof
```

Once you have saved and sourced your config, you can now spawn a new shell and it will print out a table showing the slowest processes in a descending list. Bingo! `nvm` was taking up over 60% of the time it 
took to spawn a new shell. With `nvm` disabled, I then ran my benchmark and saw my shell startup time back down to below 1/10th second.

The only thing left to do now is remove the profiler calls from the `.zshrc` and resource so that the profiler does not run on every new session. Don't do what I did at this point though. 

At the time, I had a shell alias `nah` that I had picked up from somewhere (I think it was Freek Van Der Verten but not sure). It was a simple alias.

```shell
alias nah='git reset --hard;git clean -df'
```

This alias might seem pretty innocuous at first glance and it is, IF YOU RUN IT IN A DIRECTORY THAT IS UNDER VERSION CONTROL WITH GIT! Unfortunately for me, I ran it in my home directory where my `.zshrc` resided. By the time I had realised what was happening, it was too late. Far too late. Git had cleaned up all the unversioned files in my home directory. It was a bad day to be me.
