# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScrapyLearnItem(Item):
    # Primary fields
    title = Field()
    body = Field()
    # Calculated fields
    images = Field()
    location = Field()
    # HouseKeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
    # uu
    image_urls = Field()
    img_thumb_url = Field()
    file_size = Field()
    info = Field()

