import scrapy
from ..items import ScrappingItem

class ScrapNecklaceSets(scrapy.Spider):
    name = 'NecklaceSets'
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']

    def parse(self,response):
        products = response.xpath("//div[@class = 'catgList']/ul[@id = 'JsonProductList']/li")

        for product in products:
            product_link = product.xpath(".//@data-url").extract_first()
            yield scrapy.Request(url=product_link,callback=self.gotolink)

    def gotolink(self,response):
        items = ScrappingItem()

        product_name  = response.xpath('//div[@class = "prodRight"]/h1/text()').extract_first()
        discription = response.xpath('//div[@id="tab-1"]/p/text()').extract_first()
        price = response.xpath('//div[@id="wrapper"]/div[4]/div/div[2]/div[2]/h4/span[2]/text()').extract_first()
        image_urls =  response.xpath('//li[@class = "zoomli"]/a/@data-image').extract()

        items['product_name'] = product_name
        items['discription'] = discription
        items['price'] = price
        items['image_urls'] = image_urls

        yield items


