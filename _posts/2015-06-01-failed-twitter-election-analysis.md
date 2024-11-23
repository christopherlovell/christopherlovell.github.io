---
layout: post
title: "A failed twitter election analysis, and lessons learnt"
comments: true
date: "Sunday, June 14, 2015"
tags:
- Data Science
excerpt: Twitter, MongoDB and yournextmp.com prove no match for socially fickle parliamentarians  
---

I had grand data-based plans for the recent British general election. My 'novel' (as far as I'm aware) idea was to capture all tweets from the *candidates* over the election period, and do some time series analysis around the kinds of terms used. I've been developing a package to do term frequency analysis and visualisation, and this seemed like an exciting opportunity to show it off. It also presented a good excuse to refresh my python skills, by leveraging the [Tweepy](http://www.tweepy.org/) library, and learn the basics of MongoDB for storing all my tweets and user details.

I hit my first hurdle just trying to find the accounts for all the potential candidates. This was further complicated by the fact that, on parliament dissolving on the 30th of March, MPs were no longer MPs. They couldn't call themselves MPs in any communications, including twitter. For all those MPs who created their twitter accounts in the last 5 years, and short sightedly stuck these two letters in their twitter handle, they had to stop using the offending account and create a new one.

Fortunately a group of tireless individuals at [yournextmp.com](https://yournextmp.com/help/api/) have compiled an amazing data set of all the election candidates, updated after the dissolusion, with basic details such as age and sex, as well as social media contact information. It's all done by volunteers, so likely incomplete or inaccurate in a number of cases, but it was the nearest I was going to get to a list of twitter handles without collecting the information myself by hand.

With this information I started work. I wrote a script that looped through each account, grabbed the last 200 tweets, and put them in Mongo. If the given account already had tweets in the database, it would grab 200 of the next latest tweets, or as many as it could up to the very latest. If the tweets in the database were up to date, it would go back and grab a few more older tweets before the oldest tweet in the DB. I set it up this way so that I could run the script at any time, and get all tweets from the surrounding period so long as I left the script run for long enough. Easy.

Yet, not so easy. Because politicians can't even be trusted to keep their accounts open long enough for me to grab all their tweets. In keeping with their growing reputation of being useless social media test subjects, plenty of candidates (mostly those that lost or failed to win their seats, incidentally) chose to delete their accounts after the results came in on that fateful night after polling day. So, unless you collected the tweets before the account was deleted, the tweets associated with these accounts are lost. Forever.

Of course, I hadn't thought of this. The last time I ran my script was nearly a fortnight before polling day. I'd done some initial analysis to see if it was worth pursuing, and there were some interesting initial results. I naively thought I'd leave it until after polling day, grab all the latest tweets, complete my analysis, and publish, for wealth and glory. Things didn't quite turn out as I planned, but I learnt some important lessons about capturing this kind of volatile social information. Namely, get it while it's hot. Because you never know when your test subjects might decide to disappear half way through your experiment.

The code to carry out the analysis is available [here](https://github.com/christopherlovell/telenico2015). You can view my initial, rough analysis in PDF format [here](/assets/tweet_analysis.pdf). In a future post I'll introduce the code used to do the analysis in more detail, hopefully in conjunction with another event driven social media analysis.
