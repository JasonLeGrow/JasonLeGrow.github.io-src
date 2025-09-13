#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason LeGrow'
SITENAME = 'Jason LeGrow'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Canada/Eastern'

# Copyright
COPYRIGHT_YEAR = '2024'
COPYRIGHT_NAME = 'Jason T. LeGrow'

DEFAULT_LANG = 'en'

# Where Pelican looks for stuff
STATIC_PATHS = ['images','teaching','cv']

SITELOGO = '/images/MyIcon.jpeg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('CV','/cv/JasonLeGrowCV.pdf'),
         ('VT Math','https://math.vt.edu/'),
         ('VTQ', 'https://vtq.vt.edu'))

# Social widget
SOCIAL = (('envelope','mailto:jlegrow@vt.edu'),
          ('linkedin', 'https://www.linkedin.com/in/jasonlegrow/'),
          ('twitter', 'https://twitter.com/jason_legrow'),
          ('github', 'https://github.com/jasonlegrow'))

DISABLE_URL_HASH = True

#DEFAULT_PAGINATION = False

# Change theme
# THEME = 'bootstrap'
# THEME = '../pelican-themes/bootstrap' #Actually works
# THEME = '../pelican-themes/myTheme'
THEME = '/Users/jasonlegrow/Documents/Projects/pelican-themes/myTheme/'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['autopages']
# PLUGINS = ['neighbors','i18n_subsites','tipue_search']

# Remove old files before creating new ones
DELETE_OUTPUT_DIRECTORY = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
# USE_GOOGLE_FONTS = False

# Change page ordering
PAGE_ORDER_BY = 'page-order'

# Markdown extensions
MARKDOWN = {
        'extension_configs':{
            'markdown.extensions.sane_lists' : {}
            }
        }
