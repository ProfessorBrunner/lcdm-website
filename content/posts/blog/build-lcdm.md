Title: Building the LCDM Website
Slug: build-lcdm
Date: 2014-01-27
Authors: Robert J. Brunner
Tags: Pelican, LCDM, Python
Comments: True

<!-- PELICAN_BEGIN_SUMMARY -->

The LCDM website is built dynamically from static content, written
primarily in Markdown, by the Pelican static content generator. In
this blog post, I provide a basic summary of how the entire LCDM
website, minus large static file content, can be built by using the
github repository for the website and the custom LCDM theme.

<!-- PELICAN_END_SUMMARY -->

### Building the LCDM Website from Scratch

In a [previous post]({welcome-to-lcdm.md}), I wrote about how I chose
the [Pelican](https://github.com/getpelican/pelican) static site
generator to convert
[Markdown](http://daringfireball.net/projects/markdown/) content files
into the HTMl displayed on this website. As mentioned in that article,
the website content is archived on github, including the [LCDM Pelican
theme](https://github.com/ProfessorBrunner/lcdm-pelican) and the [LCDM
website content](https://github.com/ProfessorBrunner/lcdm-website).

Because of this approach, it is easy to start from a clean install and
regenerate the website (other than the static content consisting of
large PDF or code archive files, these are simply stored in the
appropriate locations within the main website). In this blog post, I
describe how to build the website in this manner. As I installed Pelican
in a separate virtual environment (i.e.,
[virtualenv](http://www.virtualenv.org/en/latest/), the first step is to
switch to the pelican virtual environment (as I am using
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
, this process is simplified). I plan to discuss the LCDM pelican
software stack installation in a subsequent post.

Basically, the following steps are all that is required

```bash
bigdog:~ rb$ cd /Volumes/Research/

bigdog:Research rb$ workon pelican

(pelican)bigdog:Research rb$ git clone 
    https://github.com/ProfessorBrunner/lcdm-website.git
    
(pelican)bigdog:Research rb$ cd lcdm-website/

(pelican)bigdog:lcdm-website rb$ git clone 
    https://github.com/ProfessorBrunner/lcdm-pelican.git
    
(pelican)bigdog:lcdm-website rb$ git clone 
    https://github.com/getpelican/pelican-plugins.git
```

At this point, you should have everything installed properly, leaving
you with the following:

```bash
(pelican)bigdog:lcdm-website rb$ ls
Makefile		develop_server.sh	pelican-plugins
README.md		fabfile.py		      pelicanconf.py
archive			lcdm-pelican		publishconf.py
content			lcdmwebsite.py
```

### Maintaining the LCDM Website with Github

At this point, the only person who can commit changes to the
lcdm-website is me, but if necessary we can fix that. To add a new or
modified file to eh github repository, you first need to `git add` the
file, and second, `git commit` the file to the local repository. Once
all changes have been made to the local cloned repository, you simply
push the changes to the master repository. For example, when I wrote the
news page stating my new appointment to the Beckman Institute (at the
same time I updated my .gitignore file, discussed below, to ignore the
pelican-plugins directory), I used the following commands to record the
changes in the github repository.

```bash
(pelican)bigdog:lcdm-website rb$ git add content/pages/news/baf.md
(pelican)bigdog:lcdm-website rb$ git add .gitignore
(pelican)bigdog:lcdm-website rb$ git commit -m"Added News item and ignore plugins"
[master b1d2acc] Added News item and ignore plugins
 2 files changed, 18 insertions(+)
 create mode 100644 content/pages/news/baf.md

(pelican)bigdog:lcdm-website rb$ git push origin master
Counting objects: 12, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.02 KiB | 0 bytes/s, done.
Total 7 (delta 3), reused 0 (delta 0)
To https://github.com/ProfessorBrunner/lcdm-website.git
   7aa0a3d..b1d2acc  master -> master
```

If at any time, you are unsure about the status of your cloned
repository, simply issue a `git status` command.

To simplify the updating of our git repository, I use the local
`.gitignore` file to specify the files that should be ignored by git.
This also will work with the `git status` command, so that only those
files that are relevant will be identified as untracked. For the LCDM
website, our `.gitignore` file is fairly simple:

```bash
(pelican)bigdog:lcdm-website rb$ cat .gitignore 
.DS_Store
output
lcdm-pelican
pelican-plugins
content/static/presentations
content/static/papers
content/static/code
```
### Automatic Rebuilds

One last item is the automatic regeneration of the full website. The
simplest technique to accomplish this task is to use a crontab entry
(even though Mac OSX has deprecated this feature in favor of their own
`Launchd`). To perform this track, I found a [blog post by
macdrifter](http://www.macdrifter.com/2013/05/the-road-to-pelican-32.
html) helpful. 

First I wrote a BASH shell script to invoke `make publish` and
subsequently copy, by using rsync since I want to only update, the new
html files over to the production server. The resultant BASH script is
called `lcdmregen.sh` and is archived in `bin` directory (note: I
removed all comments and some output formatting commands):

```bash
#!/bin/bash

export LANG=en_US.UTF-8

# Switch to the virtualenv and activate
cd /Users/rb/.virtualenvs/pelican
source bin/activate

# Relocate to LCDM website directory
cd /Volumes/Research/lcdm-website

# Copy over posts from RJB Dropbox
rsync -uav /Users/rb/Dropbox/work/posts/ content/posts/ 
    >> /Users/rb/logs/lcdm_cron.log 2>&1

# Run pelican in publish made and capture output.
make publish >> /Users/rb/logs/lcdm_cron.log 2>&1

# Copy output to official Webserver directory: 
# update, archive mode, use checksum for files, be verbose.
rsync -uacv output/ /Library/WebServer/Documents/ 
    >> /Users/rb/logs/lcdm_cron.log 2>&1

# Timestamp script
echo "*** Completed lcdmregen script: $(date) ***" 
    >> /Users/rb/logs/lcdm_cron.log 2>&1
```

Of the lines in this script, the only one not previously mentioned is
the first rsync. I want the freedom to be able to write blog posts
anywhere, and by using a special directory in my Dropbox account, I can
write a post using another compute, an iPad, or even my iPhone and have
the post automatically appear the next time the site rebuilds.

I wrote and installed, as shown below, the following crontab entry to
have the entire website automatically rebuilt every four hours. In this
manner, any new pages that I or anyone else with access to the webserver
machine can easily add new content to the LCDM group website.

```bash
(pelican)bigdog:~ rb$ cat ~/bin/crontab.txt 
0 0/4 * * * /Users/rb/bin/lcdmregen.sh

(pelican)bigdog:~ rb$ crontab bin/crontab.txt 

(pelican)bigdog:~ rb$ crontab -l
0 0 */4 * * /Users/rb/bin/lcdmregen.sh
```

Of course, the regeneration BASH script can be run at other times to
rebuild the site. Anyone with access to the webserver machine should
have permission to run the script to rebuild the site.
