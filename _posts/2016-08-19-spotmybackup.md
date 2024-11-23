---
title: "Back up your Spotify Playlists"
layout: post
comments: true
tags:
- Technology
date: "Friday, August 19, 2016"
excerpt:
og_image: /images/spotify_logo.jpg
cover: /images/spotify_logo.jpg
---

Discovered the excellent <a href="https://github.com/bitsofpancake/spotify-backup" target="source">spotify-backup</a> recently, which swipes your entire spotify playlists. Useful if you're as paranoid as me about Spotify accidentally deleting your painstakingly curated content.

You'll need Python3, after that just clone the repo and run the line below in the directory. It should launch a window in your browser to authenticate with Spotify (if not, there are instructions on the site for manual authentication).

```
python3 spotify-backup.py playlists.json --format=json
```

I haven't found a working scraper for my entire library yet. If anyone is reading this and has seen the light, please let me know in the comments!
