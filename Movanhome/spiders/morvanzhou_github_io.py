from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PythonItem, PortiaItem


class MorvanzhouGithubIo(BasePortiaSpider):
    name = "morvanzhou.github.io"
    allowed_domains = ['morvanzhou.github.io']
    start_urls = ['https://morvanzhou.github.io/tutorials/']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PythonItem, None, '#recent-update > li:nth-child(-n+5) > a',
                   [Field('field1', '#recent-update > li > a > .lazy-img::attr(src)', [])])]]
