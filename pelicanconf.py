#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Soroush Javidi'
SITENAME = 'SOROU.SH'
SITEURL = ''
SITESUBTITLE = ''

SITE_DESCRIPTION = "Hello, I'm Soroush Javidi, and this is my website. I list my work and write articles on topics that interest me."
SITE_KEYWORDS = 'Soroush, Javidi, Signal Processing, Machine Learning, Finance, Research, Programming, Algorithm, Python, Rapid Application Development, MATLAB'

GOOGLE_VERIFICATION = 'BJJK_2K6ly1OjytWJxk-FxUqBKxe5qiS1bg0pFsBWhM'

PATH = 'content'

TIMEZONE = 'Europe/London'

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
SOCIAL = (('linkedin', 'http://uk.linkedin.com/in/soroushjavidi'),
          ('github', 'http://github.com/yrex'),
          ('gitlab', 'http://gitlab.com/yrex'),
          ('email', 'mailto:my-name-dot-surname-at-this-domain'),)

DEFAULT_PAGINATION = 10

MENUITEMS = [('Posts','/posts')]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Themes
# THEME = 'themes/notmyidea2'
# THEME = '../custom-pelican-themes/mnmlist2'
THEME = '../custom-pelican-themes/pelican-bootstrap32'
BOOTSTRAP_THEME = 'yeti'
CUSTOM_CSS = 'files/custom.css'
FAVICON = 'favicon.ico'
# PYGMENTS_STYLE = 'vim'
SITELOGO = 'images/SJ_logo_W.png'
SITELOGO_SIZE = '25'
BOOTSTRAP_NAVBAR_INVERSE = False
HIDE_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
# BANNER = 'images/banner2.jpg'
# BANNER_ALL_PAGES = True
# ABOUT_ME = ' '
AVATAR = 'images/SJ_logo_BW.png'
# CC_LICENSE = 'CC-BY-SA'


STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/robots.txt': {'path': 'robots.txt'},
}

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap', 'posts')
PAGINATED_DIRECT_TEMPLATES = ('posts', 'index')

DISPLAY_CATEGORIES_ON_MENU = False
# DISPLAY_PAGES_ON_MENU = False

# Article URL Settings
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Page URL Settings
PAGE_URL = '{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Author URL Settings
# AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = ''

# Category URL Settings
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'

# Tag URL Settings
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

# Sitemamp URL Settings
SITEMAP_SAVE_AS = 'sitemap.xml'




