import scrapy


class OlxItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    condition = scrapy.Field()
    url = scrapy.Field()
