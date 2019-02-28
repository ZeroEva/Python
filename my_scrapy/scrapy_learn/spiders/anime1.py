#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'anime1'
    start_urls = ['http://e-shuushuu.net/']

    def parse(self, response):
        for href in response.css('.image_block .thumb a::attr(href)'):
            full_url = response.urljoin(href.extract())
            print(full_url)
