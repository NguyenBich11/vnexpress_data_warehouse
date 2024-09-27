import scrapy


class BenhnguoilonSpider(scrapy.Spider):
    name = "BenhNguoiLon"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/"]

    def parse(self, response):
        pass
