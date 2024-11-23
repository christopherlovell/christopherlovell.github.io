---
title: "Converting WAV to MP3 in the terminal"
layout: post
comments: true
tags:
- Technology
date: "Tuesday, August 16, 2016"
excerpt: Convert WAV to MP3 through the terminal
---

Need to convert multiple WAV files to MP3 through the terminal? You need `ffmpeg`. Most commonly used for video conversions, `ffmpeg` can also be used to convert between audio formats.

Here's how to do a simple conversion from WAV to MP3:

```
ffmpeg -i test.wav -acodec mp3 test.mp3
```

You can also specify the bitrate of the MP3 with the `-ab` flag.

```
ffmpeg -i test.wav -acodec mp3 -ab 64k test.mp3
```
