# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
     actor_image = scrapy.Field()
     actor_name = scrapy.Field()
     acticle_title = scrapy.Field()


