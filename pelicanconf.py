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
LINKS = (('Combinatorics and Optimization', 'https://uwaterloo.ca/combinatorics-and-optimization/'),
          ('Institue for Quantum Computing', 'https://uwaterloo.ca/institute-for-quantum-computing/'),
         )

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/jasonlegrow/'),)

DEFAULT_PAGINATION = False

# Change theme
THEME = '/home/jason/pelican-themes/bootstrap' #Actually works
# THEME = '/home/jason/pelican-themes/pelican-blue'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['/home/jason/pelican-plugins']
PLUGINS = ['autopages']
# PLUGINS = ['neighbors','i18n_subsites','tipue_search']

# Remove old files before creating new ones
DELETE_OUTPUT_DIRECTORY = True

# Needed for some themes
# DIRECT_TEMPLATES = ['category', 'blog-index']
# PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# For pelican-blue
# SIDEBAR_DIGEST = 'PhD Student in Post-Quantum Cryptography'

# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True

# Change page ordering
PAGE_ORDER_BY = 'page-order'
