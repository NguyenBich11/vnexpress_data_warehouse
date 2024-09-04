
import scrapy
import csv

class PhauThuatNoiSoiSpider(scrapy.Spider):
    name = "Phau_Thuat_Noi_Soi"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/bat-ngo-phat-hien-u-thuc-quan-khi-noi-soi-da-day-4744532.html',
        'https://vnexpress.net/beo-phi-thu-pham-gay-nhieu-benh-4705379.html',
        'https://vnexpress.net/nang-ruot-doi-khien-nguoi-dan-ong-non-oi-suot-hai-nam-4701594.html',
        'https://vnexpress.net/noi-soi-tieu-hoa-phat-hien-som-dieu-tri-khoi-ung-thu-4693418.html',
        'https://vnexpress.net/noi-soi-qua-duong-mieng-cat-u-thuc-quan-4680686.html',
        'https://vnexpress.net/thung-da-day-do-vien-thuoc-nguyen-vi-4676641.html',
        'https://vnexpress.net/tuong-bat-thuong-thai-ky-hoa-viem-ruot-thua-4663347.html',
        'https://vnexpress.net/cat-polyp-dai-trang-co-nguy-hiem-khong-4630081.html'
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
        with open('PhauThuatNoiSoi.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)