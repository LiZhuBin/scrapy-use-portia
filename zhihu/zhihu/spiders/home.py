# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem


class HomeSpider(scrapy.Spider):
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    name = 'home'
    start_urls = ['https://www.zhihu.com/', ]

    def parse(self, response):
        print(response.body)
        item = ZhihuItem()
        for sel in response.xpath('//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div/div/div[2]'):
            item['actor_image'] = sel.xpath('text()').extact()
            print(sel.xpath('text()'))
        yield item
