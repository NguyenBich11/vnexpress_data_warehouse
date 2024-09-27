import scrapy


class BenhtreemSpider(scrapy.Spider):
    name = "BenhTreEm"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/"]

    def parse(self, response):
        pass
