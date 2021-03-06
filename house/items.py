# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    type = scrapy.Field()
    size = scrapy.Field()
    orientation = scrapy.Field()
    fitment = scrapy.Field()
    price = scrapy.Field()
    
