# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):

    good_name = scrapy.Field()
    good_url = scrapy.Field()
    good_price = scrapy.Field()
    good_star = scrapy.Field()
    good_commentsnum = scrapy.Field()
    good_commentsurl = scrapy.Field()