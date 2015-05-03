#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Navin Pai'
SITENAME = u'The GSoC Diaries'
SITEURL = 'http://navinpai.github.com/gsoc-blog'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

THEME='themes/svbhack'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [('GSoC','https://www.google-melange.com/gsoc/homepage/google/gsoc2015'),('DBpedia','http://wiki.dbpedia.org'), ('JSONpedia','http://jsonpedia.org')]

# Social widget
SOCIAL = (('@navinpai', 'http://twitter.com/navinpai'),
		('Personal Blog', 'http://lifeofnav.in'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


###### SPECIFIC TO SVBHACK

USER_LOGO_URL = SITEURL + '/theme/images/logo.jpg'
TAGLINE = 'GSoC 2015 | DBpedia'
#######

OUTPUT_PATH = 'outpt/'
