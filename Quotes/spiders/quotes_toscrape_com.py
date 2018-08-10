from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import QuotesToScrapeItem, PortiaItem


class QuotesToscrape(BasePortiaSpider):
    name = "quotes.toscrape.com"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(QuotesToScrapeItem,
                   None,
                   '.quote',
                   [Field('content',
                          '.text *::text',
                          []),
                       Field('autor',
                             'span:nth-child(2) > .author *::text',
                             []),
                       Field('tag',
                             '.tags a.tag *::text',
                             [])])]]
