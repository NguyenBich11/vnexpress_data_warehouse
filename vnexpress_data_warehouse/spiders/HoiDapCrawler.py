import scrapy
import csv

class HoidapcrawlerSpider(scrapy.Spider):
    name = "HoiDapCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/suc-khoe/cac-benh/da-lieu/hoi-dap"]

    def parse(self, response):
        data = {
            'comment' : "\n".join(response.css('section.section div.width_common div.content_less ::text').getall()),
            'count_comment' : len(response.css('section.section div.width_common div.content_less ::text').getall()),
        }

        with open('DataHoiDap.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['comment', 'count_comment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        
