#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import scrapy
from idna import unicode
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

from ..items import ScrapyLearnItem


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow_simple'
    start_urls = ['https://stackoverflow.com']

    def parse(self, response):
        item = ItemLoader(item=ScrapyLearnItem(), response=response)
        item.add_css('title', 'h1::text', MapCompose(unicode.strip))
        item.add_css('body', '.question-summary .summary h3 a::text')
        return item.load_item()


