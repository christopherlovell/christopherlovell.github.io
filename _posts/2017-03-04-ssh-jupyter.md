---
title:  "Accessing Jupyter over SSH"
layout: post
comments: true
tags:
- Technology
date: "Saturday, March 4, 2017"
excerpt: Remotely access Jupyter notebooks through SSH
---

If you spend a lot of time on a remote machine and want the flexibility and interactivity of Jupyter notebooks, here's a short guide on how to access notebooks on the remote from your local browser.

You first need to start Jupyter on the server. Log in, navigate to the directory you want to serve, then start the server:

{% highlight bash %}
remote-user@remote-host$ jupyter notebook --no-browser --port=8888
{% endhighlight %}

The `--no-browser` flag stops it launching a browser instance from the server. The port number should also be free - if the port is busy, or being used by someone else, Jupyter will throw a warning and try a different port automatically. Make sure you take note of the exact port Jupyter eventually uses.

We can now try to access the Jupyter instance from our local machine. Open a terminal and start an SSH tunnel:

{% highlight bash %}
$ ssh -i ~/.ssh/id_rsa.pub -NL 8157:localhost:8888 remote-user@remote-host
{% endhighlight %}

The `N` flag prevents a shell prompt coming up (ideal for port forwarding). You can also request that the command goes to background with the `-f` flag, so you can still use the terminal afterwards. The `-L` flag list the port forwarding configuration. Here, `8157` is the local port, and `localhost:8888` is the port used on the remote (the one we specified earlier). Finally, you need the username and address of the machine you're trying to access (`remote-user@remote-host`). If you have credentials saved locally, you can access these by pointing to your identity file with the `-i` flag.

You can now got to your local browser and navigate to `localhost:8157`, and Jupyter on the remote host should load.

You've made it! Now go crunch some data.
