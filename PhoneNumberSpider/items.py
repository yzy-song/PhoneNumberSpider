# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhonenumberspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #省份名
    province = scrapy.Field()
    #城市名
    city = scrapy.Field()
    #城市对应url
    city_url = scrapy.Field()
    #区号
    area_code = scrapy.Field()
