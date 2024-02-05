---
title: "🌶️ PHP Is My Favorite Language and I Will Never Be Embarrassed About It"
date: 2024-02-05T13:52:19Z
draft: false
---

## PHP is dead!

Upon reading his own obituary in 1897, author Mark Twain is reported to have said "Reports of my death are greatly exagerrated". Whenever I hear this
quote, I think of PHP (and to an extent, my first programming love Ruby which gets an unfair share of criticism too).

Far from being dead, PHP is evloving its feature set to include some of the most exciting features from functional languages such as 
[pattern matching](https://www.php.net/manual/en/control-structures.match.php) as well as performance improvements and general tidying of the language 
to meet the needs of modern developers.

PHP may not be one of the trendiest languages out there or attract the most hype but it certainly is one of the more productive and ergonomic languages
around, particularly when paired with a framework like Laravel.

## The Language

In recent years, the PHP language itself has seen major performance improvements and the difference in speed between PHP 5.x and PHP > 8.0 can be 
staggering. Performance is not everything though and developer experience is an equally important metric in all but the most niche of circumstances 
as [Taylor Otwell rightly pointed out](https://twitter.com/taylorotwell/status/1596636995039932416?s=46&t=RCAZzkPQYuvcyVZUqsZf3A).

The language has also introduced some nice "quality of life" features in recent releases such as [constructor property promotion](https://stitcher.io/blog/constructor-promotion-in-php-8),
[attributes](https://stitcher.io/blog/attributes-in-php-8), [named arguments](https://stitcher.io/blog/php-8-named-arguments), 
[the nullsafe operator](https://stitcher.io/blog/new-in-php-8#the-nullsafe-operator-rfc) more support for types including 
[static return type](https://stitcher.io/blog/new-in-php-8#union-types-rfc) and [union types](https://stitcher.io/blog/new-in-php-8#union-types-rfc)
and my absolute favorite new feature (after match expressions of course) [first classs callable syntax](https://www.php.net/manual/en/functions.first_class_callable_syntax.php).

## The Frameworks

Both Laravel and Symfony are fantastic web frameworks that are constantly improving their feature set and both projects are lead by opinionated leaders
that have a vision on the direction of travel. This may rub some people up the wrong way but it does make for a consistent experience and limits the
possibility of [creeping featuritis](http://www.catb.org/jargon/html/C/creeping-featuritis.html).

Laracon EU is in full swing as I write this and already after day one of the conference there have been some amazing reveals and showcases of some of 
the tools developed by the team and community around Laravel such as Laravel Herd Pro (which now runs on Windows too), Laravel Pulse and Laravel Reverb

## The Community

The PHP community is fantastic. Not only have I found it to be welcoming but also the ability for the community to laugh at itself (Lambos anyone?) flies in the face
of some of the more serious, pompous groups. The community are also constantly developing new and better tools with special shoutout going to the likes 
of [Nuno Maduro](https://www.youtube.com/@nunomaduro) who seems to have a knack for getting a new open source package released to the community sooner than you could imagine possible.

## The Tools

Ok, maybe I am biased on this one as I have contributed to a number of open source PHP projects and tools including Composer, Laravel, Symfony and MiniCli
to name a few but I have found some of the tooling around PHP to be excellent and at least as good as the competition from other languagues. I'm thinking
[PHPStan](https://phpstan.org/), [XDebug](https://xdebug.org/), [Composer](https://getcomposer.org/), 
[Intelephense](https://intelephense.com/). Not to mention paid tools like [PHPStorm](https://www.jetbrains.com/phpstorm/) and 
[Tinkerwell](https://tinkerwell.app/).


## The Future

While I don't think that PHP will cease to be the butt of many jokes for some time yet, I have been seeing a shift recently as more and more people,
especially those with a prominent online presence give modern PHP another chance. Two examples are Neovim (btw) ninja, Netflix (btw) engineer and Twitch
streamer [ThePrimeagen](https://www.youtube.com/@ThePrimeTimeagen) who went viral after he reacted to a video showing the latest features of modern PHP.
He even went as far to say that PHP is better than JavaScript. High praise indeed /s.

Another prominent content creator to try PHP and Laravel recently is NeoVim core team member and creator of some of the most heavily used NeoVim plugins
[TJ Devries](https://www.youtube.com/@teej_dv) who has been learning about Laravel on stream recently and considered building some NeoVim tooling specifically 
for Laravel developers. (He even visited [this very blog]({{< ref "intelephense_in_neovim">}}) while doing so). 

![Teej](/teej.png)

While I do have my frustrations with PHP from time to time, my problems generally are not PHP specific. Yeah ok, sometimes I get annoyed that I'm searching
for a haystack in a needle but this if this is the height of my problems then things are not at all bad (this can also be helped by some of the aforementioned tooling).

PHP is far from perfect but it is my workhorse. It gets shit done and for the most part stays out of my way. It may not tickle the intellect in the same 
way that Haskell might, or allow you to do the crazy type gymnastics associated with TypeScript but what it does do, is allow me to build cool shit
in an approachable way and adopt features such as static typing and functional programming techniques incrementally.

PHP is dead! Long live PHP!

:wq
