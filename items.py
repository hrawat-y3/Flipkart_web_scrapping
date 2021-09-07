# Define here the models for your scraped items


import scrapy


class FlipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    original_price = scrapy.Field()
    sale_price = scrapy.Field()
    discount_price = scrapy.Field()
    image_url = scrapy.Field()
    product_category = scrapy.Field()
    product_page_url = scrapy.Field()


    pass
