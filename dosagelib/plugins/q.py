# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..scraper import _ParserScraper
from ..helpers import xpath_class, bounceStarter


class QuantumVibe(_ParserScraper):
    url = 'https://www.quantumvibe.com/'
    stripUrl = url + 'strip?page=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "disppageV3?story=qv")]'
    prevSearch = '//a[./img[contains(@src, "nav/prevstrip")]]'


class QuestionableContent(_ParserScraper):
    url = 'http://www.questionablecontent.net/'
	starter = bounceStarter
    stripUrl = url + 'view.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[text()="Previous"]'
	nextSearch = '//a[text()="Next"]'
    help = 'Index format: n (unpadded)'
	textSearch = '//div[@id="news"]//text()'
	textOptional = True


class Qwantz(_ParserScraper):
    url = 'http://www.qwantz.com/index.php'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[{}]'.format(xpath_class('comic'))
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: n'
