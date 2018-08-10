# -*- coding: utf-8 -*-
import scrapy
from hao123.items import Hao123Item


class Hao123Spider(scrapy.Spider):
    name = 'hao123'
    allowed_domains = ['https://www.hao123.com/?tn=98160835_hao_pg']
    start_urls = ['https://www.hao123.com/?tn=98160835_hao_pg',]

    def parse(self, response):
        item = Hao123Item()
        for sel in response.xpath('//*[@id="site"]/div/ul/li/a'):
            item['site_name'] = sel.xpath("/text()").extract()
            item['site_href'] = sel.xpath('/@href').extract()
            print(item['site_name'])


        yield item

