# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field() # id of the product
    name = scrapy.Field()   # name of the product
    description = scrapy.Field()   # description of product
    slug = scrapy.Field()   # slug of product
    meta_description = scrapy.Field()   # description of product
    price = scrapy.Field()  # list of prices
    old_price = scrapy.Field()  # float value
    updated_at = scrapy.Field()  # sale date
    category = scrapy.Field()  # string value
    storeUrl = scrapy.Field()  # external Product url
    images = scrapy.Field()  # array of images
    is_featured = scrapy.Field()  # if featured or not
