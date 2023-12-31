## 0x0F. Load balancer


<div class="panel-body">
<h2>Statistics Report</h2>
<a href="admin:your_password_here@http://100.27.13.221:8080/haproxy?stats#hbnb/364825-web-01"><img src="https://i.ibb.co/BnkzRhm/Screenshot-2023-10-04-at-18-27-21-Statistics-Report-for-HAProxy.png" alt="Screenshot-2023-10-04-at-18-27-21-Statistics-Report-for-HAProxy" border="0"></a>

<h2>Background Context</h2>

<p>You have been given 2 additional servers:</p>

<ul>
<li>gc-[STUDENT_ID]-web-02-XXXXXXXXXX</li>
<li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
</ul>

<p>Let’s improve our web stack so that there is <a href="/rltoken/xnAaJdhmAxx7PoH3l6EwDg" title="redundancy" target="_blank">redundancy</a> for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>

<p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/B7f3oz8i3Xvvom_YQZzLnQ" title="Introduction to load-balancing and HAproxy" target="_blank">Introduction to load-balancing and HAproxy</a> </li>
<li><a href="/rltoken/sZ9v3Vq2tgLwN_PWVQketw" title="HTTP header" target="_blank">HTTP header</a> </li>
<li><a href="/rltoken/2VRAgtKKR9g6Xfb0xzGiSg" title="Debian/Ubuntu HAProxy packages" target="_blank">Debian/Ubuntu HAProxy packages</a></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

  </div>