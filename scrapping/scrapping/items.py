# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappingItem(scrapy.Item):
    product_name = scrapy.Field()
    discription = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()

