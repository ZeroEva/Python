# -*- coding: utf-8 -*-
import re

import scrapy
from idna import unicode
from scrapy.loader import ItemLoader
from urllib import parse

from scrapy.loader.processors import MapCompose

from ..items import ScrapyLearnItem


class ManualSpider(scrapy.Spider):
    start_urls = ['http://e-shuushuu.net/']
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "DNT": "1",
        "Host": "e-shuushuu.net",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://e-shuushuu.net/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }
    name = 'manual'

    def parse(self, response):
        url = response.css('.pagination .next a::attr(href)').extract_first()
        url_join = response.urljoin(url)
        print("===A===", url_join)
        yield scrapy.Request(url_join)

        item_selector = response.css('#content .image_thread h2 a::attr(href)').extract()
        for url in item_selector:
            url_join = response.urljoin(url)
            print("===B===", url_join)
            yield scrapy.Request(url_join, callback=self.parse_item)

    def parse_item(self, response):
        item = ItemLoader(item=ScrapyLearnItem(), response=response)
        item.add_css('image_url', '#content .image_block .thumb_image::attr(href)',
                     MapCompose(lambda url: response.urljoin(url)))
        item.add_css('img_thumb_url', '#content .image_block .thumb_image img::attr(src)',
                     MapCompose(lambda url: response.urljoin(url)))
        item.add_css('title', '#content .image_block .title h2 a::text', MapCompose(unicode.strip))
        # item.add_css('info', '.meta', MapCompose(unicode.strip))
        return item.load_item()
