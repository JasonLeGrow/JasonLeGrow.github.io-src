#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason LeGrow'
SITENAME = 'Jason LeGrow'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/jasonlegrow/'),)

DEFAULT_PAGINATION = False

# Change theme
THEME = '/home/jason/pelican-themes/bootstrap'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
# PLUGIN_PATHS = ['plugins']
# PLUGINS = ['autopages']

# Remove old files before creating new ones
DELETE_OUTPUT_DIRECTORY = True
