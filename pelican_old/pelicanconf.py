#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import join, dirname, pardir

BASE_DIR = dirname(__file__)

AUTHOR = 'SDH Dobřichovice'
SITENAME = 'Hasiči Dobřichovice'
SITEURL = 'http://www.sdhdobrichovice.cz'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

LOCALE = 'cs_CZ.UTF-8'
DEFAULT_LANG = 'cs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('město Dobřichovice', 'http://www.dobrichovice.cz/'),
    ('HZS Středočeského kraje', 'http://www.hzscr.cz/hzs-stredoceskeho-kraje.aspx'),
)

# Social widget
SOCIAL = (
    ('Facebook', 'https://www.facebook.com/Hasi%C4%8Di-Dob%C5%99ichovice-186516169180/?fref=ts'),
)

PLUGIN_PATHS = [join(BASE_DIR, pardir, 'pelican-plugins')]
PLUGINS = ['photos', 'lightbox']
PHOTO_LIBRARY = join(BASE_DIR, 'content', 'images', 'gallery')
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)


THEME = join(BASE_DIR, 'themes', 'bricks')

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
