#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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
