import scrapy
from ..items import FlipItem

class FlipSpiderSpider(scrapy.Spider):
    name = 'flip_spider'

    def start_requests(self):
        start_urls = [#add the url/urls in quotes]
        for urls in start_urls:
            for i in range(1, 26):
                x = urls.format(i)
                yield scrapy.Request(url=x, callback=self.parse)



    def parse(self, response):
        items = FlipItem()
        name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "IRpwTa", " " ))]').xpath('text()').getall()
        brand = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_2WkVRV", " " ))]').xpath('text()').getall()
        original_price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_3I9_wc", " " ))]').xpath('text()').getall()
        sale_price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_30jeq3", " " ))]').xpath('text()').getall()
        discount_price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_3Ay6Sb", " " ))]//span').xpath('text()').getall()
        image_url = response.css('._1a8UBa').css('::attr(src)').getall()
        product_category = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_1jJQdf", " " ))]').xpath('text()').getall()
        product_page_url = response.url

        sale_price = [sale_price[i].strip('₹') for i in range(len(sale_price))]
        discount_price = [discount_price[i].strip('% off') for i in range(len(discount_price))]
        original_price = [original_price[i] for i in range(1, len(original_price), 2)]

        d = {ord(x): "" for x in ","}  # removing special charcater from data
        original_price = [x.translate(d) for x in original_price]  # removing special character from data

        items['name'] = str(name)
        items['brand'] = str(brand)
        items['original_price'] = original_price
        items['sale_price'] = sale_price
        items['discount_price'] = discount_price
        items['image_url'] = image_url
        items['product_category'] = product_category
        items['product_page_url'] = product_page_url


        yield items
        pass
