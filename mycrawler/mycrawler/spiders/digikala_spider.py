import scrapy

class DigikalaSpider(scrapy.Spider):
    name = 'digikala_spider'
    allowed_domains = ['digikala.com']
    start_urls = ['https://www.digikala.com/']

    def parse(self, response):
        # جستجو برای دریافت محصولات
        for product in response.css('div.c-product-box'):
            title = product.css('a.c-product-box__title::text').get()
            price = product.css('div.c-price__value::text').get()
            link = product.css('a::attr(href)').get()

            yield {
                'title': title.strip() if title else 'N/A',
                'price': price.strip() if price else 'N/A',
                'link': response.urljoin(link) if link else 'N/A',
            }
