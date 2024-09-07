import scrapy
import csv

class HoHapHiemGapSpider(scrapy.Spider):
    name = "Ho_Hap_Hiem_Gap"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/kham-suc-khoe-hoc-duong-bac-si-phat-hien-be-gai-bat-thuong-tim-phoi-4688876.html',
        'https://vnexpress.net/vi-khuan-an-thit-nguoi-co-lay-khong-4535888.html',
        'https://vnexpress.net/viem-phoi-do-nam-4520092.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-tre-co-trieu-chung-ho-hap-hau-covid-19-4452703.html',
        'https://vnexpress.net/nhung-dieu-can-biet-ve-thuoc-dieu-tri-hen-suyen-4437165.html',
        'https://vnexpress.net/benh-bui-phoi-silic-pho-bien-o-nguoi-tren-40-4436530.html',
        'https://vnexpress.net/benh-sarcoidosis-dau-hieu-nguyen-nhan-va-phuong-phap-dieu-tri-4436531.html',
        'https://vnexpress.net/benh-phoi-hiem-gap-khien-be-gai-9-nam-thieu-mau-3730384.html',
        'https://vnexpress.net/kho-tho-do-vo-ken-khi-phoi-4769681.html',
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': ''.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'location': response.css('span.location-stamp::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('HoHapHiemGap.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date','location', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
