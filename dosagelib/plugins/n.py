# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..helpers import indirectStarter, bounceStarter
from ..util import tagre


class Namesake(_BasicScraper):
    url = 'http://namesakecomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'prologue-cover-3'
    imageSearch = compile(tagre("img", "src", r'([^"]*/wp-content/uploads/[^"]+)', after='title='))
    prevSearch = compile(tagre("a", "href", r'([^"]*/comic/[^"]+)', after='navi-prev'))
    help = 'Index format: name'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgmatch = compile(r'uploads/(\d+)/(\d+)/(.+)$').search(imageUrl)
        return '-'.join(imgmatch.groups())


class NamirDeiter(_BasicScraper):
    description = u'Namir Deiter, by Isabel Marks'
    url = 'http://www.namirdeiter.com/'
    rurl = escape(url)
    stripUrl = url + 'comics/index.php?date=%s'
    firstStripUrl = stripUrl % '19991128'
    imageSearch = compile(tagre("img", "src", r"'?(%scomics/\d+\.jpg)'?" % rurl, quote=""))
    prevSearch = compile(tagre("a", "href", r'(%scomics/index\.php\?date=\d+)' % rurl, quote="'")+"Previous")
    help = 'Index format: yyyymmdd'


class Nedroid(_BasicScraper):
    url = 'http://nedroid.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2005/09/2210-whee'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class NeoEarth(_BasicScraper):
    description = u'Neo-Earth - Web comic by Bryan King - Updated Every Monday'
    url = 'http://www.neo-earth.com/NE/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2007-03-23'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'


class NewAdventuresOfBobbin(_BasicScraper):
    url = 'http://www.bobbin-comic.com/bobbin_strips/'
    imageSearch = compile(tagre("a", "href", r'(\d+\.gif)'))
    multipleImagesPerStrip = True
    help = 'Index format: none'


class NewWorld(_BasicScraper):
    url = 'http://www.tfsnewworld.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/08/30/63'
    imageSearch = compile(r'<img src="(http://www.tfsnewworld.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/stripn'


class Nicky510(_BasicScraper):
    url = 'http://www.nickyitis.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'close-enough'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="Previous"))
    help = 'Index format: stripname'


class NekkoAndJoruba(_BasicScraper):
    url = 'http://www.nekkoandjoruba.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '7'
    imageSearch = compile(r'<img src="(http://www\.nekkoandjoruba\.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">&lsaquo;</a>')
    help = 'Index format: nnn'


class NekoTheKitty(_BasicScraper):
    url = 'http://www.nekothekitty.net/'
    rurl = escape(url)
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % '936393/001-video-games'
    starter = bounceStarter(url, compile(tagre("a", "href", r'(%scomics/[^"]+)' % rurl) +
      tagre("img", "src", r'%sfiles/smallnext\.png' % rurl)))
    imageSearch = compile(tagre("img", "src", r'(http://(?:img\d+|www)\.smackjeeves\.com/images/uploaded/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%scomics/[^"]+)' % rurl) +
      tagre("img", "src", r'%sfiles/smallprev\.png' % rurl))
    help = 'Index format: n/n-name'


class NichtLustig(_BasicScraper):
    url = 'http://www.nichtlustig.de/main.html'
    stripUrl = 'http://static.nichtlustig.de/toondb/%s.html'
    lang = 'de'
    imageSearch = compile('background-image:url\((http://static\.nichtlustig\.de/comics/full/\d+\.jpg)')
    prevSearch = compile(tagre("a", "href", r'(http://static\.nichtlustig\.de/toondb/\d+\.html)'))
    help = 'Index format: yymmdd'
    starter = indirectStarter(url,
                              compile(tagre("a", "href", r'([^"]*toondb/\d+\.html)')))


class Nnewts(_BasicScraper):
    url = 'http://nnewts.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'nnewts-page-1'
    imageSearch = compile(tagre("img", "src", r'(%snewty/comics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s(?:nnewts-)?page-\d+/)' % rurl, after="navi-prev"))
    help = 'Index format: page-number'


class Nodwick(_BasicScraper):
    description = u'Welcome to Nodwick.com - A fantasy farce for the whole party!'
    url = 'http://comic.nodwick.com/'
    rurl = escape(url)
    stripUrl = url + "?p=%s"
    imageSearch = compile(tagre("img", "src", r'(%snodwickstrips/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: stripnumber'


class NobodyScores(_BasicScraper):
    description = u'Nobody Scores! A little comic about inevitable disaster'
    url = 'http://nobodyscores.loosenutstudio.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre("img", "src", r'(%scomix/[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(r'<a href="(%sindex.php.+?)">the one before </a>' % rurl)
    help = 'Index format: nnn'


class NoNeedForBushido(_BasicScraper):
    baseUrl = 'http://noneedforbushido.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'latest/'
    stripUrl = baseUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/comic/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="previous-comic-link"))
    help = 'Index format: yyyy/comic/nnn'


class Nukees(_BasicScraper):
    description = u'Nukees, The Atomic Comic Strip'
    url = 'http://www.nukees.com/'
    stripUrl = url + 'd/%s'
    firstStripUrl = stripUrl % '19970121'
    imageSearch = compile(r'"comic".+?"(/comics/.+?)"')
    prevSearch = compile(r'"(/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'
