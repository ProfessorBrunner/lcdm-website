#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Custom Pelican configuration file.
# For LCDM: Robert J. Brunner
#
# Note: Need to look at using Typekit to get fonts (https://typekit.com)
# Note: Also, IcoMoon to get icon fonts (http://icomoon.io)
# Note: Maybe look at skeleton as a framework to build scaleable CSS.
# This includes for mobile (http://www.getskeleton.com)

# This version of the configuration file assumes the following:
# 1) All articles are in the pages directory
# 2) Articles provide a save_as tag to specify save location
# 3) All posts are in posts directory.
# 4) News items are articles and placed in posts directory
# 5) Blog posts are articles in posts directory. 

# Add these to allow custom jinja2 & Python code

from datetime import datetime

# RJB 12/16/2013
# This function checks to see if the inpute date is within three months
# of today. No day comparisons are made.
# This is for my custom lcdm Pelican theme.

def recentNews(dt, months = 3):
    td = datetime.today()
    
    # If years match, simply check the month difference
    if ((dt.year == td.year) and 
        ((int(dt.month) + (months - 1)) >= int(td.month))):
        return True
    
    # If post was from last year, we increment current month by 12
    elif ((dt.year == (td.year - 1)) and 
        ((int(dt.month) + (months - 1)) >= int(td.month + 12))):
        return True

    return False

# RJB 01/03/2014
# Format Unicode string to date for HTML

def lcdmDateFormat(str, format='%b %d, %Y'):
    date = datetime.strptime(str, "%Y-%m-%d")
    return date.strftime(format) 

# This method dumps the values associated with a given variable. Used for debugging.
# Use with contents or page, or pages. For example, 
# {{ contents|show_all_attrs }}
# {{ pages |show_all_attrs }}
# {{ page |show_all_attrs }}

def show_all_attrs(value):
    res = []
    for k in dir(value):
        res.append('%r %r\n <br />' % (k, getattr(value, k)))
    return '\n'.join(res)
    
# Add the new jinja extension filter
JINJA_FILTERS = { 'recentNews': recentNews, 'lcdmDateFormat' : lcdmDateFormat, 'show_all_attrs': show_all_attrs }

# Standard Pelican material

AUTHOR = u'Robert J. Brunner'
SITENAME = u'Laboratory for Cosmological Data Mining'
SITEURL = 'http://localhost:8080'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TIMEZONE = 'America/Chicago'

# By default use filesystem date
FALLBACK_ON_FS_DATE = "True"
DEFAULT_DATE = 'fs'

DEFAULT_LANG = u'en'

# These are linked in my sidebar.

LCDM_PAGES = (('Research', '/research.html'),
              ('&nbsp;&nbsp;Blog', '/blog/index.html'),
              ('&nbsp;&nbsp;Code', '/code.html'),
              ('&nbsp;&nbsp;Data', '/data.html'),
              ('&nbsp;&nbsp;Papers', '/papers.html'),
              ('&nbsp;&nbsp;Presentations', '/presentations.html'),
#              ('Projects', '/projects.html'),
              ('Teaching', '/teaching.html'),
              ('&nbsp; ', '&nbsp;'),
              ('Group Members', '/people.html'),
              ('&nbsp; ', '&nbsp;'))
              
# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/ProfessorBrunner'),
          ('LinkedIn', 'http://www.linkedin.com/pub/robert-brunner/33/75b/ba6'),
          ('Twitter', 'https://twitter.com/ProfBrunner'))

ACTIVE = 'Blog'

# All static content is placed in static directory, including images

STATIC_PATHS = ['static']

# Most of he LCDM site is built from pages, not articles. So I need to build a work 
# around to make the page approach work with my needs.
#
# 1) I put all pages inside the pages directory.
# 2) I inform pelican to only look at this directory for pages
# 3) I use a hierarchical directory structure for pages.
#    This means I have Research, Code, Data, and Teaching subdirectories inside pages.
#    I also have subdirectories within those directories. Each directory 
#    (other than pages) also has a markdown file with appropriate tags that is 
#    converted into the equivalent of an index.html file for that directory.

#USE_FOLDER_AS_CATEGORY = True

#  Tried parsing path to pull out category, also tried EXTRA_PATH_METADATA
#PATH_METADATA = r'^(?:pages/)?(?P<category>[\w/]*)/(?P<slug>[\w]*)\.md$'

PAGE_DIR = ('pages')
PAGE_EXCLUDES = (('static'), ('posts'))

PAGE_URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{category}/{slug}.html'

ARTICLE_DIR = ('posts') 
ARTICLE_EXCLUDES = ('pages', 'static')

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Note you can't use '-' in variable names, doing so caused a problem in
# the LCDMPOSTS_SAVE_AS variable with Pelican.

DIRECT_TEMPLATES = (('index', 'articles', 'news'))
#DIRECT_TEMPLATES = (('index', 'articles', 'news', 'papers', 'projects', 'presentations'))
PAGINATED_DIRECT_TEMPLATES = (('articles', 'news'))
ARTICLES_SAVE_AS = ('blog/index.html')
NEWS_SAVE_AS = ('news/index.html')

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 2

# I do not want individual author, individual tag, or bulk category html files.
#CATEGORY_URL = '{category}'

CATEGORY_SAVE_AS = 'extra/category/{slug}/index.html'
AUTHOR_SAVE_AS = 'extra/author/{slug}/index.html'
TAG_URL = 'extra/tag/{slug}/'
TAG_SAVE_AS = 'extra/tag/{slug}/index.html'

CATEGORIES_SAVE_AS = 'extra/categories.html'

AUTHORS_SAVE_AS = 'extra/authors.html'
TAGS_URL = 'extra/tags/'
TAGS_SAVE_AS = 'extra/tags/index.html'

# Serve all source files. While I would like to do this, right now it
# makes a directory and simply copies the md file into that directory
# (teaching.txt, for example. i wanted the file to be viewable as is.
#OUTPUT_SOURCES = True
#OUTPUT_SOURCES_EXTENSION = '.txt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# git clone repositories for themes and plugins locally

THEME = 'lcdm-pelican'

# Setting for the better_figures_and_images plugin

#RESPONSIVE_IMAGES = True

# Note, since I am using the better_figures_and_images plugin, every
# image must have the {filename} prepended, even if I am simply using
# the <img> tage. Otherwise page doesn't build properly.

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['latex', 'summary', 'assets']#, 'better_figures_and_images']

# Allow Latex
LATEX = ('articles', 'posts', 'pages')
