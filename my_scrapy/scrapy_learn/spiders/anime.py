# -*- coding: utf-8 -*-
import scrapy
from idna import unicode
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider, Rule

from ..items import ScrapyLearnItem


class AnimeSpider(CrawlSpider):
    name = 'anime'
    start_urls = ['http://e-shuushuu.net/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//*[contains(@class,'next')]"), follow=True),
        Rule(LinkExtractor(restrict_css='#content .image_thread h2'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ItemLoader(item=ScrapyLearnItem(), response=response)
        item.add_css('image_url', '#content .image_block .thumb_image::attr(href)',
                     MapCompose(lambda url: response.urljoin(url)))
        item.add_css('img_thumb_url', '#content .image_block .thumb_image img::attr(src)',
                     MapCompose(lambda url: response.urljoin(url)))
        item.add_css('title', '#content .image_block .title h2 a::text', MapCompose(unicode.strip))
        item.add_css('info', '.meta', MapCompose(unicode.strip))
        return item.load_item()

    def info_parse(self,value):
        value = "asdf"
        value.strip()

