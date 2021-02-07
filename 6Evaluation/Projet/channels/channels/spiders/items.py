# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChannelsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    name = scrapy.Field()
    streamername = scrapy.Field()
    timestamp = scrapy.Field()
    audience = scrapy.Field()
