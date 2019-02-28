# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from ..items import ScrapyLearnItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']

    start_urls = ['https://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        ItemLoader(item=ScrapyLearnItem, response=response)
        item = ScrapyLearnItem()
        item['title'] = response.css('h1::text').extract()
        item['body'] = response.css('.question-summary .summary h3 a::text').extract()
        return item
