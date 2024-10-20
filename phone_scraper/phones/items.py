# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhonesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class PhoneSpecItem(scrapy.Item):
    phone_brand = scrapy.Field()
    phone_model = scrapy.Field()
    price = scrapy.Field()
    specs = scrapy.Field()
    pricing = scrapy.Field()
