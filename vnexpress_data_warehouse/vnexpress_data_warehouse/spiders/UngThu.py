
import scrapy
import csv

class UngThuSpider(scrapy.Spider):
    name = "Ung_Thu"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/vi-khuan-hp-co-gay-ung-thu-da-day-4785874.html',
        'https://vnexpress.net/trac-nghiem-de-biet-ban-co-nguy-co-ung-thu-truc-trang-4776961.html',
        'https://vnexpress.net/tai-sao-phu-nu-de-mac-ung-thu-tui-mat-4776082.html',
        'https://vnexpress.net/beo-phi-lam-tang-nguy-co-ung-thu-dai-truc-trang-the-nao-4773632.html',
        'https://vnexpress.net/kiem-tra-dau-hieu-ung-thu-da-day-4772111.html',
        'https://vnexpress.net/phat-hien-u-ac-tinh-tu-dau-hieu-an-kho-tieu-4769274.html',
        'https://vnexpress.net/cat-nang-ong-mat-chu-ngan-ung-thu-4766363.html',
        'https://vnexpress.net/phat-hien-ung-thu-da-day-giai-doan-cuoi-du-khong-trieu-chung-4762241.html'
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': '\n'.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('UngThu.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)