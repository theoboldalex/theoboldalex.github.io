---
title: "Maslows Lambda"
date: 2023-09-04T21:18:07+01:00
draft: true
---

Lately, I have been using and contributing to [Bref](https://bref.sh/). It is a fantastic tool and allows me to write serverless functions
in PHP on AWS Lambda. This is a great thing no doubt. Not only can I write Lambda functions in a language that feels really comfortable, 
but through Composer, I also have access to all my favorite packages.

Bref also allows running entire Laravel and Symfony applications inside a Lambda function too and because it is built on top of Serverless framework, deployment is as simple as a single command.

Now, how could I have any complaints against a tool that makes my life so easy? Well, I don't actually have any complaints against Bref as such but a problem I _am_ having is that I now see every application as a Lambda. Mainly due to how easy setup and deployment is and it has made me somewhat lazy with my sideprojects. It has become somewhat a Maslow's Hammer.

At AWS Summit London in early 2022, I attended a lot of talks where serverless workloads were pushed hard and a less skeptical mind might beforgiven for thinking that serverless is all upside with no downside. After coming home from that conference I experimented with Serverless framework and some AWS CDK and found them fine but not as earth shattering as I had been led to believe. Yeah, it was great, I didn't have to manage my own servers, it was incredibly easy to deploy and with the level of traffic these apps were expecting, the workloads would be essentially free; forever.

This post is a bit of a call to arms for me to get back to using the right deployment model for the task at hand, whether that is the decidedly untrendy EC2, ECS, Lambda or whatever else suits the project.
